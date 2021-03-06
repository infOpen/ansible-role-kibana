# kibana

[![Build Status](https://travis-ci.org/infOpen/ansible-role-kibana.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-kibana)

Install kibana package.

## Requirements

This role requires Ansible 2.1 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Locally, you can run tests on Docker (default driver) or Vagrant.
Travis run tests using Docker driver only.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Xenial

and use:
- Ansible 2.1.x
- Ansible 2.2.x
- Ansible 2.3.x

### Running tests

#### Using Docker driver

```
$ tox
```

#### Using Vagrant driver

```
$ MOLECULE_DRIVER=vagrant tox
```

## Role Variables

### Default role variables

``` yaml
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.kibana }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
