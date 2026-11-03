# 🎓 Student Management System

A web-based Student Management System developed using **Python and Django**. This application provides an organized way to manage student records, academic information, departments, and degrees through a database-driven web interface.

## 📌 Features

- ➕ Add New Students
- 📋 View All Students
- 🔍 View Individual Student Details
- ✏️ Update Student Information
- ❌ Delete Student Records
- 🏢 Department Management
- 🎓 Degree Management
- 📚 Semester Management
- 🎓 Track Student Graduation Status
- 🔐 User Registration and Login
- 🔒 Login-Required Access
- 🛡️ Permission-Based Access Control
- 🗄️ Database Management Using Django ORM

## 🛠️ Technologies Used

- Python 3
- Django
- Django ORM
- SQLite
- PostgreSQL (if configured)
- HTML
- CSS
- Bootstrap (if used)
- Git & GitHub

## ⚙️ Django Concepts Implemented

- Model-View-Template (MVT) Architecture
- Django Models and Relationships
- Foreign Key Relationships
- Database Migrations
- Django ORM
- Function-Based Views (FBV)
- Class-Based Views (CBV)
- Django ModelForms
- CRUD Operations
- User Authentication
- LoginRequiredMixin
- PermissionRequiredMixin
- Django Admin Panel

## 📁 Project Structure

```text
school/
│
├── school/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── students/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── templates/
├── static/
├── media/
├── manage.py
└── README.md
```

## ▶️ How to Run

1. Clone the repository.
2. Navigate to the project directory.
3. Create and activate a virtual environment.
4. Install Django.
5. Apply database migrations.
6. Start the development server.

```bash
pip install django
python manage.py migrate
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```


⭐ Feedback and contributions are welcome!
