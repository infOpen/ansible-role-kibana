"""
Role tests
"""
import pytest


# To run all the tests on given docker images:
pytestmark = pytest.mark.docker_images('infopen/ubuntu-xenial-ssh-py27')


def test_foo_a(User):
    assert User().name == 'root'


def test_foo_b(User):
    assert User().name == 'root'
