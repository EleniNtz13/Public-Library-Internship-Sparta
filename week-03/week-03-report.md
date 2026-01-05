# 🌟 Week 3 – Django Forms & Excel Integration

## 🧭 Overview

This stage completes the **Django form workflow** by fully integrating **models, views, templates, authentication, Excel imports, and PostgreSQL**.
The application is designed **exclusively for internal library staff** to manage records safely and efficiently.

---

## 🗂️ Project Structure (Exact – Based on `excel_form_app`)

```
excel_form_app/
│── manage.py
│── excel_form_app/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── main/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│       └── __init__.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   └── registration/
|       ├── home.html
│       ├── login.html
│       ├── logged_out.html
│       └── signup.html
│
└── main/templates
|   └── main/
        ├── people.html
        ├── edit_person.html
        ├── duplicates.html
        └── duplicates_done.html
|   ├── people.html
│   ├── upload_excel.html
│   ├── upload_result.html
│   ├── upload_success.html
```



✅ **Note:**

* `people.html` **is required** and is the **main listing page** for all stored entries.
* There is **no unused or optional `people.html`** — it is a core template.

---

## 1️⃣ Verify Database Table

```
python manage.py shell
```

```
from main.models import Person
Person.objects.all()
```

If no errors appear, the model and table exist.

Inspect fields:

```
for field in Person._meta.fields:
    print(field.name, field.get_internal_type())
```

---

## 2️⃣ Forms Setup 📝

File:

```
main/forms.py
```

Purpose:

* Defines Django forms
* Connects directly to the `Person` model
* Used for **manual data entry**

---

## 3️⃣ Views Logic 👁️

File:

```
main/views.py
```

Handles:

* Listing entries (`people.html`)
* Editing records (`edit_person.html`)
* Excel uploads
* Duplicate detection
* Success & result pages

---

## 4️⃣ URL Configuration 🔗

App-level URLs:

```
main/urls.py
```

Project-level URLs:

```
excel_form_app/urls.py
```

Ensure the app URLs are included:

```
path('', include('main.urls'))
```

---

## 5️⃣ Templates 🧩

### 📂 `main/templates/main/`

```
people.html           # List all records
edit_person.html      # Edit entry
duplicates.html       # Show duplicates
duplicates_done.html  # Duplicates resolved
```

### 📂 `templates/`

```
base.html
home.html
upload_excel.html
upload_result.html
upload_success.html
```

### 📂 `templates/registration/`

```
login.html
logged_out.html
signup.html
```

---

## 6️⃣ Manual Entry Test ✅

```
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

Verify:

* `people.html` loads
* Entries are saved correctly

---

## 7️⃣ Install Required Libraries 📦

```
pip install pandas openpyxl
```

Used for Excel (`.xlsx`) imports.

---

## 8️⃣ Authentication Setup 🔐

```
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
```

Create admin user:

```
python manage.py createsuperuser
```

---

## 9️⃣ Excel Upload Flow 📊

Implemented in:

```
main/views.py
```

Features:

* Accepts **.xlsx only**
* Uses Pandas
* Maps rows to `Person` model
* Detects duplicates

---

## 🔟 Import Test 🚀

```
python manage.py runserver
```

Login:

```
http://127.0.0.1:8000/login/
```

Verify:

* Login works
* Excel upload succeeds
* Records appear in `people.html`

---

## 🧹 Delete Imported Data (If Needed)

⚠️ **Use only if a reset is required**

```
python manage.py shell
```

```
from main.models import Person
Person.objects.all().delete()
exit()
```

This step is useful **after imports** if incorrect data was uploaded.

---

## ⚠️ Important Notes

* 🔒 Intended **only for library staff**
* 🐍 Python & Django must be installed
* 🧪 Virtual environment must be **active**
* 📁 Commands must run from the folder containing `manage.py`
* 🔄 Run `makemigrations` & `migrate` **only when model fields change**

---

## 🎯 Result

You now have a **complete internal Django system** with:

* 📝 Manual entry forms
* 📊 Excel imports
* 💾 PostgreSQL persistence
* 🔐 Authentication
* 🧹 Controlled data reset

🚀 Ready for internal library use.










# 🌟 Week 3 – Library Management System
This week focuses on completing the **full integration between Django forms, views, and the PostgreSQL database**. The system now supports **data persistence**, **Excel imports**, and **web-based data management**.

## 🧭 Overview
During Week 3, the application transitions from initial setup to a **fully functional backend system** by:

- 📐 Defining database models
- 💾 Persisting data in PostgreSQL
- 📊 Importing Excel data into the database
- 📝 Connecting Django forms to models
- 🌐 Displaying stored data using views and templates

## ✨ Features
- 📚 Book model integration with PostgreSQL
- 📝 Manual book entry using Django forms
- 📊 Excel (.xlsx) upload and import
- 🛠️ Database verification via Django Shell & pgAdmin
- 📦 Pandas & OpenPyXL support

---

## 1️⃣ Verify Database Table
###  Option A: Django Shell
```
python manage.py shell
```
```
from excel_data.models import Book
Book.objects.all()
```

✅ If no error occurs, the model and table exist.

Inspect fields:
```
for field in Book._meta.fields:
    print(field.name, field.get_internal_type())
