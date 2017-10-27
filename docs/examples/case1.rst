Case 1 description
------------------

Case 1 is a really simple microgrid made of three loads, one PV installation, and one storage device.
The microgrid is grid-tied, and can thus exchange with the grid at a price indexed on the spot price.
A peak pricing penalty is also applied and is implemented as follows:

* At the beginning of each month, the highest peak over the 11 preceding months is stored in :math:`p_{past}`
 - A cost proportional to :math:`p_{past}` is directly incurred
* Then, the highest monthly peak is recorded at each period :math:`t` in a variable  :math:`p_t`
 - Every time :math:`p_t > p_{past}`, a cost proportional to (:math:`p_t - p_{past}`) is incurred, and :math:`p_{past} := p_t`