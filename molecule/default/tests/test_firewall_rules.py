import pytest

"""Role testing services using testinfra."""


@pytest.mark.parametrize("rule", [
    ("-A ufw-user-output -p udp -m udp --dport 123 -j ACCEPT"),
    ("-A ufw-user-input -p tcp -m tcp --dport 22 -j ufw-user-limit-accept")
])
def test_ufw_rules(host, rule):
    """Validate that services are enabled and running """
    rules = host.iptables.rules()
    assert rule in rules
