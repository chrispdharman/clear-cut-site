# clear-cut-site

## To run locally:
- Navigate to this repo
    - `cd [this_directory]/`
- Setup venv if you haven't already:
    - `python3 -m venv venv`
    - `source venv/bin/activate`
    - `pip install -r requirements.txt`
- Activate venv if you haven't already:
    - `source venv/bin/activate`
- Bring up the django server (default http://localhost:8000):
    - `python app/manage.py runserver`
- If you need login credentials, setup a new superuser via terminal (Django) command:
    - `python app/manage.py createsuperuser`
