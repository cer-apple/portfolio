# Portfolio Website

A minimal Django-powered personal portfolio with a monochrome aesthetic — Playfair Display serif headings on a black canvas, Inter for body text.

## Setup

### 1. Activate virtual environment

```bash
source venv/bin/activate
```

On Windows:
```bash
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run migrations

```bash
python manage.py migrate
```

### 4. Start the development server

```bash
python manage.py runserver
```

The site is available at `http://localhost:8000`.

## Project Structure

```
portfolio/
├── portfolio/              # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/                   # Main app (views, URLs)
│   ├── views.py
│   ├── urls.py
│   ├── static/main/images/ # Portrait and profile images
│   └── migrations/
├── templates/              # HTML templates
│   ├── base.html           # Shared layout + navigation
│   ├── top.html            # Home (hero portrait)
│   ├── profile.html        # Bio
│   ├── education.html      # Academic history
│   ├── work.html           # Professional experience
│   └── contact.html        # Email + social links
├── static/main/css/        # Stylesheet
│   └── style.css
├── media/                  # User uploads (empty by default)
├── requirements.txt
└── manage.py
```

## Pages

- **TOP** — Hero section with portrait and tagline
- **PROFILE** — Bio and background
- **EDUCATION** — Academic credentials
- **WORK** — Professional experience and side business
- **CONTACT** — Email, LinkedIn, GitHub

## Customization

### Colors & fonts

Edit [static/main/css/style.css](static/main/css/style.css):
- Background: `background-color: #000` on `body`
- Fonts: Playfair Display (headings), Inter (body)

### Navigation links

Edit [templates/base.html](templates/base.html).

### Page content

Each page is a standalone template under [templates/](templates/). The `{% extends "base.html" %}` line pulls in the shared layout.

## Common commands

```bash
# Start dev server
python manage.py runserver

# Create admin user
python manage.py createsuperuser

# Collect static files (for production)
python manage.py collectstatic
```

## Dependencies

- **Django 6.0** — Web framework

See [requirements.txt](requirements.txt) for pinned versions.

## Deployment

This project ships with a Render Blueprint ([render.yaml](render.yaml)) that provisions a free web service plus a free PostgreSQL database in one click.

### Architecture

| Layer | Local dev | Render |
| --- | --- | --- |
| WSGI server | `runserver` | `gunicorn portfolio.wsgi:application` |
| Static files | Django dev server | WhiteNoise (compressed + manifest) |
| Database | SQLite (`db.sqlite3`) | Managed PostgreSQL |
| Settings | reads `.env` (optional) | reads Render env vars |
| `DEBUG` | `True` | `False` |

### Environment variables

Settings come from environment variables via [python-decouple](https://github.com/HBNetwork/python-decouple). See [.env.example](.env.example) for the full list.

| Variable | Required | Notes |
| --- | --- | --- |
| `SECRET_KEY` | prod | Render auto-generates this when using the Blueprint. |
| `DEBUG` | always | Defaults to `False`. Set to `True` only locally. |
| `ALLOWED_HOSTS` | always | Defaults to `localhost,127.0.0.1,.onrender.com`. |
| `DATABASE_URL` | prod | Auto-injected by Render's Postgres add-on. Falls back to SQLite if unset. |
| `CSRF_TRUSTED_ORIGINS` | optional | Defaults to `https://*.onrender.com`. |
| `WEB_CONCURRENCY` | optional | Number of gunicorn workers. Default 4 in `render.yaml`. |

### Deploy to Render

1. Push this repo to GitHub.
2. In the Render dashboard, click **New → Blueprint** and connect the repo.
3. Render reads [render.yaml](render.yaml), provisions the database, and runs [build.sh](build.sh).
4. First deploy takes ~5 min. Subsequent pushes to `main` redeploy automatically.

### Build pipeline

[build.sh](build.sh) runs on every deploy:

```bash
pip install -r requirements.txt
python manage.py collectstatic --no-input   # WhiteNoise needs this
python manage.py compilemessages            # builds .mo from locale/*/django.po
python manage.py migrate --no-input
```

### Local production-mode smoke test

```bash
DEBUG=False SECRET_KEY=test ALLOWED_HOSTS=localhost,127.0.0.1 \
  python manage.py collectstatic --no-input
DEBUG=False SECRET_KEY=test ALLOWED_HOSTS=localhost,127.0.0.1 \
  gunicorn portfolio.wsgi:application
```

## Notes

- Portrait image lives at `main/static/main/images/portrait.jpg`; replace to customize.
- After editing template strings or `locale/*/django.po`, run `python manage.py compilemessages` and restart the server.
