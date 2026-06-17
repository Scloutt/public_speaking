# Debate Scoring Application

A Django-based debate scoring application built for judges, admins, and event staff.

## Architecture
- Backend: Django 5.x
- Frontend: server-rendered Django templates
- Interactivity: `django-htmx` + `Alpine.js`
- Styling: Bootstrap + custom CSS
- Deployment: Vercel with `@vercel/python`
- Database: PostgreSQL in production, SQLite local/dev fallback

## Quick start
1. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
2. Set local environment variables or create a `.env` file with at least:
   ```bash
   DJANGO_SECRET_KEY=your-local-secret
   DJANGO_DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Production / Vercel
- Ensure `DJANGO_SECRET_KEY`, `DATABASE_URL`, `ALLOWED_HOSTS` are set.
- Set `DJANGO_DEBUG=False`.
- For first deploy, use `DJANGO_AUTO_MIGRATE=True`, then set it to `False`.
- Use PostgreSQL in production.

## Netlify / Vite
- Static assets are built with Vite into `static/dist`.
- Use `npm ci && npm run build` to generate production assets.
- `netlify.toml` is configured to publish `static/dist`.
- Run `npm run dev` locally for Vite development.

## Render deployment
- Add `render.yaml` to the repo so Render can auto-deploy.
- Create a free Render PostgreSQL database and attach it to `DATABASE_URL`.
- Set required environment variables on Render:
  - `DJANGO_SECRET_KEY`
  - `DATABASE_URL`
  - `DJANGO_DEBUG=False`
  - `ALLOWED_HOSTS=<your-render-domain>`
  - `DJANGO_AUTO_MIGRATE=True` for first deploy, then `False`
  - `DJANGO_AUTO_SEED=False`
- Build command: `npm ci && npm run build && pip install -r requirements.txt && python manage.py collectstatic --noinput`
- Start command: `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`

## Project Layout
- `config/` — Django settings and URLs
- `debate/` — core application models, views, templates
- `static/` — custom CSS and static assets
- `templates/` — shared base templates

## Features to build
- Judge login / entry form
- Team management
- Rubric editing
- Class ranking aggregates
- Kiosk mode
- Audit log
- CSV exports
- Offline queue sync endpoint

## Notes
- Static files are served using `whitenoise` in production.
- This scaffold uses a backend-driven Django approach with HTMX support.
