# 🌟 Weeks 3 and 4 – Overview: Django Forms & Excel Integration

This stage completes the **Django form workflow** by fully integrating **models**, **views**, **templates**, **authentication**, **Excel imports**, and **PostgreSQL**.

## 🧩 Project Structure 

Exact – Based on `excel_form_app` folder 🗂️:

```
Project 1
│── manage.py
│── requirements.txt
│── urls.py
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
│   ├── views.py
│   └── urls.py
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
|       └── book_background.jpg
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


### 2️⃣ Forms Setup 📝

File:

`main/forms.py`

Purpose:

* Defines Django forms
* Connects directly to the `Person` model
* Used for **manual data entry**

Paste the corresponding python code which is available in the `week-03` folder 🗂️.

### 3️⃣ Views Logic 👁️

File:

`main/views.py`

Handles:

* Listing entries (`people.html`)
* Editing records (`edit_person.html`)
* Excel uploads
* Duplicate detection
* Success & result pages


There, paste the corresponding python code which is also available in the `week-03` folder 🗂️.

### 4️⃣ URL Configuration 🔗

App-level URLs:

`main/urls.py`

Paste the corresponding python code which exists in the `week-03` folder 🗂️.


Project-level URLs:

`excel_form_app/urls.py`

Paste the corresponding python code which also exists in the `week-03` folder 🗂️.


Ensure the app URLs are included:
```
path('', include('main.urls'))
```


### 5️⃣ Templates are included 🧩

#### 📂 `templates/`

```
registration/
base.html     # Base layout template
home.html     # Landing page template
```


#### 📂 `templates/registration/`

```
home.html        # Authentication home page
login.html       # Login form template
logged_out.html  # Logout confirmation page
signup.html      # User registration page
```

#### 📂 `main/templates/`

```
main/
people.html          # Alternative or extended listing view
upload_excel.html    # Excel upload form
upload_result.html   # Excel import results page
upload_success.html  # Import success confirmation page
```

#### 📂 `main/templates/main/`

```
people.html           # Displays all stored records
edit_person.html      # Edit record form
duplicates.html       # Duplicate detection page
duplicates_done.html  # Confirmation page for duplicates handling
```

### 6️⃣ Manual Entry Test ✅
In the same CMD, run:
```
python manage.py runserver
```

Open:

```
http://localhost/
```

Verify:

* `people.html` loads
* Entries are saved correctly


### 7️⃣ Install Required Libraries 📦

```
pip install pandas openpyxl
```

Used for Excel (`.xlsx`) imports.


### 8️⃣ Authentication Setup 🔐

```
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
```

Create admin user:

```
python manage.py createsuperuser
```


### 9️⃣ Excel Upload Flow 📊

Implemented in:

```
main/views.py
```

Features:

* Accepts **.xlsx only**
* Uses Pandas
* Maps rows to `Person` model
* Detects duplicates


### 🔟 Import Test 🚀

```
python manage.py runserver
```

Login:

```
http://localhost/login/
```

Verify:

* Login works
* Excel upload succeeds
* Records appear in `people.html`

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

