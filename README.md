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

## Notes

- This is a development setup. For production, use Gunicorn or similar and set `DEBUG = False`, a proper `SECRET_KEY`, and `ALLOWED_HOSTS` in [portfolio/settings.py](portfolio/settings.py).
- Portrait image lives at `main/static/main/images/portrait.jpg`; replace to customize.
