# 🌟 Week 2 – Overview: Development Environment Setup

The development of the *library system* was based on setting up a complete local environment that integrates tools for data management, web application development, and dynamic content delivery. Each technology used in the project fulfills a specific role within the system’s architecture, and their interaction ensures smooth and reliable application functionality.

At the application layer, two different technologies were employed: **Django** (a Python framework) and **PHP**. Django serves as the application layer responsible for request routing, business logic processing, database communication and the generation of dynamic HTML pages through its template system. PHP was also used as an application layer, primarily in combination with Apache, to serve dynamic pages and interact with the MySQL database.

For data management, two database systems were utilized: **MySQL** and **PostgreSQL**. MySQL was used alongside PHP and managed through **phpMyAdmin**, a web-based interface that allows easy viewing, editing, and organization of database content. PostgreSQL served as Django’s primary database, offering stability, strong support for complex queries, and seamless integration with the Django ORM. Its administration was performed through **pgAdmin4**, a graphical tool for monitoring and managing tables, relationships, and stored data.

At the web server level, the Apache HTTP Server was used as the intermediary between the browser and PHP. Apache receives incoming HTTP requests, forwards them to PHP for processing, and returns the final HTML response to the user. This setup provides a stable, production‑like environment for serving PHP applications. In contrast, Django runs through its own development server, which is suitable for development but not intended for production use.

The overall workflow operates as follows: the user sends a request through the browser; if the request targets a Django page, it is processed by Django, which communicates with PostgreSQL and returns the resulting page. If the request targets a PHP page, it is handled by Apache, forwarded to PHP, processed using MySQL and finally returned to the user by Apache. Meanwhile, phpMyAdmin and pgAdmin4 are used to manage their respective databases but do not participate directly in the request–response cycle.

Through this structure, the development environment integrates all essential layers — application, database, and web server — forming a complete and functional architecture for building and managing a library system.

The diagram below illustrates the communication flow between the system’s components and how they work together to handle user requests:

                                                     ┌──────────────────────────┐
                                                     │        Web Browser       │
                                                     └─────────────┬────────────┘
                                                                   │
                                                     ┌─────────────┼────────────┐
                                                     │                          │
                                                     ▼                          ▼
                                        ┌──────────────────────┐     ┌───────────────────────┐
                                        │   Apache HTTP Server │     │  Django Dev Server    │
                                        └─────────────┬────────┘     └─────────────┬─────────┘
                                                      │                              │
                                                      ▼                              ▼
                                        ┌──────────────────────┐        ┌──────────────────────┐
                                        │         PHP          │        │        Django        │
                                        └─────────────┬────────┘        └─────────────┬────────┘
                                                      │                              │
                                                      ▼                              ▼
                                        ┌──────────────────────┐        ┌──────────────────────┐
                                        │        MySQL         │        │     PostgreSQL       │
                                        └─────────────┬────────┘        └─────────────┬────────┘
                                                      │                              │
                                                      ▼                              ▼
                                        ┌──────────────────────┐        ┌──────────────────────┐
                                        │      phpMyAdmin      │        │       pgAdmin4       │
                                        └──────────────────────┘        └──────────────────────┘
                                    


## ⚙️ phpMyAdmin Setup

## 1️⃣ phpMyAdmin Installation ⬇️
### 1. Download phpMyAdmin

Go to the official site: https://www.phpmyadmin.net/downloads/


Download the **All Languages ZIP** version

### 2. Extract Files

Create a folder inside ```htdocs``` named:

```
C:\Apache24\htdocs\phpmyadmin
```

Extract **all ZIP contents** *directly inside it*.

⚠️ Make sure no double folder is created (e.g. phpmyadmin/phpmyadmin).

### 3. Configure phpMyAdmin

Inside the ```phpmyadmin``` folder:

1. Copy ```config.sample.inc.php```
2. Paste → rename to:
```
config.inc.php
```

3. Open it and on **line 16**, add a **random 32-character secret key**:
```
$cfg['blowfish_secret'] = 'your32charactersecretkeyhere';
```
and save.

### 4. Register phpMyAdmin in Apache

Open:
```
C:\Apache24\conf\httpd.conf
```

Scroll to the end and add:
```
Alias /phpmyadmin "C:/Apache24/htdocs/phpmyadmin"
<Directory "C:/Apache24/htdocs/phpmyadmin">
    AllowOverride All
    Require all granted
</Directory>
```

💾 Save the file.

### 5. Set Default Directory Index
Still inside:
```
C:\Apache24\conf
```
Open ```httpd.conf``` and add this line at the very end:
```
DirectoryIndex index.php index.html
```
This ensures Apache loads ```index.php``` first when a folder is accessed.

💾 Save the file.

### 6. Configure PHP Extensions
Navigate to the PHP installation folder:
```
C:\php
```
1. Copy the file ```php.ini-production```
2. Paste and rename the copy to:
```
php.ini
```
3. Open ```php.ini```
4. Press **Ctrl + F** and search for the following extensions:
- extension=mysqli
- extension=pdo_mysql
5. Remove the semicolon ```;``` in front of them so they become:
```
extension=mysqli
extension=pdo_mysql
```
💾 Save the ```php.ini``` file.

### 7. Restart Apache

Open **Command Prompt as Administrator**:
```
cd C:\Apache24\bin
httpd -k restart
```

### 8. Access phpMyAdmin

Open:
```
http://localhost/phpmyadmin
```

If configured correctly, the **login page** will appear.
Enter your **MySQL username and password**.

## 2️⃣ Create a Database in phpMyAdmin 🗄️
### 1. Create New Database

1. Left sidebar → **New**
2. Enter a name
3. Choose collation:
```
utf8mb4_general_ci
```
4. Click **Create**

