import pytest
from twosix import is_valid_ip, find_ips


@pytest.mark.parametrize(
    "ip_input, ip_expected",
    [("127.0.0.1", True),
     ('0.0.0.0', True),
     ('1.2.3.4.5', False),
     ("999.0.0.0", False),
     ('1', False)
     ], )
def test_is_valid_ip(ip_input, ip_expected):
    assert is_valid_ip(ip_input) == ip_expected

@pytest.mark.parametrize(
    'test_string_ip, tagged_ip',
    [
        ('There is no place like 127.0.0.1.', ['127.0.0.1']),
        ('Is 72.68.0.255 an IP?', ['72.68.0.255']),
        ('72.68.0.110 and 127.0.0.1 is an ip. but 1.2.3.4.5 is not. neither is 2.2', ['72.68.0.110', '127.0.0.1']),
        ('IP:172.168.0.1', ['172.168.0.1'])
    ], )
def test_find_ip(test_string_ip, tagged_ip):
    assert find_ips(test_string_ip) == tagged_ip
