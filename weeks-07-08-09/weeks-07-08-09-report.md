# 🌟 Weeks 7, 8 & 9 – Overview: Laravel Setup and Development of a Protocol Management System
The next project implemented during my internship at the library concerned the development of a **Protocol Management System**. After setting up a development environment on *Windows* by installing *PHP* and *MySQL* manually (without using WAMP or XAMPP) and configuring *Apache*, the following section outlines the initial steps required to install *Laravel*.

**Laravel** is a modern, open-source PHP web application framework designed to simplify and accelerate web development. It follows the MVC (Model–View–Controller) architectural pattern and provides elegant syntax, built-in tools, and robust features such as routing, authentication, database migrations, and security mechanisms. Its goal is to make development both efficient and maintainable while promoting clean, structured code.

Below are the first steps for installing Laravel on a Windows environment.

## ✅ Laravel Installation Steps

### 1️⃣ Open Command Prompt

Open Command Prompt (preferably as Administrator) and check PHP version:
```
php -v
```

### 2️⃣ Enable Required PHP Extensions ⚙️

Make sure the following extensions are enabled in php.ini:
```
- curl
- fileinfo
- mbstring
- mysqli
- openssl
- pdo_mysql
- pdo_sqlite
- zip
```

Open the php.ini file:
```
C:\php\php.ini
```

Find one of the following lines:
```
;extension=zip
```
or
```
;extension=php_zip.dll
```
Remove the semicolon (;), so it becomes:
```
extension=zip
```
or
```
extension=php_zip.dll
```
Save the file and restart Apache 🔄

### 3️⃣ Verify ZIP Extension 📦

Run:
```
php -m | findstr zip
```
If you see:
```zip```
→ ✅ OK

Run:
```
php -m
```
Ensure that at least the following extensions are visible:
```
curl
mbstring
openssl
pdo_mysql
zip
fileinfo
```
If any are missing, enable them from ```php.ini```


### 4️⃣ Composer Installation

Check if Composer is installed:
```
composer -v
```
If not installed, download it from:
https://getcomposer.org/Composer-Setup.exe

During installation:
- When asked for PHP path, select:

  ```
  C:\php\php.exe
  ```
- Leave all options as default

After installation:

Open a new CMD window and verify:
```
composer -V
```

### 5️⃣ Create Laravel Project

Navigate to your projects directory:
```
cd C:\Apache24\htdocs
```

Create the Laravel project:
```
composer create-project laravel/laravel protocol_project
```

📌 Note:
"protocol_project" is the project name and can be changed.

Wait 1–2 minutes for installation to complete ⏳


============================================================
⚠️ Composer Proxy Issue (Common Problem)
============================================================

Sometimes Composer detects broken proxy settings and freezes.

✅ Guaranteed Fix:

Open Command Prompt (NOT PowerShell) and run EXACTLY:

composer config --global --unset http-proxy
composer config --global --unset https-proxy


============================================================
🔍 Check extension_dir
============================================================

In php.ini, ensure the following line exists:
extension_dir="C:\php\ext"

Save the file, restart Apache,
close all CMD windows, and open a new CMD.


============================================================
🧹 Clear Composer Cache
============================================================

Run:
composer clear-cache


============================================================
🗄️ Database Configuration (.env)
============================================================

Open the .env file located at:
C:\Apache24\htdocs\laravelapp\.env

Open it using Notepad, VS Code, or any editor.
Be careful not to change unrelated settings.


============================================================
Update Database Settings
============================================================

Default configuration:
DB_CONNECTION=sqlite
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=database/database.sqlite
DB_USERNAME=root
DB_PASSWORD=

Change to MySQL configuration:
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=laravel
DB_USERNAME=root
DB_PASSWORD=your_mysql_password

Notes:
- DB_DATABASE: name of the MySQL database
- DB_USERNAME: usually root
- DB_PASSWORD: MySQL root password


============================================================
🚀 Run Laravel Commands
============================================================

Generate application key:
php artisan key:generate

Run database migrations:
php artisan migrate

Start Laravel development server:
php artisan serve


============================================================
🌐 Browser Test
============================================================

Open your browser and navigate to:
http://127.0.0.1:8000

If everything is correct, the Laravel welcome page will appear 🎉


============================================================
🧹 Clear Laravel Cache (If Needed)
============================================================

Sometimes Laravel keeps old configuration values.

Run:
php artisan config:clear
php artisan cache:clear
php artisan route:clear

Then restart the server:
php artisan serve


============================================================
🌐 Final Result
============================================================

The Laravel application is now fully installed, configured,
and running successfully 🚀✅
