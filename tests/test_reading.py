import pytest
from mikan import Reading, Writing

@pytest.mark.parametrize(
    "string,expected",
    [
        ('食べる', False),
        ('たべる', True),
    ]
)
def test_is_reading(string, expected):
    writing = Writing.create(string)
    if expected:
        assert isinstance(writing, Reading)
    else:
        assert isinstance(writing, Writing)
        assert not isinstance(writing, Reading)
