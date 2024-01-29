Test suite
==========

The testing framework used for that project is ``pytest``

Usage
-----
From the root project directory (in your project environment)::

    pytest

.. note::
   No option required as they are already set in ``pyproject.toml`` under ``[tool.pytest.ini_options]`` section.

   The test suite is considered as a success if the coverage is above 80%.

Writing tests
-------------
When writing tests, remember the following tips and guidelines:

* Each app as its own ``tests`` directory, and almost each module as its own ``test_*.py`` file.
* Use ``pytest.mark.django_db`` decorator on each test function that requires database access.
* When sample or data set is required, use ``pytest_factoryboy`` to create fixtures.

Coverage
--------
After tests, a coveraqe report is printed on the terminal and generated under the ``htmlcov`` directory.

.. note::
   Sources and omissions options are specified in ``pyproject.toml`` under ``[tool.coverage.run]`` section.


PEP8 compliance
---------------

To verify the PEP8 compliance of the project source code, ``flake8`` is used.

To run it locally (in your project environment)::

    flake8

.. note::
   No option required as they are already set in ``.flake8`` file.

.. note::
   In the future, the project test suite may include the ``flake8`` compliance check directly in the ``pytest`` run, using the ``pytest-flake8`` plugin.


Dependencies
------------
The project ``dev`` group dependencies are:

* ``pytest-django``
* ``pytest-cov``
* ``pytest-factoryboy``
* ``flake8``
