cookiecuter-django-paas
=======================

Django template ready to use in Heroku and OpenShift without any specific modification.


Project initialization
----------------------

To start a project run the following command:

    $ cookiecutter https://github.com/pbacterio/cookiecutter-django-paas
    project_name (default is "myproject")?

Start the git repository.

    $ cd myproject
    $ git init .
    $ git add .
    $ git commit -m "initial project version"

Install dependencies listed in `requirements.txt`. I suggest use `pip` and `virtualenvironment`.

    $ virtualenvironment venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt


Running local server
--------------------

Just use `foreman`.

    $ foreman start

Now your application is listening on port 5000. If you want to use other port number run the command like this:

    $ PORT=8080 foreman start


Deploy to Heroku
----------------

    $ heroku apps:create myproject
    $ heroku addons:add heroku-postgresql
    $ git push heroku
    $ heroku run python manage.py syncdb


Deploy to OpenShift
-------------------

    $ rhc app create myproject python-2.7 --no-git
    $ git remote add openshift ssh://2516000083533c2d2c500446@myproject.rhcloud.com/~/git/myproject.git/
    $ rhc add-cartridge postgresql-9.2 --app myproject
    $ ssh 2516000083533c2d2c500446@myproject.rhcloud.com
    [myproject.rhcloud.com 2516000083533c2d2c500446]\> cd app-root/repo
    [myproject.rhcloud.com repo]\> python manage.py syncdb


Other PAAS providers?
---------------------

I'm working to support dotCloud, Gondor and others. Feel free to colaborate.
:smile: