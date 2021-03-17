"""Role testing users using testinfra."""


def test_users(host):
    """Validate that users are created correctly """
    test1 = host.user("test1")

    assert test1.exists
    assert test1.shell == "/bin/zsh"

    assert host.file("/home/test1/.ssh/authorized_keys").exists

    test2 = host.user("test2")
    assert test2.exists
    assert test2.shell == "/bin/bash"
