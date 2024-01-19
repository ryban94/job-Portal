# College_Job_Portal

# overview

This project is a Python Django-based web application for managing a college job portal. The portal allows students to explore job vacancies, apply for jobs, view training programs, and access various study materials. Faculty members, designated as administrators, have the authority to manage students, faculty, courses, departments, jobs, placed students, and training programs.

# Getting Started

Follow these steps to set up and run the project on your local machine: <br>

# System Requirements

Ensure that your system meets the following requirements to successfully set up and run the College Job Portal:<br>

# Software Requirements

Python: Version 3.6 or higher
Django: Version 3.0 or higher
Database: SQLite (default for Django)

# Installation

Clone this repository to your local machine<br>
#### git clone https://github.com/ryban94/job-Portal.git<br>

Navigate to the project directory.<br>
#### cd CMS

Activate the virtual Environment.<br>
#### myenv\scripts\activate<br>

Install the required dependencies.<br>
#### pip install -r requirements.txt

Apply initial migrations to set up the database:<br>

#### python manage.py makemigrations
#### python manage.py migrate

Configure email settings in the settings.py file to enable the "Forgot Password" feature.<br>

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your_smtp_server'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_email_password'

Run the server.<br>

#### python manage.py runserver<br>
###### The server will be running at http://127.0.0.1:8000/.

# Admin Credentials

Username: 4
Password: 9876543210

# User Authentication

Only administrators can create accounts for students and faculty.
Users can log in using their user ID and mobile number.
Users can reset their password using the "Forgot Password" feature, which involves receiving an OTP via email.<br>

# Admin Authority

Admin faculty members have the authority to add, modify, and delete students, faculty, courses, departments, jobs, placed students, and training programs.<br>

# Navigation
    Home Page Navbar:

        Home
        Recruiters
        Contact Us
        Gallary
        Help
        Job Vacancy List
        Training Program List
    
    Home Page Body:

        View Jobs List
        Placed Student List
        Study Programs
        Aptitude, etc.
        View Training Programs

# Job Application Process
    Students can apply for jobs.
    Students can upload their resumes during the application.
    Once a student applies for a job, they cannot apply for the same job again.
    Faculty can view the resumes of students who have applied under their respective companies.
    Feel free to explore the features and functionalities of the College Job Portal! If you have any questions or issues, please refer to the help section or contact us.
