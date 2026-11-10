"""Offline checks for collection failures that must preserve published records."""
import csv
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import MagicMock, patch


SPEC = importlib.util.spec_from_file_location('doctors_scraper', Path(__file__).resolve().parents[1] / 'scraper/doctors_scraper.py')
scraper = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(scraper)


class CollectionIntegrityTests(unittest.TestCase):
    def test_failed_region_rejects_partial_collection_and_closes_browser(self):
        browser = MagicMock()
        with patch.object(scraper, 'setup_driver', return_value=browser), patch.object(scraper, 'scrape_region', side_effect=['HK records', None]):
            with self.assertRaisesRegex(RuntimeError, 'keeping the previous'):
                scraper.scrape_all_regions('EN')
        browser.quit.assert_called_once()

    def test_complete_collection_includes_each_region(self):
        browser = MagicMock()
        with patch.object(scraper, 'setup_driver', return_value=browser), patch.object(scraper, 'scrape_region', side_effect=['HK', 'Kowloon', 'NT']):
            self.assertEqual(scraper.scrape_all_regions('TC'), 'HK\nKowloon\nNT')
        browser.quit.assert_called_once()

    def test_failed_next_page_is_not_accepted_as_end_of_results(self):
        browser = MagicMock()
        table = MagicMock()
        table.get_attribute.return_value = '<tbody><tr><td class="PHName">Example</td></tr></tbody>'
        browser.find_element.side_effect = [MagicMock(), table]
        browser.find_elements.return_value = [MagicMock()]
        browser.execute_script.side_effect = [None, RuntimeError('next page failed')]
        with patch.object(scraper, 'WebDriverWait'), patch.object(scraper.time, 'sleep'):
            self.assertIsNone(scraper.scrape_region(browser, 'CommandHK', 'https://example.invalid/', max_retries=1))

    def test_empty_collection_keeps_existing_csv(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'doctors.csv'
            output.write_text('previous records', encoding='utf-8')
            with self.assertRaises(ValueError):
                scraper.save_to_csv([], str(output))
            self.assertEqual(output.read_text(encoding='utf-8'), 'previous records')

    def test_csv_publish_preserves_unicode_and_quoted_fields(self):
        record = dict(Name='Example 醫生', ProfileLink='https://apps.pcdirectory.gov.hk/Public/EN/Viewdetails?dp=123', Description='Example "Clinic"', Address='Room A, Example Road', Phone='1234 5678', Lat='22.3', Lon='114.1', Programs='Example scheme')
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'doctors.csv'
            scraper.save_to_csv([record], str(output))
            with output.open(encoding='utf-8', newline='') as source:
                self.assertEqual(list(csv.DictReader(source)), [record])
            self.assertEqual(list(Path(directory).glob('*.tmp')), [])


if __name__ == '__main__':
    unittest.main()
