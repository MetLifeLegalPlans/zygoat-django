Recommended Usage
-----------------

``zygoat`` will automatically install ``zygoat-django`` into your project when it's being generated, and adds a single import statement to your ``settings.py`` file.

::

   from zygoat_django.settings import *  # noqa


This applies all of the default settings values typically used with Zygoat, and makes them modifiable later.

.. include:: middleware.rst

.. include:: commands.rst
