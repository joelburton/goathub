GoatHub
=======

A mini-best practice Django 1.11 site inspired by Meggie's awesome GoatHub.

Demonstrates good style and use of class-based views.


Requirements
------------

- Python 3.6 [it uses Py3 print() and Py3.6 f"strings")

- SQLite (which you should have via Python already)


Installation
------------

1. Create a virtualenv::

     virtualenv-3.6 venv
     source venv/bin/activate

   (If you prefer, you can use pyvenv instead)

2. Install requirements::

     pip install -r requirements.txt

3. Bootstrap Django tables::

     python manage.py migrate


4. Run tests::

     python manage.py test

Play With Site
--------------

1. Add an admin user::

     python manage.py createsuperuser

2. Load default fixtures to get some sample data in the real database::

     python manage.py loaddata default

3. Start server::

     python manage.py runserver

4. You can visit and play with site at

   - http://localhost:8000/

   - http://localhost:8000/admin

To see the features for adding/editing/deleting goats outside of the Django
admin, you will need to either be a superuser user or explicitly be given
permissions in the django admin/User.
