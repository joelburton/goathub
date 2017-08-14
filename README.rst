GoatHub
=======

This project requires:

- Python 3.6 [it uses Py3 print() and Py3.6 f"strings")

- SQLite (which you should have via Python already)


1. Create a virtualenv::

     virtualenv-3.6 venv
     source venv/bin/activate

2. Install requirements::

     pip -r requirements.txt

3. Bootstrap Django::

     python manage.py migrate           # create tables
     python manage.py createsuperuser   # create user for yourself

4. Load sample data::

     python manage.py loaddata default  # loads "fixtures" of several goats

5. Run tests::

     python manage.py test

6. Start server::

     python manage.py runserver

7. You can visit and play with site at

   - http://localhost:8000/   # public view, but with extra features for staff

   - http://localhost:8000/admin
