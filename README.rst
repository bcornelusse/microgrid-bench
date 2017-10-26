Installation
============

1. Download the code from `Github <https://github.com/bcornelusse/microgrid-bench>`__
2. We highly recommend to use an Anaconda distribution

 a. download and install `Anaconda <https://www.anaconda.com/download/>`__ for Python 2.7 and your specific OS.

 b. Create one environement for this project

 ::

    conda create --name microgrid --file conda-{platform}.txt

 where "{platform}" must matche your OS. Checkout `this
 reference <https://conda.io/docs/user-guide/tasks/manage-environments.html>`__
 for more information about how to manage Anaconda environments.

 c. Activate the environment

 For Windows:

 ::

    activate microgrid

 For OSX and Linux,

 ::

    source activate microgrid

Running the application
=======================
At the root of the project, execute

::

    python main.py


Configure the file ``main.py`` if you want to change

* the simulation length
* the controller
* etc.

`Read the doc <http://microgrid-bench.readthedocs.io/en/latest/>`__ for more information.

Alternatively you can generate the documentation yourself if you have sphinx installed:

::

    cd <to the root of the project>
    sphinx-apidoc -o docs/ microgrid/ -f --separate
    cd docs; make html; cd ..

The html doc is in ``_build/html``