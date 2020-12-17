# Verdict
### About
A fully featured blog application built with Django.
[Click here](http://hmsayem.pythonanywhere.com) to view a live version of the website.

### Features

- User Registration
- User Login & Logout
- Create, Update, Edit & Delete Posts
- Blog Categories
- Comments
- Likes
- User Setting

### Screenshot

<img src="media/demo.gif">

### How to set up
##### Clone project & Install Requirements
> Make sure you have already installed python3 and git.
```
git clone https://github.com/hmsayem/Verdict.git && cd Verdict
pip install -r requirements.txt
```
##### Migrate & Collect Static
```
python manage.py migrate
python manage.py collectstatic
```
##### Create Admin User
```
python manage.py createsuperuser
```
##### Run Server
```
python manage.py runserver
```
>  The blog should be available at `localhost:8000`. You can login as an admin at `http://localhost:8000/admin`.
