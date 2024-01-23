=============
Holiday Homes
=============

Preamble
========
This application was designed for a school project with specific requirements and fixed constraints (for example, the given database was sqlite).
This project is not intended be perfect and to evolve that much once finished. 
This project is not open to contribution.
The following need is fictive.

Project context
===============
Orange County Lettings is a start-up in the real estate **rental** industry with an **online platform**. 
The start-up is in the midst of an expansion phase and has decided to hire a new recruit: and here I am. 

The company's main needs are as follows:
. Splitting the existing application to make it more **modular**
. Adding a comprehensive **test suite**
. Creating a **CI/CD pipeline**
. Tracking and monitoring **logs** and errors
. **Documenting** the application.

Documentation
=============

`Holiday Homes Documentation <https://holiday-homes.readthedocs.io/en/latest/>`_

.. inclusion-marker-do-not-remove

The project design and technologies
====================================

Web framework
-------------
The online platform is made with the ``Django`` web framework.

The project is split into 3 applications:

    * the *lettings* part,
    * the user *profiles* part,
    * the general/main part (hosting settings).

Each app has its own URL config, models, views, templates and tests.
More about technical aspect HERE.
.. todo

Database
--------
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

Quick-start
===========
Here quick-start doc

