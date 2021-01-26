# Epic Recipes

# Description

This project is a challenge for a job opening. It's a Recipe and Ingredients platform.

Deployed app at Heroku: https://epic-recipes.herokuapp.com/


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

# Using Docker

If you prefer to use docker to run the project after cloning the repository, run
this command to build the image and run the container.

``` docker-compose up --build ```

Remember that for the project fully work, you must configure the env vars from 
the database and the AWS keys.


# Testing

To test the application use:

```$ python manage.py test```