```

###  Option B: pgAdmin 4
1. Open **pgAdmin 4**

2. Navigate:
```
Databases → db → Schemas → public → Tables
```
3. Confirm table ```excel_data_book``` exists

4. Verify fields: ```entry_number```, ```entry_date```, ```koha_author```, ```publish_year```

⚠️ Fix:
```
publish_year = models.CharField(max_length=20, null=True, blank=True)
```

Must be ```CharField```, not integer.

Run migrations if missing:
```
python manage.py makemigrations
python manage.py migrate
```

## 2️⃣ Create ```forms.py```
File: ```main/forms.py``` 

Defines Django form for manual book entry.

## 3️⃣ Create ```views.py```
File: ```main/views.py``` 
Handles:

- Displaying book form
- Saving data to PostgreSQL
- Rendering success templates
- Uploading Excel files


## 4️⃣ Create ```urls.py```
File: ```main/urls.py``` 
⚠️ Ensure included in project-level ```urls.py``` using ```include()```.


5️⃣ Templates 🧩
Directory:
```
templates/
└── excel_data/
    ├── book_list.html
    ├── add_book.html
    ├── upload_excel.html
    ├── success.html
    ├── upload_result.html
    └── login.html
```


- 📄 ```add_book.html``` → Add book form (CSRF protected)
- 📄 ```book_list.html``` → Display stored books
- 📄 ```upload_excel.html``` → Excel upload form
- 📄 ```success.html``` → Success message
- 📄 ```upload_result.html``` → Upload results
- 📄 ```login.html``` → User login page


## 6️⃣ Manual Entry Test ✅
1. Run server:
```
python manage.py runserver
```

2. Open:
```
http://127.0.0.1:8000/books/add/
```
3. Verify form loads and saves data.

## 7️⃣ Install Libraries 📦
```
pip install pandas openpyxl
```

## 8️⃣ Configure Authentication 🔐
In ```settings.py```:
```
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/upload-excel/'
LOGOUT_REDIRECT_URL = '/login/'
```

⚠️ Note: After login, the user is redirected directly to the Excel upload page (```/upload-excel/```).

Ensure ```INSTALLED_APPS``` and ```MIDDLEWARE``` include required Django defaults.

## 9️⃣ Authentication Views
In ```urls.py```:
```
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
```
Create ```templates/main/login.html```. 
Create superuser:
```
python manage.py createsuperuser
```

## 🔟 Excel Upload Logic 📊
Update ```views.py```:

- Add upload_excel view
- Read .xlsx files with Pandas
- Map rows to Book model

⚠️ Restrict file type:
```
if not file.name.endswith('.xlsx'):
    messages.error(request, 'Only .xlsx files are allowed')
```

## 1️⃣1️⃣ Excel Upload URL 🔗
In ```excel_data/urls.py```:
```
path('upload-excel/', views.upload_excel, name='upload_excel'),
```

## 1️⃣2️⃣ Final Test – Excel Upload 🚀
Run server:
```
python manage.py runserver
```
Open:
```
http://127.0.0.1:8000/login/
```
➡️ After login, user is redirected to:
```
http://127.0.0.1:8000/upload-excel/
```
Verify:

- Login works
- Upload form loads
- ```.xlsx``` accepted
- Records imported into PostgreSQL

---

## ✅ Key Notes
- 📌 Only ```.xlsx``` files supported
- 📌 Templates contain HTML only
- 📌 Run migrations after any model change
- 📌 Confirm app URLs are registered at project level
- 📌 Login redirects directly to Excel upload page

## 🎯 Result
You now have a complete Django backend that supports:
- 📝 Manual book entry via forms
- 📊 Excel-based bulk data import
- 💾 PostgreSQL-backed data persistence
- 🔐 Secure login flow → redirect to Excel upload

🚀 Happy coding!





python manage.py shell




from main.models import Person
Person.objects.all().delete()

exit()



