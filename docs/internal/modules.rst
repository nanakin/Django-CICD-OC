=============
Internals
=============

.. toctree::
    :caption: Modules
    :maxdepth: 1

    site-module
    lettings-module
    profiles-module

Structure of the project
========================
| 📁
| ├── lettings
| │    ├── templates, migrations, urls.py, views.py
| │    └── models.py
| ├── profiles
| │    ├── templates, migrations, urls.py, views.py
| │    └── models.py
| └── oc_lettings_site
|      ├── templates, migrations, urls.py, views.py
|      └── settings.py

.. note::
    The ``oc_lettings_site`` directory is the root directory of the project, containing the ``settings.py`` file.
    The other two directories are the apps of the project, containing their own models, URL patterns, templates, etc.

