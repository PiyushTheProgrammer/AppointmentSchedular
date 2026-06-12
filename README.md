# Appointment Management System

A Django-based web application for managing appointments. Users can register, log in, book appointments, and admins can manage all appointments through a dedicated dashboard.

## Project Overview

This is a Django appointment booking system that allows:
- **Regular Users**: Register, login, book appointments, view appointment history, and manage their profile
- **Admin Users**: Manage all appointments, view user appointments, edit/delete appointments, and access the admin panel

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- **Python** (3.8 or higher) - [Download Python](https://www.python.org/downloads/)
- **pip** (Python package manager) - Usually comes with Python
- **Git** (optional, for cloning the repository)

## Installation & Setup

### Step 1: Navigate to Project Directory

Open PowerShell or Command Prompt and navigate to the project directory:

```bash
cd C:\Users\piyus\Desktop\AppointmentProject\AppointmentProject\mysite
```

### Step 2: Create a Virtual Environment

Create a Python virtual environment to isolate project dependencies:

```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

**On Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```bash
venv\Scripts\activate.bat
```

After activation, you should see `(venv)` at the beginning of your terminal prompt.

### Step 4: Install Dependencies

Django should already be installed, but if needed, install all required packages:

```bash
pip install django pillow
```

**Required packages:**
- `django` - Web framework
- `pillow` - For image processing (profile pictures)

## Running the Project on Local System

### Step 1: Apply Migrations

Before running the server, apply all database migrations:

```bash
python manage.py migrate
```

This will create all necessary database tables and ensure the database schema is up to date.

### Step 2: Start the Development Server

Run the development server:

```bash
python manage.py runserver
```

You should see output like:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Step 3: Access the Application

Open your web browser and go to:
- **Home Page**: `http://127.0.0.1:8000/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`

## Creating a Superuser (Admin Account)

A superuser is required to access the Django admin panel and manage the application.

### Step 1: Create Superuser

While the development server is **stopped** (Ctrl+C), run:

```bash
python manage.py createsuperuser
```

### Step 2: Enter Superuser Details

You'll be prompted to enter:
- **Username**: Enter your desired admin username (e.g., `admin`)
- **Email address**: Enter your email (e.g., `admin@example.com`)
- **Password**: Enter a strong password (note: characters won't be visible as you type)
- **Password (again)**: Re-enter your password for confirmation

Example:
```
Username: admin
Email address: admin@example.com
Password: 
Password (again): 
Superuser created successfully.
```

### Step 3: Access Admin Panel

Start the server again:
```bash
python manage.py runserver
```

Go to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

## How to Use the Application

### For Regular Users

1. **Register**: Click "Register" on the home page and fill in your details
2. **Login**: Use your username and password to log in
3. **Dashboard**: View your appointments and profile
4. **Book Appointment**: Schedule a new appointment with date and time
5. **Edit Appointment**: Modify existing appointments
6. **Delete Appointment**: Remove appointments if needed
7. **View Profile**: See and edit your profile information including birthdate and profile picture

### For Admin Users

1. **Admin Dashboard**: After logging in as admin, you'll be redirected to the admin appointments page
2. **View All Appointments**: See all appointments booked by all users
3. **Manage Appointments**: Edit or delete any appointment
4. **Access Django Admin Panel**: Visit `/admin/` to:
   - Manage users and permissions
   - Manage appointment records
   - Manage user profiles
   - View system logs and activity

## Project Structure

```
mysite/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database file
├── clients/                 # Main application folder
│   ├── models.py            # Database models (Appointment, Profile)
│   ├── views.py             # View functions (login, register, dashboard)
│   ├── urls.py              # URL routing
│   ├── forms.py             # Django forms
│   ├── admin.py             # Admin panel configuration
│   ├── signals.py           # Django signals
│   ├── apps.py              # App configuration
│   ├── static/              # Static files
│   │   └── style.css        # Stylesheet
│   ├── templates/           # HTML templates
│   │   └── clients/
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── dashboard.html
│   │       ├── profile.html
│   │       ├── take_appointment.html
│   │       ├── edit_appointment.html
│   │       ├── appointment_history.html
│   │       ├── admin_appointments.html
│   │       └── base.html
│   ├── migrations/          # Database migrations
│   └── tests.py             # Unit tests
├── mysite/                  # Project settings folder
│   ├── settings.py          # Django settings and configuration
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI application
│   └── asgi.py              # ASGI application
└── media/
    └── profile_pics/        # User profile pictures

```

## Database Models

### Appointment Model
- **student** (ForeignKey to User): The user who booked the appointment
- **timestamp** (DateTime): When the appointment was created
- **title** (CharField): Appointment title/name
- **description** (TextField): Appointment description
- **appointment_date** (DateField): Date of the appointment
- **appointment_time** (TimeField): Time of the appointment
- **completed** (BooleanField): Whether the appointment is completed

### Profile Model
- **user** (OneToOneField to User): Associated user account
- **birthdate** (DateField): User's date of birth
- **profile_image** (ImageField): User's profile picture

## Common Commands

```bash
# Apply database migrations
python manage.py migrate

# Create a new migration after model changes
python manage.py makemigrations

# Create a superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver

# Run on a specific port (e.g., 8080)
python manage.py runserver 8080

# Access shell to interact with database
python manage.py shell

# Create a new app
python manage.py startapp appname

# Collect static files (for production)
python manage.py collectstatic
```

## Troubleshooting

### Port Already in Use
If port 8000 is already in use, run on a different port:
```bash
python manage.py runserver 8080
```

### Database Errors
If you encounter database errors, reset migrations:
```bash
# Remove db.sqlite3 file and run migrations fresh
python manage.py migrate
python manage.py createsuperuser
```

### Module Not Found Errors
Make sure your virtual environment is activated and all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Image Upload Not Working
Ensure the `media/profile_pics/` directory exists and has proper permissions.

## Development Tips

1. **Debug Mode**: Currently `DEBUG = True` in settings.py (only for development)
2. **Static Files**: Place CSS/JS in `clients/static/` directory
3. **Templates**: Place HTML templates in `clients/templates/clients/` directory
4. **Database Backups**: Always backup `db.sqlite3` before making major changes

## Future Enhancements

Potential improvements for this project:
- Email notifications for appointments
- Calendar view for appointments
- Appointment reminders
- User roles and permissions system
- Appointment categories/types
- Search and filter appointments
- Appointment feedback/ratings
- SMS notifications

## Support & Documentation

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Models Documentation](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django Views Documentation](https://docs.djangoproject.com/en/stable/topics/http/views/)

## Notes

- This is a development setup. For production deployment, update settings.py security settings
- Change `SECRET_KEY` in settings.py before deploying
- Set `DEBUG = False` in settings.py for production
- Use PostgreSQL or MySQL instead of SQLite for production

---

