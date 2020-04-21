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
  
### Other Notes
- I intended to introduce a privileged user level, and hiding some columns
  from others, but did not have time.
- The revenue calculation should be aggregated up the hierarchy recursively,
  but I haven't had time to think about that and the implications for tree
  nodes that are both aggregators and have volumes in their own right.
- I took the hint that you could not rely on inference from the codes about hierarchy,
  and started out with data models that explicitly modelled hierarchy. That's partly why
  I chose to model the 4 digit heading codes as strings not integers - to reinforce the idea that
  they are just tags. But when I got more deeply familiar with the API response payloads, I found that
  in order to **display** the hierarchy I had no need to know the hierarchy. The payloads express a
  visual paradigm - and cites the indentation level for each row. I believe they also express formal hierarchy too
  through the **includes** fields, but I didn't need that to display the table. I'm regretting that now, because
  I would need explicit hierarchy to aggregate the revenues.
- I also started out with a Duty model that modelled the headline percentage and a plus/minus component along
  with its units. But then when I found out that the api payloads express duty as a pre-formatted
  string (that includes html markup) I realised that it would take too long to parse the components out,
  and be fragile. This does beg the question how you would do calculations based on duty though?
