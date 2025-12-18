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
Databases → your_db → Schemas → public → Tables
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
File: ```excel_data/forms.py``` 

Defines Django form for manual book entry.

## 3️⃣ Create ```views.py```
File: ```excel_data/views.py``` 
Handles:

- Displaying book form
- Saving data to PostgreSQL
- Rendering success templates
- Uploading Excel files


## 4️⃣ Create ```urls.py```
File: ```excel_data/urls.py``` 
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



















### 2. 🏗 Django Project & App Registration 

The Django project (`myproject`) and a Django application (`main`) are created, verified and registered.

Purpose:
- Enable Django to detect models, templates, and management commands

📁 Code reference:
- `myproject/settings.py` → `INSTALLED_APPS`
- App folder: `main/`

⚠️ **Warning**  
If the app is missing from `INSTALLED_APPS`, models and forms will not work.

---

### 3. 🐘 Database Configuration (PostgreSQL)

Django is configured to use PostgreSQL instead of SQLite.
Connection details such as database name, user, password, host, and port are defined.

Purpose:
- Production-level database support
- Compatibility with bulk data import

📁 Code reference:
- `myproject/settings.py` → `DATABASES`

⚠️ **Warning**  
The database name, user, and password must match exactly the PostgreSQL configuration in pgAdmin.

---

### 4. 📦 Data Model Design

The `Book` model defines the structure of library records.
Each field corresponds **directly** to a column in the Excel file (entry number, author, title, ISBN, etc.).

Purpose:
- Map database fields to real library data
- Match Excel column names

📁 Code reference:
- `main/models.py`

⚠️ **Warning**  
Any modification to the model requires new migrations.


Special care is taken to:
- Allow nullable fields (`null=True`, `blank=True`)
- Support real-world incomplete data
- Ensure compatibility with imported Excel values

---

### 5. 🔄 Database Migration 

After defining the data model, Django migrations are created and applied. Migrations synchronize Django models with PostgreSQL tables. This step generates the actual database table inside PostgreSQL.

Purpose:
- Create database tables
- Ensure schema consistency

📁 Code reference:
- `manage.py`

📁 *Commands executed from project root*:
- `makemigrations`
- `migrate`

⚠️ **Warning**  
Commands must be executed from the directory containing `manage.py`.

---

### 6. 📊 Excel Data Placement 

The Excel file containing book records is placed inside a dedicated folder within the app.  
This keeps data files separated from source code and ensures predictable paths.

📁 Location:
`main/excel_data/data.xlsx`

The column headers of the Excel file **must exactly match** the model field names.

---

### 7. ⚙️📥 Custom Excel Import Command 

A custom Django management command is implemented to import Excel data into PostgreSQL.

Key features:
- Uses Pandas to read Excel files
- Safely converts dates and numeric fields
- Handles empty (NaN) values
- Uses `bulk_create` for performance

This approach is scalable and suitable for large datasets.

📁 *Refer to*:  
- `main/management/commands/import_books.py`

📌 *Execution command*:
python manage.py import_books





---

### 8. 📝 Form Creation for Manual Data Entry 

A Django `ModelForm` is created to allow manual insertion of new books via the web interface.

Benefits:
- Automatic validation
- Minimal code duplication
- Direct connection to the data model

📁 *Refer to*:  
- `main/forms.py`

---

### 9. 👁 Views for Data Display & Submission 

Two main views are implemented:

- **Book List View**: Retrieves and displays all books from the database
- **Add Book View**: Handles form display and submission

These views act as the logical bridge between the database and the templates.

📁 *Refer to*:  
- `main/views.py`

---

### 10. 🌐 URL Routing 

URL routing connects browser requests to the appropriate views.

- Root URL (`/`) → displays the book list
- `/add/` → displays the book entry form

📁 *Refer to*:  
- `main/urls.py`
- `myproject/urls.py`

---

### 11. 🎨 Templates & Presentation 

HTML templates are used to render data dynamically.

- `book_list.html`: Displays all books in a table
- `add_book.html`: Displays the form for adding new records

Templates are stored inside the app to leverage Django’s template discovery system.

📁 *Refer to*:  
- `main/templates/`

---

### 12. ▶️ Application Execution 

The Django development server is started, and the application is accessed through the browser.

Available endpoints:
- `http://localhost:8000/` → Book list
- `http://localhost:8000/add/` → Add new book

📁 *Refer to*:  
- `manage.py`

---

## ✅ Final Outcome 🎉

At the end of this process, the system supports:

