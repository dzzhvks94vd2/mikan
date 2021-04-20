import pytest
from mikan import MonthDayCounter, Number

@pytest.mark.parametrize(
    "number,expkanji,expdigits,expkana",
    [
        (1, '一日', '1日', 'ついたち'),
    ]
)
def test_hon_counter(number, expkanji, expdigits, expkana):
    word = Number(number) + MonthDayCounter()
    assert expkanji in word.writings
    assert expdigits in word.writings
    assert expkana in word.readings
