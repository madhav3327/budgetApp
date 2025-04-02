# 🧾 BudgetApp – Shared Expense Tracker for Roommates

A stylish and easy-to-use web app built with **Django** that helps roommates manage shared expenses efficiently. This project was designed for 4 members living together, but can be easily extended to more.

---

## Features

- Entrance Access – Only users with a special access code (`*****`) can use the app.
- User Management – Separate login for existing users and registration for new users using name + PIN.
- Expense Logging – Users can log purchases with:
  - Location (auto-filled from last entry)
  - Product name
  - Quantity
  - Price
- Multi-product support at the same location (optional via future enhancement)
- CSV Export – All user info and expense logs are saved to `.csv` files for later analysis.
- Modern UI – Uses a **blurred background**, **glassmorphism UI**, and clean form layouts.
  
---

##  Project Structure


budget_tracker/
│
├── expenses/                   # Main Django app
│   ├── models.py               # UserProfile & Expense models
│   ├── views.py                # Views for login, registration, expense logging
│   ├── forms.py                # Custom forms for each step
│   ├── templates/expenses/     # HTML templates
│
├── staticfiles/               # Local static folder for images
│   ├── background.jpg
│   ├── login.jpg
│
├── data/
│   ├── users.csv              # Stores registered users (name, PIN)
│   ├── expenses.csv           # Stores all expense data
│
├── manage.py
└── README.md



How It Works

Step 1: Entrance Code

Users must enter a valid entrance code (1926) to proceed.

Step 2: Login or Register
	•	Existing users log in using name and PIN.
	•	New users register with name, PIN, and confirmation. Data is saved to users.csv.

Step 3: Add Expenses

Once logged in:
	•	A form is shown to add product, quantity, price, and location.
	•	Location is auto-filled based on the user’s last entry.
	•	All entries are saved to expenses.csv with user name and timestamp.

Step 4: View History

Below the form, users can see their past entries with full details.

⸻