### 2. Import Data (CSV)

If you have Excel data:

1. Convert Excel file to **.csv**

2. Open phpMyAdmin → select your database

3. Go to **Import**

4. Upload your CSV file

### 💡 Tip: CSV Import Notes

When importing your .csv file into phpMyAdmin:

- Make sure that the **column names in the CSV match exactly** the fields in your database table (same order, same spelling, no extra spaces)
- If the data does not appear correctly aligned after import, change the **Field Separator** from ```,``` to ```;```
- Ensure the file is saved in **UTF-8** encoding to avoid incorrect characters


## 3️⃣ Installing & Setting Up Django 📥
### 1. Verify Python Installation

Open **CMD** and run:
```
python --version
```

- If Python is **not installed**, download and install it from the official website.
- If the command prints a version number, you're good to go ✔️.

### 2. Create a Virtual Environment (Recommended)

In **CMD (Run as Administrator)**, navigate to your desired directory and run:
```
python -m venv venv
```

Activate it:
```
venv\Scripts\activate
```

⚠️ The **v**irtual **env**ironment must be active before installing Django.

### 3. Install Django

Navigate to your working directory:
```
cd C:\Users\...
```

Then install Django:
```
pip install django
```

✅ If installation completes successfully, continue to the next step. 

### 4. Create a New Django Project

Run:
```
django-admin startproject excel_form_app
```

A new folder named ```excel_form_app``` will be created in your current path. Automatically, a file named ```excel_form_app``` will be created, which contains the files: 

- ```settings.py```
- ```urls.py```
- ```wsgi.py```
- ```asgi.py```

Move into the project directory:
```
cd excel_form_app
```

### 5. Run the Development Server

Start the Django server:
```
python manage.py runserver
```

You will receive a local URL such as:
```
http://localhost/
```

Open it in your browser — you should see the **default Django page with the rocket** 🚀

Stop the server anytime with:
```
Ctrl + C
```

The files ```manage.py``` and ```db.sqlite3``` must be located in the root directory created by the user. Keeping them in the initial folder ensures that Django can properly manage the project and database.


### 6. Open the Project in VS Code (optional)

Run:
```
code .
```

This will open **excel_form_app** project in Visual Studio Code for development. 



## 4️⃣ Install & Configure PostgreSQL & pgAdmin4 🔧

### 1. Install PostgreSQL (Windows)

1. Download **PostgreSQL** for *Windows* from the official website: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
2. Run the installer → click **Yes** to all prompts.
3. Leave all default components selected:
   - PostgreSQL Server
   - pgAdmin 4
   - Stack Builder
4. Choose the default installation directory.
5. Set a **password** for the default user ```postgres```.
6. Leave the default **port 5432**.
7. Keep all other settings on default.
8. Click **Next** → **Next** → **Install** → **Finish**.
9. After installation finishes, Stack Builder will appear. Click **Cancel** and close it — not required for now.

#### 🔄 Optional: Verify PostgreSQL Service

You can optionally check that the PostgreSQL service is running:
1. Open **Services** (Start → type Services).
2. Locate **postgresql-x64-18** (or your installed version).
3. Make sure the **Status** is Running.

If it is stopped, right-click → **Start**.

### 2. Open pgAdmin4

Go to **Start** → **pgAdmin 4**.

The program opens in your browser.

In the left panel, expand **Servers** → **PostgreSQL 18**.

Enter the password you set earlier.

### 3. Create a New Database

In the left sidebar, right-click **Databases**.

Select **Create** → **Database**…

Enter a **name** for your database.

Click **Save**.


## 5️⃣ Connecting Django with PostgreSQL 🐘
### 1. Install PostgreSQL Driver

Open the terminal **inside the folder where** ```manage.py``` **exists** and run:
```
pip install psycopg2-binary
```

If the installation completes successfully, continue to the next step.

⚠️ `psycopg2-binary` is a Python library that allows your Python programs to connect and interact with PostgreSQL databases. 



### 2. Database Credentials

Use the following settings (adjust values as needed):

- **Database name**: ```db```
- **User**: ```postgres```
- **Password**: *(the password you set during PostgreSQL installation)*
- **Host**: ```localhost```
- **Port**: ```5432```

### 3. Edit Django Settings (```settings.py```)

Open the file:
```
excel_form_app/settings.py
```

Find the ```DATABASES``` section and replace it with:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db',
        'USER': 'postgres',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Save the file.

⚠️ Note: The database name given by the user in pgAdmin 4 needs to be the same as the one set in the ```settings.py``` code.

### 4. Apply Initial Migrations

In the same terminal:
```
python manage.py migrate
```

If everything is correct, Django will create the necessary tables in PostgreSQL.

### 5. Create a Django App 

Inside the ```Project 1``` folder 🗂️, run:
```
python manage.py startapp main 
```

A new folder named **main** will be created inside your project. The folder contains:

- ```models.py```
- ```views.py```
- ```forms.py```
- ```urls.py```
- ```templates/```

### 6. Register the App in Django

Open ```settings.py``` again and find:
```
INSTALLED_APPS = [
```

Add your new app:
```
'main',
```

Save the file. Now, you should have:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main'
]
```

### 7. Define the Book Model

Open:
```
main/models.py
```

Replace the Python code (```models.py```) shown in the folder ```week-02``` of this repository and save the file. 

⚠️ This specific code refers to the library manuals, covering the needs of the Sparta public library.

### 8. Create and Apply Migrations for the New Model

Run:
```
python manage.py makemigrations
```
```
python manage.py migrate
```

This will create the Book table inside the PostgreSQL database according to your model.

⚠️`makemigrations` and `migrate` must be executed whenever changes are made to the database schema (models), such as adding, removing, or modifying model fields or models.


