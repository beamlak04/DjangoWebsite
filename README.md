# School Website

Simple Django project for a school website with public pages, registration pages, and a member dashboard.

## Features

- Public home, about, and contact pages
- Login and sign-up pages for registration
- Member dashboard under the `member/` route
- SQLite database for local development
- Static assets served from the `static/` directory

## Project Structure

- `main/` - public site pages
- `registration/` - login and sign-up pages
- `clients/` - member dashboard area
- `templates/` - shared top-level templates
- `static/` - CSS, JavaScript, images, and vendor assets
- `school_website/` - Django project configuration

## Requirements

- Python 3
- Django 4.x

## Setup

Create and activate a virtual environment, then install Django:

```bash
pip install django
```

Apply the database migrations:

```bash
python manage.py migrate
```

Create an admin user if you need access to the Django admin:

```bash
python manage.py createsuperuser
```

## Run the Project

Start the development server:

```bash
python manage.py runserver
```

Then open the app in your browser at `http://127.0.0.1:8000/`.

## Available Routes

- `/` - home page
- `/about-us/` - about page
- `/contact-us/` - contact page
- `/sign-up/` - registration page
- `/login/` - login page
- `/member/` - member dashboard
- `/admin/` - Django admin

## Notes

- The project uses SQLite by default through `db.sqlite3`.
- Static files are configured through `STATICFILES_DIRS` in `school_website/settings.py`.