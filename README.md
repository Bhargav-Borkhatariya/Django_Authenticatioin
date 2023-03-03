# Django_Authenticatioin
It is a simple authentication that provide login and signup functionality for user.

Functionality like every successful redirect have proper msg for guidance and greeting.
---
# Home_Page
Here you can get the option for signup and sign in navbar.
---
# SignUp_Page
Need to file form that have fiels like.
1. username
2. firstname
3. lastname
4. email
5. password
6. confirm password
7. Upload Image.

## We have validation like.

* for username = characters lessthan 20.
* for email = syntax validation.
* for password = Bothe password should match.

After succefully login redirect to the signin page.
--- 
# SignIn_Page.
Simple need to provide the Some fields for login like.

1. username
2. password

In their you have signout link.
After succesfully login redirect to the dashboard, find their your username with greeetings.
---
# Dashboard_Page.
Just have some greeting for user.

# Deploy
For run this we app need to follow steps like.

1. Download zip and extract it.(Also other options, you can find online.)
2. creat virtual enviroment.
``` python -m venv venv ```
* activate enivroment.
MacOS/Linux: ``` source venv/bin/activate```
Windows: ``` lib/bin/activate``` (Not sure.)
3. Install requirements.txt file.
``` pip install -r requirements.txt```
4. Need to change mysql client credintials in setting.py file.
``` username and pass``` 
5. Creat database and tables.
``` python manage.py makemigrations```
``` python manage.py migrate```
6. run development server.
``` python manage.py runserver```

You are good go, open browser and open your localhost url.
Mostly at 127.0.0.0:8000
