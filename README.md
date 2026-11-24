# whizzed-site

Static website for **Whizzed** (operated by DGFIX LTD, company number 10646551, registered office 13 Chestnut Road, Dartford DA1 2LB).

- Pages: Home/About, Games, a landing page for each live app (`/games/stellar-run/`, `/games/flashsums/`, `/games/meridian/`), Contact, Privacy, and app privacy policies (`/privacy/stellar-run/`, `/privacy/flashsums/`, `/privacy/meridian/`, `/privacy/printcost/`).
- Source: `src/build.py` (Python + `markdown`) renders the HTML; policy text lives in `src/*-privacy.md`.
- `robots.txt` and `sitemap.xml` are written by the build.
- Preview banner + `noindex` are controlled by `PREVIEW_NOTE` in `src/build.py` — keep this `False` on the live site.
