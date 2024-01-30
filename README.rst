====================
Holiday Homes |logo|
====================

|build-status| |docs|

.. |build-status| image:: https://dl.circleci.com/status-badge/img/gh/nanakin/OC-P13-Django-CICD/tree/master.svg?style=shield
    :target: https://dl.circleci.com/status-badge/redirect/gh/nanakin/OC-P13-Django-CICD/tree/master
    :alt: Build Status

.. |docs| image:: https://readthedocs.org/projects/holiday-homes/badge/?version=latest
    :target: https://holiday-homes.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |logo| image:: https://github.com/nanakin/OC-P13-Django-CICD/assets/14202917/992d4714-36a2-4970-bcf5-ffd791fb5161
    :width: 60

Preamble
========

This application was designed for a school project with specific requirements and fixed constraints (for example, the given database was sqlite).
This project is not intended be perfect and to evolve that much once finished. 
For that reason, this project is not open to contribution.

The following need is fictive.

Project context
===============
Orange County Lettings is a start-up in the real estate **rental** industry with an `online platform <https://holidays-homes.onrender.com/>`_.
The start-up is in the midst of an expansion phase and has decided to hire a new recruit: and here I am.

The company's main needs are as follows:

* Splitting the existing application to make it more **modular**,
* Adding a comprehensive **test suite**,
* Creating a **CI/CD pipeline**,
* Tracking and monitoring **logs** and **errors**,
* **Documenting** the application.

Documentation
=============
A `documentation of this project <https://holiday-homes.readthedocs.io/en/latest/>`_ is available on ReadTheDocs.

Quick-start
===========
.. inclusion-marker-do-not-remove

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

.. quickstart-end-marker

The project design and technologies
====================================

Technologies:
-------------
* The online platform is made with the ``Django`` web framework.
* Its data is stored in a relational database ``sqlite``.
* The Python testing framework used for that project is ``pytest``, coupled with ``coverage``.
* The log messages inserted in the code and Django's errors messages are tracked and monitored by ``Sentry``.
* The chosen CI/CD platform to automate the build, test, and deployment is ``CircleCI``.
* Commits on ``master`` branch trigger build and push of a ``Docker`` image to the ``DockerHub`` registry.
* The Docker image is then auto-deployed on the ``Render`` web service host.
* The documentation is build with ``sphinx`` and deployed on ``ReadTheDocs``.

More details in documentation
-----------------------------
* Read `Development Guide <https://holiday-homes.readthedocs.io/en/latest/development/development.html>`_ to know more about the testing and the deployment process.
* Read `Internals <https://holiday-homes.readthedocs.io/en/latest/internal/modules.html>`_ to know more about technical aspects of the web application (models, URLs, etc.).
