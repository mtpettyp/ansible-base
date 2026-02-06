"""Role testing atuin installation using testinfra."""


def test_atuin_installed(host):
    """Validate that atuin is installed for each user."""
    assert host.file("/home/test1/.atuin/bin/atuin").exists
    assert host.file("/home/test2/.atuin/bin/atuin").exists
