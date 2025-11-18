# Task Manager – Django Web Application

A feature-rich **task management web application** built with **Django**, using server-rendered templates, form-based workflows, and AJAX for real-time task updates.  
Users can register, log in, and manage their tasks with due dates, descriptions, and status tracking.  
The project demonstrates Django fundamentals, form handling, user authentication, CRUD operations, Bootstrap UI components, and jQuery-based asynchronous requests.

---

## ⭐ Features

### 🔐 User Authentication
- User registration (custom `SignUpForm`)
- Login and logout
- Flash messages for feedback
- Logged-in users see **only their own tasks**

---

### 📝 Task Management
- Create new tasks (title, description, due date)
- Edit tasks
- Delete tasks
- View full task details
- Update status (In Progress ↔ Completed)
- Due date validation (cannot be in the past)
- Tasks sorted by due date

---

### ⚡ AJAX / Dynamic UI
- Update task status **without page reload**
- jQuery `.ajax()` → updates `Task.status`
- Task lists refresh dynamically after status change
- Real-time UI updates:
  - Checkbox state  
  - Status label  
  - Completed-task styling (strikethrough)  

---

### 🎨 User Interface
- Built with **Bootstrap 5**
- Clean, responsive layout (`layout.html`)
- Navigation bar with conditional login/logout
- Tabs for **My Tasks** and **Completed**
- Visual status indicators (colors, icons, strikethrough)

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Django (Function-Based Views) |
| Database | SQLite (Django default) |
| Frontend | HTML, Bootstrap 5, jQuery |
| Authentication | Django Auth System |
| AJAX | jQuery |
| Templates | Django Template Language (DTL) |

---

## 📂 Project Structure

task-manager-django/
│
├── task_manager/ # Project settings, URLs, WSGI, ASGI
│
├── tasks/ # Main application
│ ├── models.py # Task model
│ ├── views.py # All task & auth views (FBV)
│ ├── forms.py # TaskForm + SignUpForm with Bootstrap widgets
│ ├── urls.py # App URL routes
│ ├── admin.py # Admin configuration
│ └── templates/tasks/ # HTML templates (Bootstrap + jQuery)
│ ├── home.html
│ ├── add_task.html
│ ├── update_task.html
│ ├── task_detail.html
│ ├── login.html
│ ├── register.html
│ └── layout.html # Layout + navbar + AJAX logic
│
└── requirements.txt


---

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/knikzad/task-manager-django.git
cd task-manager-django

# Create virtual environment
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
Visit the app:
http://127.0.0.1:8000/

## Possible Future Improvements
- Add task categories or tags
- Search & filter functionality
- Pagination for long task lists
- Convert to Django REST Framework API
- Dockerize the project
- Switch to PostgreSQL
- Add unit tests
