# Epic Recipes

# Description

This project is a challenge for a job opening. It's a Recipe and Ingredients platform.

Deployed app at Heroku: https://epic-recipes.herokuapp.com/

In order to access the project and test it I created a login and password:

```
username: epicuser
password: epic123456
```


# Installing

First step of installation is having Pipenv installed in your machine, if you doesn't have just use the below command:

``` $ pip install pipenv ```

Now after cloned the repository all you need to do is:

```
$ cd epicrecipes/
$ pipenv install
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

Remember that for the project fully work, you must configure the env vars from 
the database and the AWS keys.
