import pytest

"""Role testing 2fa using testinfra."""


@pytest.fixture(autouse=True)
def run_around_tests(host):

    host.run('apt-get install sshpass')
    host.run("rm ~test1/.google_authenticator")

    host.run(
        "yes '' | ssh-keygen -t ed25519 -f /root/.ssh/id_ed25519 -N ''")
    host.run(
        "cat /root/.ssh/id_ed25519.pub >> /home/test1/.ssh/authorized_keys")

    yield

    host.run("rm ~test1/.google_authenticator")


def test_ssh(host):

    # Ensure ssh works with google authenticator not setup
    cmd = host.run("ssh -o StrictHostKeychecking=no test1@localhost")
    assert cmd.succeeded

    # Ensure ssh works with google authenticator setup
    host.run(
        'echo "ABCDEFGHIJKLMNOPQRSTUVWXYZ" > ~test1/.google_authenticator')
    host.run('echo "\\" TOTP_AUTH" >> ~test1/.google_authenticator')
    host.run('echo "12345678" >> ~test1/.google_authenticator')
    host.run('chmod 400 ~test1/.google_authenticator')
    host.run('chown test1:test1 ~test1/.google_authenticator')

    cmd = host.run(
        "sshpass -p 12345678 -P 'Verification code:' "
        "ssh -o StrictHostKeychecking=no test1@localhost")
    assert cmd.succeeded
