An mvp django with one app intended to be copied from to shortcut starting a new project.

See commits for what's available at each iteration - the first is not viable.

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

Browse to: ```http://127.0.0.1:8000/tariffs```

### Visit admin site
`python manage.py runserver`

Browse to: ```http://127.0.0.1:8000/admin```