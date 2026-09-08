# Doctors Map — Tai Po Fire Relief

A live map of doctors and clinics in Hong Kong, built to help residents affected by the Tai Po fire find nearby primary care that is accepting patients.

**View the map: <https://support-taipo.github.io>**

## Why this exists

Following the Tai Po fire disaster, affected residents need to find nearby doctors quickly — for injuries, prescription refills, chronic disease care, and displacement-related health needs. Public information was spread across government directory pages that are hard to search under pressure.

This project turns the Hong Kong [Primary Care Directory](https://apps.pcdirectory.gov.hk) into a simple, fast, map-based view that works on a phone.

## What it shows

- Doctors and clinics across Hong Kong, in both **English** and **Traditional Chinese**
- Practice address and phone number
- Government schemes accepted at each practice, e.g.:
  - Elderly Health Care Voucher Scheme (HCVS)
  - Chronic Disease Co-Care Scheme

## How it works

1. A scheduled GitHub Actions workflow runs the Selenium scraper in [`scraper/`](scraper/) against the Primary Care Directory (English and Traditional Chinese versions).
2. Results are written to [`doctors.csv`](doctors.csv) and [`doctors_tc.csv`](doctors_tc.csv), with manual geocoding corrections in [`gps_fallback.csv`](gps_fallback.csv).
3. The map at <https://support-taipo.github.io> is generated from the latest CSV data — no server, no database, fully static.

You can see the data freshness in the commit history: the CSVs are updated automatically every day.

## Data source and accuracy

- All doctor and clinic data comes from the Hong Kong Department of Health's Primary Care Directory, a public government directory.
- Listings may be incomplete or out of date. Always call ahead before travelling to a clinic.
- This project is an independent volunteer effort and is not affiliated with the Department of Health or the Primary Care Directory.

## Maintainers

This project is maintained by volunteer doctors, not professional programmers. We use AI-assisted development to keep the project going with limited time.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Issues and pull requests are welcome — especially help with the scraper, geocoding, and the map UI.

## License

Code is released under the [MIT License](LICENSE).
