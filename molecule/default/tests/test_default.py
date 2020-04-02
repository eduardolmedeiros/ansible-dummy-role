"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"

def test_nano_package(host):
    """Ensure nano package installed."""
    p = host.package("nano")

    assert p.is_installed

