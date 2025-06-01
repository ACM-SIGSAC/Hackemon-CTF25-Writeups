
# ImpossibleLoginCTF - ACM Portal with Hints

This is a web-based CTF challenge designed to teach basic enumeration and logic-based exploration techniques.

## Setup Instructions
```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
python app.py
```

## Objective
- Find the hidden flag.
- Explore the pages carefully.
- Pre-auth tokens expire after 20 seconds.

## Hints
- Explore `/pre-auth`, `/login`, `/dashboard`
- Hidden hints are left in comments, 404 page, and robots.txt

## Flag Format
ACM{you_found_it}

## Good Luck!