- ✔ Structured data storage in PostgreSQL
- ✔ Bulk import of Excel records
- ✔ Dynamic display of library data
- ✔ Manual data entry via forms



1) make sure the table Book exists on pgAdmin4 and it has fields like (entry_number, entry_date, koha_author...) poia einai ta vimata? 2 oi tropoi!
2)  δημιουργία excel_data/forms.py me ton κώδικα που φαινεται στο αντίστοιχο αρχείο του παρόντος φακέλου
3)  δημιουργία excel_data/views.py me ton κώδικα που φαινεται στο αντίστοιχο αρχείο του παρόντος φακέλου
4)  δημιουργία excel_data/urls.py me ton κώδικα που φαινεται στο αντίστοιχο αρχείο του παρόντος φακέλου
5)  δημιουργία templates/excel_data kai ekei mesa 4 arxeia me onoma add_book.html  me ton κώδικα που φαινεται στο αντίστοιχο αρχείο του παρόντος φακέλου kai success.html  me ton κώδικα που φαινεται στο αντίστοιχο αρχείο του παρόντος φακέλου
6)  test python manage.py runserver kai meta http://127.0.0.1:8000/books/add/
7)  egkatastasi vivliothikis pip install pandas openpyxl
8)  ενημερωση views.py με προσθήκη του κώδικα upload, view pou diavazei excel kai gemizei ti forma 
9)  url gia excel upload -> prosthiki sto  excel_data/urls.py to "path('upload-excel/', views.upload_excel, name='upload_excel'),
10)  test python manage.py runserver kai meta http://127.0.0.1:8000/upload-excel/



prosthiki sto views.py tou:
import pandas as pd
import datetime
from dateutil.parser import parse
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def clean_text(value):
    if pd.isna(value):
        return None
    return str(value).strip()



upload_excel:

def upload_excel(request):
    if request.method == "POST" and request.FILES.get('file'):
        df = pd.read_excel(request.FILES['file'])

        # Καθαρισμός ονομάτων στηλών Excel
        df.columns = df.columns.str.strip().str.lower()

        books = []

        for _, row in df.iterrows():

            # entry_date
            entry_date_value = row.get('entry_date')
            if pd.notnull(entry_date_value):
                if hasattr(entry_date_value, 'to_pydatetime'):
                    entry_date_value = entry_date_value.to_pydatetime().date()
                elif isinstance(entry_date_value, str):
                    entry_date_value = parse(entry_date_value).date()
            else:
                entry_date_value = None

            books.append(Book(
                entry_number=clean_text(row.get('entry_number')),
                entry_date=entry_date_value,
                author=clean_text(row.get('author')),
                koha_author=clean_text(row.get('koha_author')),
                title=clean_text(row.get('title')),
                publisher=clean_text(row.get('publisher')),
                edition=clean_text(row.get('edition')),
                publish_year=clean_text(row.get('publish_year')),
                publish_place=clean_text(row.get('publish_place')),
                shape=clean_text(row.get('shape')),
                pages=clean_text(row.get('pages')),
                volume=clean_text(row.get('volume')),
                notes=clean_text(row.get('notes')),
                isbn=clean_text(row.get('isbn')),
                column1=clean_text(row.get('column1')),
                column2=clean_text(row.get('column2')),
            ))

        Book.objects.bulk_create(books)

        return redirect('show_books')

    return render(request, 'main/upload_excel.html')





Notes: 

- πρεπει ΤΟ ΑΡΧΕΊΟ που θα φορτωθεί στον browser να είναι .xlsx
- sto add_book.html sto telos tou kwdika den prepei na iparxei return redirect('show_books') -> einai python
- na diorthoso to publish year sto models na einai char oxi int! "publish_year = models.CharField(max_length=20, null=True, blank=True)"
<img width="892" height="620" alt="image" src="https://github.com/user-attachments/assets/59eb6eaa-c39a-44a6-aa72-8c03b2d2c92a" />
<img width="982" height="503" alt="image" src="https://github.com/user-attachments/assets/28171cea-4efd-4195-a04d-f738da27ff15" />
<img width="987" height="372" alt="image" src="https://github.com/user-attachments/assets/0f23251d-876c-42d3-9e73-5a95052a8201" />
<img width="1012" height="537" alt="image" src="https://github.com/user-attachments/assets/675979b8-fc25-4d9e-adbd-9962dd12f5b0" />
<img width="1047" height="486" alt="image" src="https://github.com/user-attachments/assets/1a954e04-fc9e-4610-9a21-52b16516e50a" />
