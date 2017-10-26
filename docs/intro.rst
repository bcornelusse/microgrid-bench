=======================
What is Microgrid-bench
=======================


A microgrid is a small power system connecting devices that consume, generate and store electricity. 
Usually microgrids are able to operate in islanded mode (off-grid), but they can also be connected to the public grid. 
We are interested mostly in the latter case, because it offers many more valorization mechanisms.


Operational planning
--------------------

Operational planning is the process that controls the operation of a microgrid over a relatively 
long time horizon (from a few hours to several days) divided in periods during which quantities are assumed constant. 
A period can last from one minute to one hour. Hence, fast dynamics of the system are not considered.

A test-bench to assess operational planning policies
----------------------------------------------------

Microgrid-bench is a python tool that aims at simulating the techno-economics of a microgrid, 
and in particular at quantifying the performance of an operational planning controller as a function
of the random processes governing all the variables that impact the microgrid operation 
(e.g. consumption, renewable generation, market price).


Functionalities
---------------

Microgrid-bench offers the following functionalities:

* To simulate an operational planning policy on real data
* Forecasters are automatically generated for all variables that have to be predicted
* New datasets can be easily integrated (``datasets.csv``)
* The microgrid topology can be easily configured (See e.g. ``data/case1.json``)
* Results are stored in the ``results`` folder (e.g. ``case1_out.json``)
* Plots are automatically generated and can be regenerated from a set of existing results (e.g. ``case1_out.json``)

So far, the following devices are available:

* Non-flexible loads 
* Non-flexible generation
* Simple battery model: limited capacity, max (dis)charge rates, (dis)charge efficiencies

Regarding the pricing scheme:

* Variable purchase price
* Variable sales price
* Peak pricing: max monthly peak, 12 months rolling horizon.