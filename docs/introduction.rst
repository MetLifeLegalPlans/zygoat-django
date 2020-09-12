What is ``zygoat-django``?
--------------------------

``zygoat-django`` is a pluggable Django module used to provide a set of baseline functionality for ``zygoat`` generated projects, without checking in "managed" code files to the repository.

Installation
------------

``zygoat`` will install this into your new project automatically upon creation, and in a typical use case it will not manually need to be installed.

If, for some reason, you desire to manually install it - you can do so as such from ``pypi``

::

   pip install zygoat-django


And then add it to the end of your ``INSTALLED_APPS`` in ``settings.py``

::

   INSTALLED_APPS = [
       # Django built-ins, user defined modules
       "backend",
       "zygoat_django",
   ]
