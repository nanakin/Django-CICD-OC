=============
Holiday Homes
=============
|build-status| |docs|

.. |build-status| image:: https://dl.circleci.com/status-badge/img/circleci/CVZEF2DgaEvNNLCtk1cBjE/hyQGadU9yQwGaXQDDaWPU/tree/master.svg?style=shield&circle-token=122a67c5e3a0cf8dc592279f806555298adcb627
    :target: https://dl.circleci.com/status-badge/redirect/circleci/CVZEF2DgaEvNNLCtk1cBjE/hyQGadU9yQwGaXQDDaWPU/tree/master
    :alt: Build Status


.. |docs| image:: https://readthedocs.org/projects/holiday-homes/badge/?version=latest
    :target: https://holiday-homes.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status



.. image:: https://github.com/nanakin/OC-P13-Django-CICD/assets/14202917/992d4714-36a2-4970-bcf5-ffd791fb5161
   :width: 60
   :align: center

Preamble
========

This application was designed for a school project with specific requirements and fixed constraints (for example, the given database was sqlite).
This project is not intended be perfect and to evolve that much once finished. 
For that reason, this project is not open to contribution.

The following need is fictive.

Project context
===============
Orange County Lettings is a start-up in the real estate **rental** industry with an **online platform**. 
The start-up is in the midst of an expansion phase and has decided to hire a new recruit: and here I am. 

The company's main needs are as follows:
    - Splitting the existing application to make it more **modular**
    - Adding a comprehensive **test suite**
    - Creating a **CI/CD pipeline**
    - Tracking and monitoring **logs** and errors
    - **Documenting** the application.

Documentation
=============
A `documentation of this project <https://holiday-homes.readthedocs.io/en/latest/>`_ is available on ReadTheDocs.

.. inclusion-marker-do-not-remove

Quick-start
===========



#. git clone this repository::

        git clone https://github.com/nanakin/OC-P13-Django-CICD.git Django-CICD

#. Move to the project directory::

        cd Django-CICD

#. Install poetry (if not installed yet), by following the `official documentation <https://python-poetry.org/docs/#installation>`_.

#. Install project dependencies in a new virtual environment using poetry::

        poetry install

#. Rename a ``.env.example`` file as ``.env``::

        mv .env.example .env

#. Edit the ``.env`` file to set the environment variables

#. Apply database migrations::

        poetry run python manage.py migrate

#. Collect static files (if your environment variable DEBUG is False)::

        poetry run python manage.py collectstatic

#. Run a development server locally::

        poetry run python manage.py runserver

#. Open your browser and go to  `<http://127.0.0.1:8000/>`_ to see the application running.

The project design and technologies
====================================

* Read `Internals <https://holiday-homes.readthedocs.io/en/latest/internal/modules.html/>`_ to know more about technical aspects of the web application (models, URLs, etc.).
* Read `Development Guide <https://holiday-homes.readthedocs.io/en/latest/internal/modules.html/>`_ to know more about the testing, the log tracking, the documentation and the deployment process.

Web framework
-------------
The online platform is made with the ``Django`` web framework.

The project is split into 3 applications:

* the *lettings* part,
* the user *profiles* part,
* the general/main part (hosting settings).

Each app has its own URL config, models, views, templates and tests.

Database
--------
Its data is stored in a relational database ``sqlite``.

To keep existing data, migrations files were written to reflect model changes.

Tests
-----
The Python testing framework used for that project is ``pytest``, coupled with ``coverage``.

Log tracking
------------
The log messages inserted in the code and Django's errors messages are tracked and monitored by ``Sentry``.

Continuous integration and delivery
-----------------------------------

The chosen CI/CD platform to automate the build, test, and deployment is ``CircleCI``.


jobs:

* On *all* branches: build and test.
* Additional steps on ``master`` branch: Build and push a ``Docker`` image to the ``DockerHub`` registry. Then trigger the image re-deployment on the ``Render`` web service host.

More about the CI/CD pipeline in `Development section <https://holiday-homes.readthedocs.io/en/latest/development.html>`_.

