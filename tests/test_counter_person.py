import pytest
from mikan import PersonCounter, Number

@pytest.mark.parametrize(
    "number,expkanji,expdigits,expkana",
    [
        (1, '一人', '1人', 'ひとり'),
        (2, '二人', '2人', 'ふたり'),
        (3, '三人', '3人', 'さんにん'),
        (4, '四人', '4人', 'よにん'),
        (5, '五人', '5人', 'ごにん'),
        (7, '七人', '7人', 'ななにん'),
        (7, '七人', '7人', 'しちにん'),
    ]
)
def test_hon_counter(number, expkanji, expdigits, expkana):
    word = Number(number) + PersonCounter()
    assert expkanji in word.writings
    assert expdigits in word.writings
    assert expkana in word.readings
