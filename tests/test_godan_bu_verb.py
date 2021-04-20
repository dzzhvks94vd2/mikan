import pytest
from mikan import GodanVerb, VerbForm

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('とぶ', VerbForm.PRESENT, False, False, 'とぶ'),
        ('とぶ', VerbForm.PAST, False, False, 'とんだ'),
        ('とぶ', VerbForm.PRESUMPTIVE, False, False, 'とぶだろう'),
        ('とぶ', VerbForm.CONDITIONAL_RA, False, False, 'とんだら'),
        ('とぶ', VerbForm.POTENTIAL, False, False, 'とべる'),
        ('とぶ', VerbForm.PASSIVE, False, False, 'とばれる'),
        ('とぶ', VerbForm.CAUSATIVE, False, False, 'とばせる'),
        ('とぶ', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, False, 'とばせられる'),

        ('とぶ', VerbForm.PRESENT, True, False, 'とばない'),
        ('とぶ', VerbForm.PAST, True, False, 'とばなかった'),
        ('とぶ', VerbForm.PRESUMPTIVE, True, False, 'とばないだろう'),
        ('とぶ', VerbForm.CONDITIONAL_RA, True, False, 'とばなかったら'),
        ('とぶ', VerbForm.POTENTIAL, True, False, 'とべない'),
        ('とぶ', VerbForm.PASSIVE, True, False, 'とばれない'),
        ('とぶ', VerbForm.CAUSATIVE, True, False, 'とばせない'),
        ('とぶ', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, False, 'とばせられない'),

        ('とぶ', VerbForm.PRESENT, False, True, 'とびます'),
        ('とぶ', VerbForm.PAST, False, True, 'とびました'),
        ('とぶ', VerbForm.PRESUMPTIVE, False, True, 'とぶでしょう'),
        ('とぶ', VerbForm.CONDITIONAL_RA, False, True, 'とびましたら'),
        ('とぶ', VerbForm.POTENTIAL, False, True, 'とべます'),
        ('とぶ', VerbForm.PASSIVE, False, True, 'とばれます'),
        ('とぶ', VerbForm.CAUSATIVE, False, True, 'とばせます'),
        ('とぶ', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, True, 'とばせられます'),

        ('とぶ', VerbForm.PRESENT, True, True, 'とびません'),
        ('とぶ', VerbForm.PAST, True, True, 'とびませんでした'),
        ('とぶ', VerbForm.PRESUMPTIVE, True, True, 'とばないでしょう'),
        ('とぶ', VerbForm.CONDITIONAL_RA, True, True, 'とびませんでしたら'),
        ('とぶ', VerbForm.POTENTIAL, True, True, 'とべません'),
        ('とぶ', VerbForm.PASSIVE, True, True, 'とばれません'),
        ('とぶ', VerbForm.CAUSATIVE, True, True, 'とばせません'),
        ('とぶ', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, True, 'とばせられません'),
    ]
)
def test_godan_bu_1(verb, tense, negative, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('とぶ', VerbForm.IMPERATIVE, False, 'とべ'),
        ('とぶ', VerbForm.IMPERATIVE, True, 'とぶな'),
        ('とぶ', VerbForm.TE_FORM, False, 'とんで'),
        ('とぶ', VerbForm.TE_FORM, True, 'とばなくて'),
        ('とぶ', VerbForm.CONDITIONAL_EBA, False, 'とべば'),
        ('とぶ', VerbForm.CONDITIONAL_EBA, True, 'とばなければ'),
    ]
)
def test_godan_bu_2(verb, tense, negative, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('とぶ', VerbForm.VOLITIONAL, False, 'とぼう'),
        ('とぶ', VerbForm.VOLITIONAL, True, 'とびましょう'),
    ]
)
def test_godan_bu_3(verb, tense, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings
