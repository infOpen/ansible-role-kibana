"""
Role tests
"""
import pytest


# To run all the tests on given docker images:
pytestmark = pytest.mark.docker_images('infopen/ubuntu-xenial-ssh-py27:0.2.0')


def test_packages(Package):
    """
    Tests about packages installed on all systems
    """

    packages = [
        'python-apt-common', 'python-apt', 'kibana'
    ]

    for package in packages:
        assert Package(package).is_installed is True


def test_process(Process):
    """
    Test about kibana processus
    """

    assert len(Process.filter(user='kibana')) == 1


def test_service(Command, Service, Socket):
    """
    Test about kibana service
    """

    assert Service('kibana').is_enabled
    assert Service('kibana').is_running
    assert Command('systemctl status kibana').rc == 0
    assert Socket("tcp://0.0.0.0:5601").is_listening
