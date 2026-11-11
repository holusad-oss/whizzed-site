# whizzed-site

Static website for **Whizzed** (operated by DGFIX LTD, company number 10646551, registered office 13 Chestnut Road, Dartford DA1 2LB).

- Pages: Home/About, Games, Contact, Privacy, Meridian privacy policy (`/privacy/meridian/`).
- Source: `src/build.py` (Python + `markdown`) renders the HTML; `src/meridian-privacy.md` is the Meridian policy text.
- Preview banner + `noindex` are controlled by `PREVIEW_NOTE` in `src/build.py` — set to `False` before going live.
