import pytest
from mikan import IAdjective, IchidanVerb, VerbForm

def test_not_ichidan():

    with pytest.raises(ValueError):
        IchidanVerb('みかん')

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('たべる', VerbForm.PRESENT, False, False, 'たべる'),
        ('たべる', VerbForm.PAST, False, False, 'たべた'),
        ('たべる', VerbForm.PRESUMPTIVE, False, False, 'たべるだろう'),
        ('たべる', VerbForm.CONDITIONAL_RA, False, False, 'たべたら'),
        ('たべる', VerbForm.POTENTIAL, False, False, 'たべられる'),
        ('たべる', VerbForm.PASSIVE, False, False, 'たべられる'),
        ('たべる', VerbForm.CAUSATIVE, False, False, 'たべさせる'),
        ('たべる', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, False, 'たべさせられる'),

        ('たべる', VerbForm.PRESENT, True, False, 'たべない'),
        ('たべる', VerbForm.PAST, True, False, 'たべなかった'),
        ('たべる', VerbForm.PRESUMPTIVE, True, False, 'たべないだろう'),
        ('たべる', VerbForm.CONDITIONAL_RA, True, False, 'たべなかったら'),
        ('たべる', VerbForm.POTENTIAL, True, False, 'たべられない'),
        ('たべる', VerbForm.PASSIVE, True, False, 'たべられない'),
        ('たべる', VerbForm.CAUSATIVE, True, False, 'たべさせない'),
        ('たべる', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, False, 'たべさせられない'),

        ('たべる', VerbForm.PRESENT, False, True, 'たべます'),
        ('たべる', VerbForm.PAST, False, True, 'たべました'),
        ('たべる', VerbForm.PRESUMPTIVE, False, True, 'たべるでしょう'),
        ('たべる', VerbForm.CONDITIONAL_RA, False, True, 'たべましたら'),
        ('たべる', VerbForm.POTENTIAL, False, True, 'たべられます'),
        ('たべる', VerbForm.PASSIVE, False, True, 'たべられます'),
        ('たべる', VerbForm.CAUSATIVE, False, True, 'たべさせます'),
        ('たべる', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, True, 'たべさせられます'),

        ('たべる', VerbForm.PRESENT, True, True, 'たべません'),
        ('たべる', VerbForm.PAST, True, True, 'たべませんでした'),
        ('たべる', VerbForm.PRESUMPTIVE, True, True, 'たべないでしょう'),
        ('たべる', VerbForm.CONDITIONAL_RA, True, True, 'たべませんでしたら'),
        ('たべる', VerbForm.POTENTIAL, True, True, 'たべられません'),
        ('たべる', VerbForm.PASSIVE, True, True, 'たべられません'),
        ('たべる', VerbForm.CAUSATIVE, True, True, 'たべさせません'),
        ('たべる', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, True, 'たべさせられません'),
    ]
)
def test_ichidan_1(verb, tense, negative, polite, expected):

    v = IchidanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('たべる', VerbForm.IMPERATIVE, False, 'たべろ'),
        ('たべる', VerbForm.IMPERATIVE, True, 'たべるな'),
        ('たべる', VerbForm.TE_FORM, False, 'たべて'),
        ('たべる', VerbForm.TE_FORM, True, 'たべなくて'),
        ('たべる', VerbForm.CONDITIONAL_EBA, False, 'たべれば'),
        ('たべる', VerbForm.CONDITIONAL_EBA, True, 'たべなければ'),
    ]
)
def test_ichidan_2(verb, tense, negative, expected):

    v = IchidanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('たべる', VerbForm.VOLITIONAL, False, 'たべよう'),
        ('たべる', VerbForm.VOLITIONAL, True, 'たべましょう'),
    ]
)
def test_ichidan_3(verb, tense, polite, expected):

    v = IchidanVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings

def test_ichidan_tai():

    v = IchidanVerb('たべる')
    tai = v.conjugate(VerbForm.TAI)
    assert 'たべたい' in tai.readings
    assert isinstance(tai, IAdjective)

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
