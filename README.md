# Smart Learning Platform

A full-featured web application built with **Python Django** for structured technology roadmaps.

## Features

- Landing page with hero section and animated progress bars
- User registration and login system
- Dashboard with sidebar navigation
- 6 Technology roadmaps: Python, JavaScript, React, Django, Machine Learning, SQL & Databases
- Each technology has Beginner, Intermediate, and Advanced roadmaps with 50+ topics
- Track your progress topic by topic
- Blue-purple gradient dark theme with Bootstrap 5

---

## Setup Instructions (VS Code / Local)

### Step 1 — Make sure Python 3 is installed

Open a terminal and check:

```
python --version
```

You need Python 3.8 or newer.

---

### Step 2 — Create a virtual environment

```
python -m venv venv
```

Activate it:

- **Windows:**
  ```
  venv\Scripts\activate
  ```
- **Mac / Linux:**
  ```
  source venv/bin/activate
  ```

---

### Step 3 — Install dependencies

```
pip install -r requirements.txt
```

---

### Step 4 — Run database migrations

```
python manage.py migrate
```

---

### Step 5 — Load the technology data (topics, roadmaps)

```
python manage.py seed_data
```

This populates the database with all 6 technologies and their roadmap topics.

---

### Step 6 — Create an admin account (optional)

```
python manage.py createsuperuser
```

Follow the prompts to set username and password.

---

### Step 7 — Start the server

```
python manage.py runserver
```

Open your browser and go to: **http://127.0.0.1:8000/**

---

## Project Structure

```
smart-learning/
├── manage.py                          # Django management tool
├── requirements.txt                   # Python dependencies
├── db.sqlite3                         # SQLite database (auto-created)
│
├── smartlearning/                     # Django project settings
│   ├── settings.py                    # App configuration
│   ├── urls.py                        # Root URL routing
│   ├── wsgi.py
│   ├── static/
│   │   ├── css/style.css              # Blue-purple dark theme styles
│   │   └── js/main.js                 # Progress toggle & animations
│   └── templates/
│       ├── base.html                  # Base HTML template
│       ├── registration/
│       │   ├── login.html
│       │   └── register.html
│       └── learning/
│           ├── landing.html           # Home / landing page
│           ├── dashboard.html         # User dashboard
│           └── technology_detail.html # Roadmap detail view
│
└── learning/                          # Main Django app
    ├── models.py                      # Database models
    ├── views.py                       # Page views
    ├── urls.py                        # App URL patterns
    ├── forms.py                       # Registration form
    ├── admin.py                       # Admin panel config
    ├── signals.py                     # Auto-create UserProfile
    ├── templatetags/
    │   └── landing_tags.py            # Custom template filters
    └── management/commands/
        └── seed_data.py               # Technology data seeder
```

---

## Pages

| URL | Description |
|-----|-------------|
| `/` | Landing page |
| `/register/` | Create account |
| `/login/` | Log in |
| `/dashboard/` | User dashboard (login required) |
| `/technology/<slug>/` | Roadmap for a specific technology |
| `/admin/` | Django admin panel |

---

## Technologies Used

- **Python 3** — Backend language
- **Django 4.2** — Web framework
- **SQLite** — Database (built-in, no setup needed)
- **Bootstrap 5** — CSS framework
- **HTML / CSS / JavaScript** — Frontend
