Ansible role ableton.pkg_mgr_path
=================================

This role sets variables for non-standard paths that belong to an Ansible host's package
manager. The primary use-case is for provisioning on macOS-based hosts where the
[Homebrew][homebrew] and [MacPorts][macports] package managers aren't able to install
their packages to a location which is part of the default system `PATH`.

When this role finishes, it will set data in facts which can then be used to set the path
for other tasks. Please see the "Role Variables" and "Example Playbook" sections below.

Requirements
------------

Ansible >= 2.10 is required. The following host OS types are supported:

- Debian Linux
- macOS (for both Homebrew and MacPorts)
- Windows ([Chocolatey][chocolatey])

On Linux, `apt` can install packages to the system `PATH`, and on Windows the concept of
paths (especially with Ansible) is somewhat different, however this role supports those OS
types in the interest of being cross-platform. The intention is that role should be easy
to add as a dependency of another role regardless of the OS type.

Role Variables
--------------

This role has no required variables, but when it finishes running, it will _set_ these
variables for you:

- `ansible_pkg_mgr_bin`: The location to the package manager's binary folder (for example,
  `/opt/whatever/bin`).
- `ansible_pkg_mgr_path`: The full system path with the package manager's binary folder
  first (for example, `/opt/whatever/bin:/usr/bin:/bin:/usr/sbin:/sbin`).
- `ansible_pkg_mgr_prefix`: The prefix to the package manager's installation folder (for
 example, `/opt/whatever`).

**IMPORTANT**: While this role has no required variables, it _does_ require that the
`ansible_pkg_mgr` variable has been set. This is usually set when gathering facts for a
host, but can also be set manually, or by calling the `gather_facts` module.

Example Playbook
----------------

```yaml
---
- name: Run a command which has been installed by a package manager
  hosts: "all"

  roles:
    - ableton.pkg_mgr_path

  tasks:
    - name: Run a command by setting the PATH for this task
      command: cowsay hello
      environment:
        PATH: "{{ ansible_pkg_mgr_path }}"

    - name: Run a command with the absolute path
      command: "{{ ansible_pkg_mgr_bin }}/cowsay hello"
```

License
-------

MIT

Maintainers
-----------

This project is maintained by the following GitHub users:

- [@ala-ableton](https://github.com/ala-ableton)
- [@nre-ableton](https://github.com/nre-ableton)


[chocolatey]: https://chocolatey.org/
[homebrew]: https://brew.sh
[macports]: https://www.macports.org
