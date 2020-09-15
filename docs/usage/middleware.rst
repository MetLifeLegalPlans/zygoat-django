Middleware
----------

``zygoat-django`` exports one piece of middleware currently, which sets the IP address of the user correctly when behind a reverse proxy.

Add it as the first entry in your ``MIDDLEWARE`` list in your settings file:

.. code-block:: python

   MIDDLEWARE = [
       "zygoat_django.middleware.ReverseProxyHandlingMiddleware",
       # The rest of your middleware goes here
   ]
