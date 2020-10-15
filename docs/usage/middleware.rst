Middleware
----------

``ReverseProxyHandlingMiddleware``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the IP address of the user correctly when behind a reverse proxy.

Add it as the first entry in your ``MIDDLEWARE`` list in your settings file:

.. code-block:: python

   MIDDLEWARE = [
       "zygoat_django.middleware.ReverseProxyHandlingMiddleware",
       # The rest of your middleware goes here
   ]


``session_expiration_middleware``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Expires user sessions after a period of inactivity.

Add it after ``SessionMiddleware`` in your ``MIDDLEWARE`` list in your settings file:

.. code-block:: python

   MIDDLEWARE = [
       # ...
       "django.contrib.sessions.middleware.SessionMiddleware",
       "zygoat_django.middleware.session_expiration_middleware",
       # ...
   ]

To customize the behavior of this middleware, the following settings are available:

``SESSION_EXPIRATION_SECONDS`` - how long to wait in seconds before expiring the user's session. Default: 3600.

``SESSION_EXPIRATION_ACTIVITY_RESETS`` - boolean that determines whether user activity delays the expiration of the session. Default: True.

``SESSION_EXPIRATION_KEY`` - key to use in the session to track the expiration time. Default: "_last_active_at".
