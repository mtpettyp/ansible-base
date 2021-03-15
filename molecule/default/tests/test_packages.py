import pytest

"""Role testing packages using testinfra."""


@pytest.mark.parametrize("package", [
    ("ntp"),
    ("openssh-server"),
    ("unattended-upgrades"),
    ("libpam-google-authenticator"),
    ("ufw"),
    ("zsh"),
    ("git")
])
def test_packages(host, package):
    """Test that the appropriate packages were installed."""
    assert host.package(package).is_installed
