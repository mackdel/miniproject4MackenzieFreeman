### INF601 - Advanced Programming in Python
### Mackenzie Freeman
### Mini Project 4


# MiniProject4 - Mini Handbook

## Description

A handbook web app allowing users to view and request clarifications on company policies.

## Getting Started

### Dependencies

You can install all required libraries using the following command:
```
pip install -r requirements.txt
```

### Setup Database

After installing dependencies, create the database schema using:
```
python manage.py makemigrations
```

Then apply the migrations:
```
python manage.py migrate
```

### Admin Setup

Create an administrator account for accessing the /admin dashboard:
```
python manage.py createsuperuser
```

### Running the Application

To start the application and run it locally, use the command:
```
python manage.py runserver
```
Once the server is running, you can access the app by visiting http://127.0.0.1:8000/ in your web browser.

## Features

* Home Page: Welcomes users and introduces the handbook.
* Policy List Page: Displays all available policies in a list view.
* Policy Detail Page: Shows detailed information for a selected policy.
* Request Form Page: Allows users to submit questions or clarification requests on policies.
* User Profile Page: Users can personalize this page and save favorite policies.


## Help

Common issues and troubleshooting:
* If migrations fail, ensure your database server is running and try rerunning the migration commands.

## Authors

Mackenzie Freeman
[LinkedIn](https://www.linkedin.com/in/mackenzie-lyn-freeman/)

## Acknowledgments

Inspiration, code snippets, etc.
* [Django Tutorial](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
* [ChatGPT]( )
* [BootStrap Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
