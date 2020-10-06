# Verdict

## About
A fully featured Django programming blog application implemented with all the best practices like user authentication, adding posts, adding comments, editing, blog categories and many more.

## How to set up
Clone This Project (Make Sure You Have Git Installed)
```
https://github.com/hmsayem/In-Queue.git
```
Install Dependencies

```
pip install -r requirements.txt
```

Set Database (Make Sure you are in directory same as manage.py)
```
python manage.py makemigrations
python manage.py migrate
```
Create SuperUser
```
python manage.py createsuperuser
```
Run server on port 8000:
```
python manage.py runserver 8000
```
The blog should be available at `localhost:8000`
