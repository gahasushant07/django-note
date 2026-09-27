1. Open your project folder
cd "C:\Users\thito\OneDrive\Documents\django web"
2. Create a virtual environment

You can use Python's built-in venv:

python -m venv venv

This creates a folder called venv.

3. Activate the virtual environment

For Windows CMD:

venv\Scripts\activate

You should now see something like:

(venv) C:\Users\thito\OneDrive\Documents\django web>

The (venv) means your virtual environment is active.

4. Upgrade pip
python -m pip install --upgrade pip
5. Install Django
pip install django

Check the installation:

django-admin --version
6. If you already have a Django project

For example, if your project contains manage.py:

django web/
│
├── venv/
├── manage.py
└── myproject/
    ├── settings.py
    ├── urls.py
    └── ...

Run:

python manage.py runserver

You should get something similar to:

Starting development server at http://127.0.0.1:8000/

Open:

http://127.0.0.1:8000/
7. If you haven't created a Django project yet

After activating venv:

django-admin startproject myproject .

Then:

python manage.py runserver
8. When you're finished

Stop the server with:

CTRL + C

Then deactivate the virtual environment:

deactivate
🔄 Every time you come back to the project

You don't need to create the virtual environment again. Just:

cd "C:\Users\thito\OneDrive\Documents\django web"
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
python manage.py runserver

pip install virtualenv
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver



\\ to create app
python manage.py startapp myapp

\\ add this myapp to projects settings.py in installed apps
'myapp',


Your django folder is inside Documents, as shown in your terminal output.

In PowerShell

Run:

cd Documents\django