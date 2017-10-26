===============
Microgrid-bench
===============

A microgrid is a small power system connecting devices that consume, generate and store electricity. 
Usually microgrids are able to operate in islanded mode (off-grid), but they can also be connected to the public grid. 
We are interested mostly in the latter casen, because it offers many more valorization mechanisms.

Microgrid-bench is a python tool that aims at simulating the techno-economics of a microgrid, 
and in particular at quantifying the performance of an operational planning controller as a function
of the random processes governing all the variables that impact the microgrid operation 
(e.g. consumption, renewable generation, market price).

Operational planning is the process that controls the operation of a microgrid over a relatively 
long time horizon (from a few hours to several days) divided in periods during which quantities are assumed constant. 
A period can last from one minute to one hour. Hence, fast dynamics of the system are not considered.

Microgrid-bench offers the following functionalities:

* To simulate an operationnal planning policy on real data
* Forecasters are automatically generated for all variables that have to be predicted
* New datasets can be easily integrated (``datasets.csv``)
* The microgrid topology can be easily configured (See e.g. ``data/case1.json``)
* Results are stored in the ``results`` folder (e.g. ``case1_out.json``)
* Plots are automatically generated and can be regenerated from a set of existing results (e.g. ``case1_out.json``)

============
Installation
============

Consult the file readme.md for instructions regarding the required configuration steps.

=======================
Running the application
=======================

Run ``python main.py``

Configure the file ``main.py`` if you want to change

* the simulation length
* the controller
* etc.