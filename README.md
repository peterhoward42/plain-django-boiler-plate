DIT App

### Install and Build

```
cd <here>
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cd ./dit

python manage.py makemigrations tariffs
python manage.py migrate
```

### Setup an admin user
python manage.py createsuperuser

### Run App
`python manage.py runserver`

Browse to: ```http://127.0.0.1:8000/tariffs/0708```

### Visit admin site
`python manage.py runserver`

Browse to: ```http://127.0.0.1:8000/admin```

### Usage

- You can try other 4 digit heading codes in the URL.
- The first time you try a new heading, there is a slow response because.
  the app is fetching the inaugural data from the GovUK API to populate
  the local database.
- Some columns are not populated from the GovUK data...
- Specifically VAT, Price, Volume, and Revenue
- All of these (except Revenue) can be edited manually in the admin site
- In the case of VAT - I could not find a source for it in the API
- In the case of Revenue, IFF both Price and Volume contain numbers, then
  the revenue is calculated and shown
- The Duty data available in the API I found to be both sparse and odd,
  but the public website shows it less sparsely? Does the public website
  feed from other APIs too perhaps?
- The display page shows how stale the data is in hours and, clicking the
  "Update from GovUK" button, re-fetches the latest for the current heading.
- I intended to introduce a privileged user level, and hiding some columns
  from others, but did not have time.
