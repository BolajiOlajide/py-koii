from __future__ import print_function
from pytest import fixture

from example import create_app


@fixture(scope='module')
def flask_app():
    flask_app = create_app()
    yield flask_app


@fixture(scope='module')
def client(flask_app):
    testing_client = flask_app.test_client()
    print("\n(Doing global fixture setup stuff!)")

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()
