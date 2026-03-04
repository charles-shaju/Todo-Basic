# Q39 – Deploy a Full-Stack App (Free Hosting)

This mini project is a small **full-stack** Django app:
- Backend: Django + SQLite + JSON API endpoints
- Frontend: simple HTML + JavaScript calling the API
- Ready for production-style serving using `gunicorn` + `whitenoise`

## Run Locally
```bash
python manage.py migrate
python manage.py runserver
```
  
## Check Output
- App: http://127.0.0.1:8000/
- API list/create: http://127.0.0.1:8000/api/todos/

## Deploy (Example: Render)
Render’s free tiers change over time, but the general steps are:

1) Push this folder to a GitHub repo
2) Create a new **Web Service** on Render connected to the repo
3) Set:
- **Build command**:
  ```bash
  pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate --noinput
  ```
- **Start command**:
  ```bash
  gunicorn config.wsgi:application
  ```
4) Set environment variables on Render:
- `DJANGO_SECRET_KEY`: a long random value
- `DJANGO_DEBUG`: `0`
- `DJANGO_ALLOWED_HOSTS`: your Render domain (comma-separated if multiple)

Notes:
- SQLite is OK for demos; many hosts recommend Postgres for real deployments.
- If you deploy with Postgres later, update `DATABASES` in `config/settings.py`.
