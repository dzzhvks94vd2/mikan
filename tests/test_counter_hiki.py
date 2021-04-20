import pytest
from mikan import Counter, Number

@pytest.mark.parametrize(
    "number,expkanji,expdigits,expkana",
    [
        (1, '一匹', '1匹', 'いっぴき'),
        (2, '二匹', '2匹', 'にひき'),
        (3, '三匹', '3匹', 'さんびき'),
        (6, '六匹', '6匹', 'ろっぴき'),
        (8, '八匹', '8匹', 'はっぴき'),
        (8, '八匹', '8匹', 'はちひき'),
        (11, '十一匹', '11匹', 'じゅういっぴき'),
    ]
)
def test_counter_hiki(number, expkanji, expdigits, expkana):
    word = Number(number) + Counter('匹', 'ひき')
    assert expkanji in word.writings
    assert expdigits in word.writings
    assert expkana in word.readings

def test_counter_hiki_wrong():
    word = Number(3) + Counter('匹', 'ひき')
    assert word != 'さんひき'
    assert set(word.writings) == {'三匹', '3匹', 'さんびき'}
    assert len(word.writings) == 3
