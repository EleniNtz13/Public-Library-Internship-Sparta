# 🌟 Weeks 5 & 6 – Overview: The final version of the online form

### 🗓️ Weeks Overview: Form Development

These weeks were dedicated to the **design**, **implementation**, and **completion** of the web-based data entry form.
Below are the steps, structure, and functionality developed during this phase, including form handling, data validation, database integration, and user access control:

1️⃣ Initial display of the **home page** 🏠 (the same view is shown when the user is logged out):
<img width="1917" height="1027" alt="Στιγμιότυπο οθόνης 2026-01-09 180250" src="https://github.com/user-attachments/assets/1720fca3-0d69-4464-927c-a01eb985b7fa" />

2️⃣ If you don't have an account 🔐, then you should **sign up**:
<img width="1920" height="1027" alt="Στιγμιότυπο οθόνης 2026-01-09 180639" src="https://github.com/user-attachments/assets/6208a993-a929-4e80-ac99-d306ca3c26a6" />

3️⃣ Otherwise, you can **login** 🔓: 
<img width="1920" height="1027" alt="Στιγμιότυπο οθόνης 2026-01-09 180823" src="https://github.com/user-attachments/assets/a8732640-4d5b-4a8c-99a6-a8828fd597d9" />

4️⃣ Now, you are **signed in** 🥳:
<img width="1920" height="1027" alt="Στιγμιότυπο οθόνης 2026-01-09 181450" src="https://github.com/user-attachments/assets/9b569d7a-76e8-40a2-b48f-38f1ddcf091e" />

5️⃣ Then, you can **upload** an `.xlsx` file 📥:
<img width="1920" height="1027" alt="Στιγμιότυπο οθόνης 2026-01-09 181610" src="https://github.com/user-attachments/assets/dd9a933c-e85c-4133-80cc-7a09188826a3" />

6️⃣ If these **entries have not been submitted before**, the form is displayed to the user like this:
<img width="1920" height="1027" alt="Στιγμιότυπο οθόνης 2026-01-09 183443" src="https://github.com/user-attachments/assets/ca4f0e12-4f7d-4755-981a-079907ed5461" />

7️⃣ Otherwise, if these **entries have been submitted before**, the form is displayed as follows:
<img width="1917" height="1026" alt="Στιγμιότυπο οθόνης 2026-01-09 182317" src="https://github.com/user-attachments/assets/056264b0-2f12-4833-b0fc-96b68a2a6b80" />

8️⃣ Additionally, library staff can **enter a book’s details directly into the form**, avoiding the need to import Excel files: 
<img width="1920" height="1027" alt="Στιγμιότυπο οθόνης 2026-01-09 192034" src="https://github.com/user-attachments/assets/6c70fc11-afc2-4e8d-9d52-8c0620481dc4" />
After all, this is the main purpose of the form — to have all the library’s books and their data consolidated in one place.

9️⃣ You can also view **all records**, search by a **selected field** (entry number, date, author, title, publisher, ISBN), and **print** any specific range of records the user chooses:
<img width="1920" height="972" alt="Στιγμιότυπο οθόνης 2026-01-25 182214" src="https://github.com/user-attachments/assets/8deb3d4c-6d02-4773-b9ce-75825a100343" />

🔟 The user is able to **edit** any record they choose as shown below:
<img width="1920" height="1027" alt="Στιγμιότυπο οθόνης 2026-01-25 184253" src="https://github.com/user-attachments/assets/99023783-05ab-4bb9-acdf-17dc121e9eaa" />

⏸️ Finally, the records **printing page** is as follows:
<img width="1920" height="1030" alt="Στιγμιότυπο οθόνης 2026-01-25 183403" src="https://github.com/user-attachments/assets/18d148b4-3dcc-4365-a70a-24bc7c9c34fd" />

⚠️ Record details are not shown in order to protect the library’s data.
<!-- And check **duplicates** here:```http://localhost/duplicates/``` -->

🔒 For confidentiality reasons, screenshots of the last two URLs are omitted, since they would reveal the library’s data.

### 📋 Important Notes

- 🏤 The application is designed exclusively for **internal library staff**, ensuring safe and controlled management of catalog records
- 🔒 For privacy and security, the screenshot does not display the *localhost URLs*. They can be accessed locally when running the app
- ⚠️ User-facing messages are displayed in *Greek*, for clarity and usability within the library working environment
- 🔢 Entries are imported sequentially and will be sorted correctly even if their input order is mixed
- 🧠 In the case of direct book data entry into the database, if the Koha author field is not provided, it is automatically populated using the main author’s name
- 🖨️ The print functionality allows staff to generate printable views of specific books by entry number, supporting internal documentation and catalog verification
- 📱 The interface is responsive and can be used on mobile devices, although it is optimized primarily for desktop use by staff


### 🧾 Form Completion & Functionality

By the end of the internship, the system supports:

- 📝 Manual data entry via Django forms
- 📊 Bulk data import from Excel files
- 💾 Persistent storage in PostgreSQL
- 🛠️ Duplicate detection and resolution
- ✏️ Editing and deletion of records
- 🔐 Authentication & restricted access
- 📱 Responsive layout, usable on mobile devices

✏️ The form has been developed in Greek due to operational requirements and to ensure consistency with the library’s internal workflow.

❗ The entire project is located in the repository named **excel_form_app**. However, for privacy reasons, the repository has been set to private.

🚀 Ready for internal library use!

