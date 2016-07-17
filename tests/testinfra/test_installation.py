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


def test_config_files(File):
    """
    Test about config files
    """

    files = ['/etc/default/kibana', '/opt/kibana/config/kibana.yml']

    for file_name in files:
        current_file = File(file_name)

        assert current_file.exists
        assert current_file.is_file
        assert current_file.user == 'kibana'
        assert current_file.group == 'kibana'
        assert current_file.mode == 0o400

    logrotate_config = File('/etc/logrotate.d/kibana')

    assert logrotate_config.exists
    assert logrotate_config.is_file
    assert logrotate_config.user == 'root'
    assert logrotate_config.group == 'root'
    assert logrotate_config.mode == 0o400


def test_folders(File):
    """
    Test about log and pid folders
    """

    folders = ['/var/log/kibana', '/var/run/kibana']

    for folder in folders:
        current_folder = File(folder)

        assert current_folder.exists
        assert current_folder.is_directory
        assert current_folder.user == 'kibana'
        assert current_folder.group == 'kibana'
        assert current_folder.mode == 0o700


def test_group(Group):
    """
    Test about Kibana group
    """

    assert Group('kibana').exists


def test_user(User):
    """
    Test about Kibana user
    """

    user = User('kibana')

    assert user.exists
    assert user.group == 'kibana'
    assert user.home == '/home/kibana'
    assert user.shell == '/usr/sbin/nologin'
