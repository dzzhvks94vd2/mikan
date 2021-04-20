import pytest
from mikan import GodanVerb, VerbForm

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('およぐ', VerbForm.PRESENT, False, False, 'およぐ'),
        ('およぐ', VerbForm.PAST, False, False, 'およいだ'),
        ('およぐ', VerbForm.PRESUMPTIVE, False, False, 'およぐだろう'),
        ('およぐ', VerbForm.CONDITIONAL_RA, False, False, 'およいだら'),
        ('およぐ', VerbForm.POTENTIAL, False, False, 'およげる'),
        ('およぐ', VerbForm.PASSIVE, False, False, 'およがれる'),
        ('およぐ', VerbForm.CAUSATIVE, False, False, 'およがせる'),
        ('およぐ', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, False, 'およがせられる'),

        ('およぐ', VerbForm.PRESENT, True, False, 'およがない'),
        ('およぐ', VerbForm.PAST, True, False, 'およがなかった'),
        ('およぐ', VerbForm.PRESUMPTIVE, True, False, 'およがないだろう'),
        ('およぐ', VerbForm.CONDITIONAL_RA, True, False, 'およがなかったら'),
        ('およぐ', VerbForm.POTENTIAL, True, False, 'およげない'),
        ('およぐ', VerbForm.PASSIVE, True, False, 'およがれない'),
        ('およぐ', VerbForm.CAUSATIVE, True, False, 'およがせない'),
        ('およぐ', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, False, 'およがせられない'),

        ('およぐ', VerbForm.PRESENT, False, True, 'およぎます'),
        ('およぐ', VerbForm.PAST, False, True, 'およぎました'),
        ('およぐ', VerbForm.PRESUMPTIVE, False, True, 'およぐでしょう'),
        ('およぐ', VerbForm.CONDITIONAL_RA, False, True, 'およぎましたら'),
        ('およぐ', VerbForm.POTENTIAL, False, True, 'およげます'),
        ('およぐ', VerbForm.PASSIVE, False, True, 'およがれます'),
        ('およぐ', VerbForm.CAUSATIVE, False, True, 'およがせます'),
        ('およぐ', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, True, 'およがせられます'),

        ('およぐ', VerbForm.PRESENT, True, True, 'およぎません'),
        ('およぐ', VerbForm.PAST, True, True, 'およぎませんでした'),
        ('およぐ', VerbForm.PRESUMPTIVE, True, True, 'およがないでしょう'),
        ('およぐ', VerbForm.CONDITIONAL_RA, True, True, 'およぎませんでしたら'),
        ('およぐ', VerbForm.POTENTIAL, True, True, 'およげません'),
        ('およぐ', VerbForm.PASSIVE, True, True, 'およがれません'),
        ('およぐ', VerbForm.CAUSATIVE, True, True, 'およがせません'),
        ('およぐ', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, True, 'およがせられません'),
    ]
)
def test_godan_gu_1(verb, tense, negative, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('およぐ', VerbForm.IMPERATIVE, False, 'およげ'),
        ('およぐ', VerbForm.IMPERATIVE, True, 'およぐな'),
        ('およぐ', VerbForm.TE_FORM, False, 'およいで'),
        ('およぐ', VerbForm.TE_FORM, True, 'およがなくて'),
        ('およぐ', VerbForm.CONDITIONAL_EBA, False, 'およげば'),
        ('およぐ', VerbForm.CONDITIONAL_EBA, True, 'およがなければ'),
    ]
)
def test_godan_gu_2(verb, tense, negative, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('およぐ', VerbForm.VOLITIONAL, False, 'およごう'),
        ('およぐ', VerbForm.VOLITIONAL, True, 'およぎましょう'),
    ]
)
def test_godan_gu_3(verb, tense, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings
