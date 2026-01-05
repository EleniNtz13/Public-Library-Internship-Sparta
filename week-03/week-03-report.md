# 🌟 Week 3 – Django Forms & Excel Integration

## 🧭 Overview

This stage completes the **Django form workflow** by fully integrating **models, views, templates, authentication, Excel imports, and PostgreSQL**.
The application is designed **exclusively for internal library staff** to manage records safely and efficiently.

---

## 🗂️ Project Structure (Exact – Based on `excel_form_app`)

```
excel_form_app/
│── manage.py
│── urls.py
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
├── main/templates
|   ├── people.html
│   ├── upload_excel.html
│   ├── upload_result.html
│   ├── upload_success.html
|   └── main/
|       ├── people.html
|       ├── edit_person.html
|       ├── duplicates.html
|       └── duplicates_done.html

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

#### 👉🏻🗑️ Delete Imported Data (If Needed)

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


### 2️⃣ Forms Setup 📝

File:

`main/forms.py`

Purpose:

* Defines Django forms
* Connects directly to the `Person` model
* Used for **manual data entry**

Paste the corresponding python code which is available in the week-03 folder 🗂️.

### 3️⃣ Views Logic 👁️

File:

`main/views.py`

Handles:

* Listing entries (`people.html`)
* Editing records (`edit_person.html`)
* Excel uploads
* Duplicate detection
* Success & result pages


There, paste the corresponding python code which is also available in the week-03 folder 🗂️.

### 4️⃣ URL Configuration 🔗

App-level URLs:

`main/urls.py`

Paste the corresponding python code which exists in the week-03 folder 🗂️.


Project-level URLs:

`excel_form_app/urls.py`

Paste the corresponding python code which also exists in the week-03 folder 🗂️.


Ensure the app URLs are included:
```
path('', include('main.urls'))
```


### 5️⃣ Templates are included 🧩

#### 📂 `templates/`

```
registration/
base.html
home.html
```


#### 📂 `templates/registration/`

```
home.html
login.html
logged_out.html
signup.html
```

#### 📂 `main/templates/main/`

```
people.html           # List all records
edit_person.html      # Edit entry
duplicates.html       # Show duplicates
duplicates_done.html  # Duplicates resolved
```

#### 📂 `main/templates/`

```
main/
people.html
upload_excel.html
upload_result.html
upload_success.html
```


### 6️⃣ Manual Entry Test ✅
In the same CMD, run:
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
http://127.0.0.1:8000/login/
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

🚀 Ready for internal library use.

---

**✨ The final version of the online form:**

Initial display of the home page 🏠︎ (the same view is shown when the user is logged out):
<img width="1920" height="1027" alt="image" src="https://github.com/user-attachments/assets/35fb8c22-37ac-473c-8965-fa0283caab55" />
If you don't have an account 🔐, then you should sign up:
<img width="1920" height="1027" alt="image" src="https://github.com/user-attachments/assets/00825dec-0c8f-4011-8dee-4e6275f5be50" />
Otherwise, you can login 🔓: 
<img width="1920" height="1028" alt="image" src="https://github.com/user-attachments/assets/24dd6764-3967-4c46-b1cf-6e7f7c9e58f4" />
Now, you are signed in 🥳:
<img width="1920" height="1027" alt="image" src="https://github.com/user-attachments/assets/854f68ec-1bdb-4845-9bca-65c78342aa7b" />
Then, you can upload an .xlsx file 📥:
<img width="1918" height="1027" alt="image" src="https://github.com/user-attachments/assets/e493f25e-af47-4ca8-8abe-ecf2278d8424" />
If these entries have not been submitted before, the form is displayed to the user like this:
<img width="1920" height="1028" alt="image" src="https://github.com/user-attachments/assets/fb632528-7e89-45cf-8a58-ef2eb2c2a6f7" />
Otherwise, it is displayed as follows:
<img width="1916" height="1030" alt="image" src="https://github.com/user-attachments/assets/4ece83f1-1a46-402f-bdac-5001ff433508" />
Finally, all entries are visible in:
```
http://127.0.0.1:8000/people/
```

⚠️ User-facing messages are displayed in Greek for clarity and usability reasons.
