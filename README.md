# 🎓 Student Management System

A web-based Student Management System developed using **Python and Django**. This application allows users to manage student records, departments, degrees, semesters, and graduation status through a database-driven web interface.

## 📌 Features

- ➕ Add New Students
- 📋 View All Students
- 🔍 View Individual Student Details
- ✏️ Update Student Information
- ❌ Delete Student Records
- 🏢 Department Management
- 🎓 Degree Management
- 📚 Semester Management
- 🖼️ Student Profile Image Upload
- 🎓 Track Student Graduation Status
- 🔐 User Registration and Login
- 🔒 Login-Required Access
- 🛡️ Permission-Based Access Control
- 🗄️ Database Management Using Django ORM

## 🛠️ Technologies Used

- Python
- Django
- Django REST Framework
- Django ORM
- SQLite
- HTML
- CSS
- JavaScript
- Git & GitHub
- Postman

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
- Django REST Framework
- Serializers
- APIView
- GET and POST API Methods

## 📁 Project Structure

```text
school/
│
├── accounts/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   └── views.py
│
├── api/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── students/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── school/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   ├── accounts/
│   │   ├── login.html
│   │   └── register.html
│   ├── 403.html
│   ├── 404.html
│   ├── add_students.html
│   ├── edit_student.html
│   ├── home.html
│   └── students_details.html
│
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── images/
│   └── js/
│
├── media/
│   ├── student_images/
│   └── Default.jpg
│
├── manage.py
├── db.sqlite3
└── README.md
```

## ▶️ How to Run

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Navigate into the project directory:

```bash
cd school
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment (Windows):

```bash
venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install django djangorestframework pillow
```

6. Apply migrations:

```bash
python manage.py migrate
```

7. Start the development server:

```bash
python manage.py runserver
```

8. Open in your browser:

```text
http://127.0.0.1:8000/
```

