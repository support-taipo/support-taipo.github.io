# Contributing

Thank you for helping. This project is maintained by volunteer doctors, not professional programmers, so clear, self-contained contributions are especially welcome.

## Ways to help

- **Scraper maintenance** — the Primary Care Directory website changes over time. When it does, `scraper/doctors_scraper.py` breaks. Fixes that keep the scraper resilient are the most valuable contributions.
- **Geocoding** — addresses that fail to geocode need manual coordinates in `gps_fallback.csv`.
- **Map UI** — accessibility, mobile layout, and clarity improvements to `index.html`.
- **Data quality** — checking that the English (`doctors.csv`) and Traditional Chinese (`doctors_tc.csv`) datasets stay in sync.

## Reporting issues

Open a GitHub issue and include:

1. What you expected vs. what happened
2. The date/time (data refreshes daily, which helps narrow things down)
3. For map problems: the affected clinic or district

## Development notes

- The scraper uses Python with Selenium (`scraper/requirements.txt`). It runs headless Chrome in GitHub Actions; no local setup is required to keep the site updated.
- The site is fully static — `index.html` reads the CSVs directly. To test locally, serve the repo root with any static file server.
- Data commits (`Update doctors data`) are automated. Please do not edit `doctors.csv` / `doctors_tc.csv` by hand; fix the scraper or `gps_fallback.csv` instead.

## Pull requests

- Keep changes focused — one fix or feature per PR.
- Do not commit credentials, tokens, or scraped data outside the existing CSV files.
- Explain in the PR description what you changed and why. We will review as time allows; please be patient.
