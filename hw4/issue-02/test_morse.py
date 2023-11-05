from morse import decode
import pytest


@pytest.mark.parametrize(
    'morse_message, result',
    [
        ('- . ... - -....- ... - .-. .. -. --.', 'TEST-STRING'),
        ('..--.. .- -... -.-. ..--..', '?ABC?'),
        ('.- .- .- -....- .--. -.-- - .... --- -. '
         '-....- ..--- ----- ..--- ...--', 'AAA-PYTHON-2023')
    ]
)
def test_decode(morse_message, result):
    assert decode(morse_message) == result
