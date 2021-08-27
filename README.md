# Renter-Api
A Renter(ভারাটিয়া) management system(RMS) for creating billing &amp; stroing informations like CRM(Customer Relation Management) . This Server will serve the basic api requrest for client request.

## Project Run Instructions:
### Create a virtual environment to isolate our package dependencies locally
* `python3 -m venv env`
* `source env/bin/activate`  # On Windows use `env\Scripts\activate`
### Install all dependencies 
* `pip install -r requirements.txt`
* `pip freeze > requirements.txt`
  
### Adding Countries Instructions:
* Open Terminal
* Go to project directory
* Type `python manage.py migrate`

### Project Run Instructions:
* Open Terminal
* Go to project directory
* Create Super User 
   * Type  `python manage.py createsuperuser`
  
* Type `python manage.py runserver`
