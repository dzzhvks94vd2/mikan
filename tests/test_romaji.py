import pytest
from mikan.utils import *

@pytest.mark.parametrize(
    "romaji,expected",
    [
        ("kafe", 'カフェ'),
        ("fakusu", "ファクス"),
    ]
)
def test_to_katakana(romaji, expected):
    assert to_katakana(romaji) == expected

@pytest.mark.parametrize(
    "romaji,expected",
    [
        ("kinyoubi", 'きにょうび'),
        ("kin'youbi", 'きんようび'),
        ("きんyoubi", 'きんようび'),
    ]
)
def test_to_hiragana(romaji, expected):
    assert to_hiragana(romaji) == expected

@pytest.mark.parametrize(
    "kana,expected",
    [
        ("ファクス", "fakusu"),
        ("カフェ", "kafe"),
        ("きんようび", "kin'youbi"),
        ("ゆうめい", "yuumei"),
        ("びょういん", "byouin"),
        ("ちょっと", "chotto"),
        ("じぶん", "jibun"),
        ("ふたり", "futari"),
        ("どちら", "dochira"),
        ("デパート", "depa-to"),
        ("つづく", "tsudzuku"),
        ("べんきょう", "benkyou"),
        ("クッキー", "kukki-"),
        ("コンピューター", "konpyu-ta-"),
        ("いっしょ", "issho"),
        ("キャベツ", "kyabetsu"),
        ("かぞく", "kazoku"),
        ("ミャンマー", "myanma-"),
        ("みょうじ", "myouji"),
        ("ミュージック", "myu-jikku"),
    ]
)
def test_to_romaji(kana, expected):
    assert to_romaji(kana) == expected
