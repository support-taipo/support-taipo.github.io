# Tai Po Doctors Map

A volunteer map of doctors and clinics across Hong Kong, created to help residents affected by the Tai Po fire find primary care information.

**[Open the map](https://support-taipo.github.io/)**

## Features

- English and Traditional Chinese listings
- Doctor and clinic details, addresses and phone numbers
- Search and an interactive map that works on mobile
- Scheme information published in the source directory

## Data and maps

Listings come from the Hong Kong [Primary Care Directory](https://apps.pcdirectory.gov.hk/). The site loads [`doctors.csv`](doctors.csv) and [`doctors_tc.csv`](doctors_tc.csv), with location corrections in [`gps_fallback.csv`](gps_fallback.csv).

The map uses locally bundled [Leaflet](https://leafletjs.com/) and Lands Department's public CSDI Map API for basemaps and place labels. Source and privacy information is available in the map's **Sources and privacy / 來源及私隱** panel.

## Data updates

A [GitHub Actions workflow](.github/workflows/update-doctors.yml) is scheduled daily, alternating between English and Traditional Chinese. It runs the Python/Selenium scraper in [`scraper/`](scraper/) and commits changes when records differ.

For data fixes, update the scraper or location corrections rather than editing the generated CSVs.

## Run locally

Serve the repository with a static web server:

```sh
python -m http.server 8000
```

Open <http://localhost:8000>.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Use [GitHub issues](https://github.com/support-taipo/support-taipo.github.io/issues) for corrections and feedback.

## Credits and licence

Directory source: Primary Healthcare Commission, Health Bureau, Government of the Hong Kong SAR. Basemaps and labels: Lands Department. See [asset notices](assets/README.md) for credits and source terms.

Project code uses the [MIT License](LICENSE). Leaflet retains its [BSD 2-Clause licence](assets/leaflet/LICENSE).
