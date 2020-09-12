Usage
=====

Recommended Usage
-----------------

``zygoat`` will automatically install ``zygoat-django`` into your project when it's being generated, and adds a single import statement to your ``settings.py`` file.

::

   from zygoat_django.settings import *  # noqa


This applies all of the default settings values typically used with Zygoat, and makes them modifiable later.


Caveats
^^^^^^^

 - ``zygoat`` will not automatically remove the ``DATABASES`` block from your Django source code on initialization, this must be done manually for now


Details/Advanced Usage
----------------------

To see all that ``zygoat-django.settings`` exports, please see the `API Reference </autoapi/zygoat_django/settings>`_ section of the documentation.
