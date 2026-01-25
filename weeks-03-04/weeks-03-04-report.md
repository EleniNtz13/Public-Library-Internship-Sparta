# 🌟 Weeks 3 & 4 – Overview: Final Steps to Run the Form

This document outlines the *final steps required to run the form locally*, including database verification, library installation, and launching the Django server. Once these steps are completed, the user can access the form through the browser and begin using the application ✨.

## 🧩 Project Structure 

📋 The project name was changed from ‘excel_form_app’ to ‘Project 1’ for clearer identification and numbering of the projects that will be completed during the internship.

Exact – Based on `Project 1` folder 🗂️:

```
Project 1
│── manage.py
│── requirements.txt
│── urls.py
│── static/main
│        └── autocomplete.js
│
│── excel_form_app/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
|   └── static/main
│        └── autocomplete.js
|
├── main/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
|
├── main/templates
│   ├── incomplete_records.html
│   ├── upload_excel.html
│   ├── upload_result.html
│   ├── upload_success.html
|   └── main/
|       ├── add_person.html
|       ├── duplicates_done.html
|       ├── edit_person.html
|       ├── people.html
|       ├── people_table_rows.html
|       ├── print_range.html
|       └── resolve_duplicates.html
|
├── main/static
|   ├── images/
|       └── books_background.jpg
│
├── templates/
│   ├── base.html
│   ├── home.html
│   └── registration/
|       ├── home.html
│       ├── logged_out.html
│       ├── login.html
│       └── signup.html
```

### 1️⃣ Verify Database Table 🗄️
Open CMD as Admin and run:

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

### 👉🏻🗑️ Delete Imported Data (If Needed)

Inside the same CMD, run:
```
python manage.py shell
```

```
from main.models import Person
Person.objects.all().delete()
exit()
```

This step is useful **after imports** if incorrect data was uploaded.

It should be noted 📝:

| What it is             | Description                                                           | Example                                 |
| ---------------------- | --------------------------------------------------------------------- | --------------------------------------- |
| **Database**           | The space where all data is stored; can contain multiple tables       | `db` in pgAdmin 4                       |
| **Table**              | A unit within the database that holds specific data in rows & columns | `Person`                                |
| **Class in models.py** | Defines a table through the ORM; describes fields & their types       | `class Person(models.Model)`            |
| **Relationship**       | The class → creates a table → inside the database                     | Person → table `person` → database `db` |


### 2️⃣ Install Required Libraries 📦
Required for Excel imports:
```
pip install pandas openpyxl
```

### 3️⃣ Start the Server & Access the Website 🌐
In CMD, run:
```
python manage.py runserver
```
Then open your browser and visit:
```
http://localhost/
```

### 4️⃣ Create Admin User (If Needed) 🔐
If no admin exists yet:
```
python manage.py createsuperuser
```

---

## ⚠️ Important Notes

* 🔒 Intended **only for library staff**
* 🐍 Python & Django must be installed
* 🧪 Virtual environment must be **active**
* 📁 Commands must run from the folder containing `manage.py`
* 🔄 Run `makemigrations` & `migrate` **only when model fields change**


## 🎯 Result

You now have a **complete internal Django system** with:

* 📝 Manual entry forms
* 📊 Excel imports
* 💾 PostgreSQL persistence
* 🔐 Authentication
* 🧹 Controlled data reset

