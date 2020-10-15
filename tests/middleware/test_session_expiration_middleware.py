from functools import reduce

import pytest
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import HttpResponse
from django.test import RequestFactory
from django.test.utils import freeze_time

from zygoat_django.middleware.session_expiration import (
    session_expiration_middleware,
    SESSION_EXPIRATION_KEY,
    SESSION_EXPIRATION_SECONDS,
)


TEST_SESSION_KEY = "test_key"
TEST_SESSION_VALUE = "test_value"
TEST_SESSION_DATA = {
    TEST_SESSION_KEY: TEST_SESSION_VALUE,
    SESSION_EXPIRATION_KEY: 0.0,
}


def set_session_middleware(data=None):
    if data is None:
        data = {}

    def middleware(process_request):
        def inner(request):
            for key, value in data.items():
                request.session[key] = value
            return process_request(request)

        return inner

    return middleware


def handle_request(request, view, session_data=None):
    middlewares = [
        session_expiration_middleware,
        set_session_middleware(session_data),
        SessionMiddleware,
    ]
    return reduce(lambda f, g: g(f), middlewares, view)(request)


@pytest.fixture
def req():
    return RequestFactory().get("/")


def test_no_session(req):
    def view(request):
        return HttpResponse()

    handle_request(req, view)

    assert req.session.is_empty()


def test_new_session(req):
    def view(request):
        request.session[TEST_SESSION_KEY] = TEST_SESSION_VALUE
        return HttpResponse()

    handle_request(req, view)

    assert req.session.get(SESSION_EXPIRATION_KEY) is not None
    assert req.session.get(TEST_SESSION_KEY) == TEST_SESSION_VALUE


def test_session_lasts_until_expiration(req):
    def view(request):
        assert request.session.get(TEST_SESSION_KEY) == TEST_SESSION_VALUE
        return HttpResponse()

    with freeze_time(SESSION_EXPIRATION_SECONDS - 1):
        handle_request(req, view, TEST_SESSION_DATA)


def test_session_expires(req):
    def view(request):
        assert request.session.is_empty()
        return HttpResponse()

    with freeze_time(SESSION_EXPIRATION_SECONDS + 1):
        handle_request(req, view, TEST_SESSION_DATA)


def test_session_activity_updates(req):
    def view(request):
        return HttpResponse()

    request_time = 1000

    with freeze_time(request_time):
        handle_request(req, view, TEST_SESSION_DATA)

    assert req.session[TEST_SESSION_KEY] == TEST_SESSION_VALUE
    assert req.session[SESSION_EXPIRATION_KEY] == request_time
