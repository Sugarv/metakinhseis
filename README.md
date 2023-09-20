# Εφαρμογή υποβολής / επεξεργασίας μετακινήσεων Συμβούλων Εκπαίδευσης

Γραμμένη σε Django με Β.Δ. SQLite

# Web Application for submission / processing of transfers of Education Consultants

Developed in Django, using SQLite as the data storage

### Instructions for production deployment

- Install Docker
- Create `settings.py` from `settings-docker.py` in `metakinhseis` folder
- Modify .env file: set a complex secret ket
- Run `docker compose up -d` to build containers & deploy
- Access app at http://localhost:8080/metakinhseis for the app or http://localhost:8080/admin for the admin backend

### Instructions for development setup

- Create a [virtual environment](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
- Install requirements: `pip install -r requirements.txt`
- Migrate DB: `python manage.py migrate`
- Create a superuser: `python manage.py createsuperuser`
- Copy settings-dev.py to settings.py (in folder metakinhseis)
- Run: `python manage.py runserver`
- Go to http://localhost:8000/metakinhseis for the app or http://localhost:8000/admin for the admin backend
