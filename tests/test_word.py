import pytest
from mikan import Compound, Word

def test_word_kanji():
    word = Word('日')
    assert word.writings == ['日']
    assert word == Word('日')

def test_word_kana():
    word = Word('ひ')
    assert word.readings == ['ひ']
    assert word == Word('ひ')

def test_word_both():
    word = Word('ひ', '日')
    assert word.readings == ['ひ']
    assert '日' in word.writings

    fire = Word('ひ', '火')
    assert word != fire

def test_word_implicit():
    word = Word('日')
    assert word.writings == ['日']
    word = Word('ひ')
    assert word.readings == ['ひ']
    word = Word('ズボン')
    assert word.readings == ['ズボン']

def test_word_index():
    word = Word('食べる', 'たべる')
    stem, okurigana = word.split_okurigana(1)
    assert okurigana == 'る'
    assert stem == Word('食べ', 'たべ')

def test_word_append():
    word = Word('食べ', 'たべ')
    assert word + 'る' == Word('食べる', 'たべる')
    word += 'る'
    assert word == Word('食べる', 'たべる')

def test_word_word():
    word1 = Word('日本語', 'にほんご')
    word2 = Word(word1)
    assert word1 == word2

def test_word_add_word():
    word1 = Word('電話')
    word2 = Word('番号')
    word = word1 + word2
    assert isinstance(word, Compound)
    assert '電話番号' in word.writings
    assert word == Word('電話番号')
    assert Word('電話番号') == word

def test_word_add_compound():
    word1 = Word('日本', 'にほん')
    word2 = Word('料理', 'りょうり')
    word3 = word1 + word2

    word4 = Word('おいしい')
    word5 = word4 + word3
    assert isinstance(word5, Compound)
    assert 'おいしい日本料理' in word5.writings
    assert 'おいしいにほんりょうり' in word5.readings

@pytest.mark.parametrize(
    "arg1,arg2,expected",
    [
        ['たべる', '食べる', 'たべる'],
        ['食べる', 'たべる', '食べる'],
    ]
)
def test_to_string(arg1, arg2, expected):
    word = Word(arg1, arg2)
    assert str(word) == expected

def test_word_add_str():
    word1 = Word('リンゴ')
    word2 = word1 + 'が'
    assert 'リンゴが' in word2.readings
