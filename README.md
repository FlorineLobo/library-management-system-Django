📚 Library Management System (Django + MySQL)

A full-featured **Library Management System** built using **Django**, **Bootstrap**, and **MySQL**.  
This web app allows users to manage books, members, and borrowing activities with ease — including fine tracking, due dates, and borrowing limits.

🚀 Features

✅ Add, edit, and delete **books**  
✅ Register new **users/members**  
✅ Borrow and return books  
✅ Restrict users to a maximum of **3 borrowed books**  
✅ Automatically calculate **fines** (₹10/day after 7 days)  
✅ Display **due dates** and **borrowed/available** status  
✅ Integrated with **MySQL** for persistent storage  
✅ Built with **Django 5.2**, **Bootstrap 5**, and **Python 3.12**

🏗️ Project Structure
library-management-system/
│
├── library_web/
│ ├── library_web/ # Project settings, URLs, WSGI/ASGI config
│ ├── libraryapp/ # Core app (models, views, templates)
│ │ ├── migrations/ # Database migrations
│ │ ├── templates/ # HTML templates (Bootstrap)
│ │ ├── models.py # Database models
│ │ ├── views.py # Business logic
│ │ ├── urls.py # App URL routing
│ │ └── forms.py # Django forms
│ ├── db.sqlite3 # (Old local DB, now replaced with MySQL)
│ ├── manage.py # Django management script
│
├── .venv/ # Virtual environment (ignored in Git)
├── .gitignore
└── README.md

⚙️ Installation & Setup
Follow these steps to run the project locally 👇

1️⃣ Clone the repository
```bash
git clone https://github.com/FlorineLobo/library-management-system-Django.git
cd library-management-system-Django

2️⃣ Create a virtual environment
python -m venv .venv
.venv\Scripts\activate   # On Windows
or
source .venv/bin/activate  # On Mac/Linux

3️⃣ Install dependencies
pip install -r requirements.txt
If you don’t have a requirements.txt, generate one with:
pip freeze > requirements.txt

4️⃣ Configure MySQL in settings.py
Make sure your DATABASES section looks like this:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library_db',
        'USER': 'root',
        'PASSWORD': '',  # your MySQL password (if any)
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
5️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Create a superuser (admin access)
python manage.py createsuperuser

7️⃣ Start the development server
python manage.py runserver

Then open 👉 http://127.0.0.1:8000/
 in your browser.

🧠 Admin Panel

Visit: http://127.0.0.1:8000/admin

Login with your superuser credentials

Manage users, books, and borrowing logs directly from the Django admin interface

📅 Borrowing Policy
Rule	Description
Max Books:	A user can borrow up to 3 books at a time
Borrow Period:	7 days
Fine:	₹10 per day after due date
Return:	Books can be returned anytime before or after due date

🧩 Tech Stack
Component	Technology
Backend	Django 5.2
Frontend	HTML, CSS, Bootstrap 5
Database	MySQL
Language	Python 3.12
Server	Django Development Server

🧑‍💻 Author

👤 Florine Lobo
💼 GitHub Profile : https://github.com/FlorineLobo

📧 Email: florinelobo52@gmail.com

⭐ Show Your Support

If you like this project, please give it a ⭐ on GitHub — it helps a lot! 
Pull requests and feedback are always welcome 🙌
