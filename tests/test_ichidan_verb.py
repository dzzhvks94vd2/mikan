import pytest
from mikan import IAdjective, IchidanVerb, Form, InvalidConjugation

def test_not_ichidan():

    with pytest.raises(ValueError):
        IchidanVerb('みかん')

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('たべる', Form.PRESENT, False, False, 'たべる'),
        ('たべる', Form.PAST, False, False, 'たべた'),
        ('たべる', Form.PRESUMPTIVE, False, False, 'たべるだろう'),
        ('たべる', Form.CONDITIONAL_RA, False, False, 'たべたら'),
        ('たべる', Form.POTENTIAL, False, False, 'たべられる'),
        ('たべる', Form.PASSIVE, False, False, 'たべられる'),
        ('たべる', Form.CAUSATIVE, False, False, 'たべさせる'),
        ('たべる', (Form.CAUSATIVE, Form.PASSIVE), False, False, 'たべさせられる'),

        ('たべる', Form.PRESENT, True, False, 'たべない'),
        ('たべる', Form.PAST, True, False, 'たべなかった'),
        ('たべる', Form.PRESUMPTIVE, True, False, 'たべないだろう'),
        ('たべる', Form.CONDITIONAL_RA, True, False, 'たべなかったら'),
        ('たべる', Form.POTENTIAL, True, False, 'たべられない'),
        ('たべる', Form.PASSIVE, True, False, 'たべられない'),
        ('たべる', Form.CAUSATIVE, True, False, 'たべさせない'),
        ('たべる', (Form.CAUSATIVE, Form.PASSIVE), True, False, 'たべさせられない'),

        ('たべる', Form.PRESENT, False, True, 'たべます'),
        ('たべる', Form.PAST, False, True, 'たべました'),
        ('たべる', Form.PRESUMPTIVE, False, True, 'たべるでしょう'),
        ('たべる', Form.CONDITIONAL_RA, False, True, 'たべましたら'),
        ('たべる', Form.POTENTIAL, False, True, 'たべられます'),
        ('たべる', Form.PASSIVE, False, True, 'たべられます'),
        ('たべる', Form.CAUSATIVE, False, True, 'たべさせます'),
        ('たべる', (Form.CAUSATIVE, Form.PASSIVE), False, True, 'たべさせられます'),

        ('たべる', Form.PRESENT, True, True, 'たべません'),
        ('たべる', Form.PAST, True, True, 'たべませんでした'),
        ('たべる', Form.PRESUMPTIVE, True, True, 'たべないでしょう'),
        ('たべる', Form.CONDITIONAL_RA, True, True, 'たべませんでしたら'),
        ('たべる', Form.POTENTIAL, True, True, 'たべられません'),
        ('たべる', Form.PASSIVE, True, True, 'たべられません'),
        ('たべる', Form.CAUSATIVE, True, True, 'たべさせません'),
        ('たべる', (Form.CAUSATIVE, Form.PASSIVE), True, True, 'たべさせられません'),
    ]
)
def test_ichidan_1(verb, tense, negative, polite, expected):

    v = IchidanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('たべる', Form.IMPERATIVE, False, 'たべろ'),
        ('たべる', Form.IMPERATIVE, True, 'たべるな'),
        ('たべる', Form.TE, False, 'たべて'),
        ('たべる', Form.TE, True, 'たべなくて'),
        ('たべる', Form.CONDITIONAL_EBA, False, 'たべれば'),
        ('たべる', Form.CONDITIONAL_EBA, True, 'たべなければ'),
    ]
)
def test_ichidan_2(verb, tense, negative, expected):

    v = IchidanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('たべる', Form.VOLITIONAL, False, 'たべよう'),
        ('たべる', Form.VOLITIONAL, True, 'たべましょう'),
    ]
)
def test_ichidan_3(verb, tense, polite, expected):

    v = IchidanVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings

def test_ichidan_tai():

    v = IchidanVerb('たべる')
    tai = v.conjugate(Form.TAI)
    assert 'たべたい' in tai.readings

    takunai = v.conjugate(Form.TAI, negative=True)
    assert 'たべたくない' in takunai.readings

    takatta = v.conjugate([Form.TAI, Form.PAST])
    assert 'たべたかった' in takatta.readings

    takunakatta = v.conjugate([Form.TAI, Form.PAST], negative=True)
    assert 'たべたくなかった' in takunakatta.readings

def test_ichidan_word():

    v = IchidanVerb('食べる', 'たべる')
    masu = v.conjugate(polite=True)
    assert '食べます' in masu.writings
    assert 'たべます' in masu.readings

def test_ichidan_to_string_1():

    v = IchidanVerb('たべる', '食べる')
    polite = v.conjugate(polite=True)
    assert str(polite) == 'たべます'

def test_ichidan_to_string_2():

    v = IchidanVerb('食べる', 'たべる')
    polite = v.conjugate(polite=True)
    assert str(polite) == '食べます'

def test_ichidan_invalid():

    v = IchidanVerb('食べる', 'たべる')

    with pytest.raises(InvalidConjugation):
        v.conjugate(Form.IMPERATIVE, polite=True)
