import pytest
from mikan import DayHourCounter, Number

@pytest.mark.parametrize(
    "number,expkanji,expdigits,expkana",
    [
        (1, '一時', '1時', 'いちじ'),
        (4, '四時', '4時', 'よじ'),
        (9, '九時', '9時', 'くじ'),
    ]
)
def test_dayhour_counter(number, expkanji, expdigits, expkana):
    word = Number(number) + DayHourCounter()
    assert expkanji in word.writings
    assert expdigits in word.writings
    assert expkana in word.readings
