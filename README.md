Employee Management Dashboard
Overview
The Employee Management Dashboard is a comprehensive web application built to streamline and optimize employee data management. It provides administrators with tools to manage employee records efficiently and offers employees a personalized interface to view their own information. The dashboard ensures data integrity, security, and ease of access, with features to view and download employee information in various formats.

Features
User Authentication

Secure login functionality for both admin and employees.
Usernames and passwords are securely stored in MySQL.
Admin Dashboard

Access detailed employee information.
Links to view and download employee reports.
Easy navigation with a user-friendly interface.
Employee Dashboard

Personalized view of individual employee details.
Access to specific documents and performance records.
Data Management

Secure storage of employee data in MySQL.
Ability to add, update, and delete employee records efficiently.
PDF Generation

View and download employee details in PDF format from the admin dashboard.
Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Python (Django Framework)
Database: MySQL
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/SupriyaJaiswal43/EmployeeManagementSystem.git
Navigate to the project directory:

bash
Copy code
cd EmployeeManagementSystem
Install required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the MySQL database and update the settings.py with your database credentials.

Apply the migrations:

bash
Copy code
python manage.py migrate
Create a superuser to access the admin dashboard:

bash
Copy code
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Usage
Admin Login: Navigate to /admin to access the admin dashboard, manage employee records, and generate PDF reports.
Employee Login: Employees can log in to view their personalized dashboard.
Contributions
Feel free to fork this repository and submit pull requests if you want to contribute to this project. All contributions are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
If you have any questions or suggestions, feel free to reach out:

GitHub: SupriyaJaiswal43
Email: supriyajswl43@gmail.com
