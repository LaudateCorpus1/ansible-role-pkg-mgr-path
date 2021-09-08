"""Molecule tests for the default scenario."""

import os

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_paths_file(host):
    """Test that variables were set correctly."""
    test_paths_file = host.file("/tmp/paths.txt")
    expected_paths = [
        "/usr/bin",  # ansible_pkg_mgr_bin
        # ansible_pkg_mgr_path
        "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
        "/usr",  # ansible_pkg_mgr_prefix
    ]

    assert test_paths_file.is_file
    assert test_paths_file.content.decode() == "\n".join(expected_paths)
