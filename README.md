# In Queue

## About
A fully featured Django programming blog application implemented with all the best practices like user authentication, adding posts, adding comments, editing, blog categories and many more.

## How to set up
Clone This Project (Make Sure You Have Git Installed)
```
https://github.com/mustafamuratcoskun/DjangoBlogApp.git
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
Go to the web browser and visit `http://localhost:8000/admin`
After all these steps , you can start testing and developing this project.
