"""
Role tests
"""

import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize('name', [
    ('python-apt-common'),
    ('python-apt'),
    ('kibana'),
])
def test_packages(host, name):
    """
    Tests about packages installed on all systems
    """

    assert host.package(name).is_installed


def test_process(host):
    """
    Test about kibana processus
    """

    assert len(host.process.filter(user='kibana')) == 1


def test_service(host):
    """
    Test about kibana service
    """

    assert host.service('kibana').is_enabled

    if host.system_info.codename == 'jessie':
        jessie_check = host.run('service kibana status')
        assert jessie_check.rc == 0
        assert 'is running' in jessie_check.stdout
    else:
        assert host.service('kibana').is_running
        assert host.check_output('systemctl status kibana').rc == 0


def test_socket(host):
    """
    Test about kibana socket
    """

    assert host.socket("tcp://0.0.0.0:5601").is_listening


@pytest.mark.parametrize('name,user,group,mode', [
    ('/etc/default/kibana', 'kibana', 'kibana', 0o400),
    ('/opt/kibana/config/kibana.yml', 'kibana', 'kibana', 0o400),
    ('/etc/logrotate.d/kibana', 'root', 'root', 0o400),
])
def test_config_files(host, name, user, group, mode):
    """
    Test about config files
    """

    current_file = host.file(name)

    assert current_file.exists
    assert current_file.is_file
    assert current_file.user == user
    assert current_file.group == group
    assert current_file.mode == mode


@pytest.mark.parametrize('name,user,group,mode', [
    ('/var/log/kibana', 'kibana', 'root', 0o755),
    ('/var/run/kibana', 'kibana', 'kibana', 0o700),
])
def test_folders(host, name, user, group, mode):
    """
    Test about log and pid folders
    """

    current_folder = host.file(name)

    assert current_folder.exists
    assert current_folder.is_directory
    assert current_folder.user == user
    assert current_folder.group == group
    assert current_folder.mode == mode


def test_group(host):
    """
    Test about Kibana group
    """

    assert host.group('kibana').exists


def test_user(host):
    """
    Test about Kibana user
    """

    user = host.user('kibana')

    assert user.exists
    assert user.group == 'kibana'
    assert user.home == '/home/kibana'
    assert user.shell == '/usr/sbin/nologin'
