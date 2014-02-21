NetworkPlanner Pyramid
=====================

Temporary repo for bootstrapping the migration of NetworkPlanner to Pyramid

The np/lib module has basically been ported as it's mostly decoupled from
Pylons/Pyramid specifics.

Main TODO's
---------------
- Controllers --> Views
- Routes      --> decorators
- Model       --> top-level models module 
              --> move to implicit transactions?
- Tests       --> update
- Setup       --> attempt to make it setup tools based (and a package?)

