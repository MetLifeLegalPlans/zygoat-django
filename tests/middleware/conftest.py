from django.conf import settings


def pytest_configure():
    settings.configure(
        SESSION_ENGINE="django.contrib.sessions.backends.file", SECRET_KEY="required"
    )
