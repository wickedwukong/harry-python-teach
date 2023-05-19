import pytest


def add(num1, num2):
    raw = num1 + num2
    return raw.replace('IIIII', 'V')


@pytest.mark.parametrize('num1, num2, expected', [
    ('I', 'I', 'II'),
    ('III', 'III', 'VI'),
    ('II', 'III', 'V'),
    ('II', 'I', 'III'),
    ('I', 'II', 'III'),
    ('I', 'I', 'II'),
    ('I', 'I', 'II'),
])
def test_addition(num1, num2, expected):
    assert add(num1, num2) == expected
