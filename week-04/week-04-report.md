<img width="1920" height="1027" alt="Στιγμιότυπο οθόνης 2026-01-09 180823" src="https://github.com/user-attachments/assets/e8a7be8e-5fb6-4c2a-937e-8f920a2072b3" /># 🌟 Week 4 – Overview: The final version of the online form

### 🗓️ Week Overview – Form Development

This week was dedicated to the **design**, **implementation**, and **completion** of the web-based data entry form.
Below are the steps, structure, and functionality developed during this phase, including form handling, data validation, database integration, and user access control.

1️⃣ Initial display of the home page 🏠︎ (the same view is shown when the user is logged out):
<img width="1917" height="1027" alt="Στιγμιότυπο οθόνης 2026-01-09 180250" src="https://github.com/user-attachments/assets/1720fca3-0d69-4464-927c-a01eb985b7fa" />

2️⃣ If you don't have an account 🔐, then you should sign up:
<img width="1920" height="1027" alt="Στιγμιότυπο οθόνης 2026-01-09 180639" src="https://github.com/user-attachments/assets/6208a993-a929-4e80-ac99-d306ca3c26a6" />

3️⃣ Otherwise, you can login 🔓: 
<img width="1920" height="1027" alt="Στιγμιότυπο οθόνης 2026-01-09 180823" src="https://github.com/user-attachments/assets/a8732640-4d5b-4a8c-99a6-a8828fd597d9" />

4️⃣ Now, you are signed in 🥳:
<img width="1920" height="1027" alt="Στιγμιότυπο οθόνης 2026-01-09 181450" src="https://github.com/user-attachments/assets/083b9729-06a3-4e2b-93a1-422048ac007f" />

5️⃣ Then, you can upload an `.xlsx` file 📥:
<img width="1920" height="1027" alt="Στιγμιότυπο οθόνης 2026-01-09 181610" src="https://github.com/user-attachments/assets/dd9a933c-e85c-4133-80cc-7a09188826a3" />

6️⃣ If these entries have not been submitted before, the form is displayed to the user like this:
<img width="1920" height="1028" alt="image" src="https://github.com/user-attachments/assets/fb632528-7e89-45cf-8a58-ef2eb2c2a6f7" />
7️⃣ Otherwise, it is displayed as follows:
<img width="1916" height="1030" alt="image" src="https://github.com/user-attachments/assets/4ece83f1-1a46-402f-bdac-5001ff433508" />

🔔 Finally, all entries are visible in:
```
http://localhost/people/
```

### 🧾 Form Completion & Functionality

By the end of the internship, the system supports:

- 📝 Manual data entry via Django forms
- 📊 Bulk data import from Excel files
- 💾 Persistent storage in PostgreSQL
- 🛠️ Duplicate detection and resolution
- ✏️ Editing and deletion of records
- 🔐 Authentication & restricted access
- 📱 Responsive layout, usable on mobile devices

### 🔒 Important Notes

- 🏤 The application is designed exclusively for internal library staff, ensuring safe and controlled management of catalog records
- ⚠️ User-facing messages are displayed in Greek, for clarity and usability within the library working environment
- 🧠 If the Koha author field is not provided, it is automatically populated using the main author name
- 📱 The interface is responsive and can be used on mobile devices, although it is optimized primarily for desktop use by staff
- 🖨️ The print functionality allows staff to generate printable views of specific books by entry number, supporting internal documentation and catalog verification


