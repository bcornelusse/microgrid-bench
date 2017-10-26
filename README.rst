Installation
============

1. We highly recommend to download and install
   `Anaconda <https://www.anaconda.com/download/>`__ for Python 2.7 and
   your specific OS.
2. Create one environement for this project

::

    conda create --name microgrid --file conda-{platform}.txt

where "{platform}" must matche your OS. Checkout `this
reference <https://conda.io/docs/user-guide/tasks/manage-environments.html>`__
for more information about how to manage Anaconda environments.

3. Activate the environment.

For Windows:

::

    activate microgrid

For OSX and Linux,

::

    source activate microgrid

Running the application
=======================

::

    python main.py


Configure the file ``main.py`` if you want to change

* the simulation length
* the controller
* etc.

Generating the doc
==================

::

    cd <to the root of the project>
    sphinx-apidoc -o docs/ microgrid/ -f
    cd docs; make html; cd ..

The html doc is in ``_build/html``