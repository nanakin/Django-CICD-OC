#################
About the project
#################

About the company
=================
Orange County Lettings is a start-up in the real estate **rental** industry with an **online platform**. 


The project design and technologies
====================================


Web framework and project tree
------------------------------
The online platform is made with the ``Django`` web framework.

The project is split into 3 applications:

    * the *lettings* part,
    * the user *profiles* part,
    * the general/main part (hosting settings).

Each app has its own URL config, models, views, templates and tests.
More about technical aspect HERE.
.. todo

Database
------------
Its data is stored in a relational database ``sqlite``. 
To keep existing data, migrations files were written to reflect model changes.

Tests
-----
The Python testing framework used for that project is ``pytest``, coupled with ``coverage``.
More about the test suite HERE.
.. todo 

Log tracking
------------
The log messages inserted in the code and Django's errors messages are tracked and monitored by ``Sentry``.

Continuous integration and delivery
-----------------------------------
.. todo A local pre-commit hook is configured to clean the code and to avoid basics mistakes to be pushed on remote branches.
.. todo replace by github action
.. todo on all branches
.. todo on ``master`` branch:
.. todo replace Render by AWS

The chosen CI/CD platform to automate the build, test, and deployment is ``CircleCI``.


Triggers:
    * On ``master`` branch: build and test.
    * Additional steps on ``production`` branch: Build and push a ``Docker`` image to the ``DockerHub`` registry. 
      Then the image re-deployment on the ``Render`` web service host.
