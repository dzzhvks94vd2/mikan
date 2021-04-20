import pytest
from mikan import GodanVerb, VerbForm

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('あう', VerbForm.PRESENT, False, False, 'あう'),
        ('あう', VerbForm.PAST, False, False, 'あった'),
        ('あう', VerbForm.PRESUMPTIVE, False, False, 'あうだろう'),
        ('あう', VerbForm.CONDITIONAL_RA, False, False, 'あったら'),
        ('あう', VerbForm.POTENTIAL, False, False, 'あえる'),
        ('あう', VerbForm.PASSIVE, False, False, 'あわれる'),
        ('あう', VerbForm.CAUSATIVE, False, False, 'あわせる'),
        ('あう', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, False, 'あわせられる'),

        ('あう', VerbForm.PRESENT, True, False, 'あわない'),
        ('あう', VerbForm.PAST, True, False, 'あわなかった'),
        ('あう', VerbForm.PRESUMPTIVE, True, False, 'あわないだろう'),
        ('あう', VerbForm.CONDITIONAL_RA, True, False, 'あわなかったら'),
        ('あう', VerbForm.POTENTIAL, True, False, 'あえない'),
        ('あう', VerbForm.PASSIVE, True, False, 'あわれない'),
        ('あう', VerbForm.CAUSATIVE, True, False, 'あわせない'),
        ('あう', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, False, 'あわせられない'),

        ('あう', VerbForm.PRESENT, False, True, 'あいます'),
        ('あう', VerbForm.PAST, False, True, 'あいました'),
        ('あう', VerbForm.PRESUMPTIVE, False, True, 'あうでしょう'),
        ('あう', VerbForm.CONDITIONAL_RA, False, True, 'あいましたら'),
        ('あう', VerbForm.POTENTIAL, False, True, 'あえます'),
        ('あう', VerbForm.PASSIVE, False, True, 'あわれます'),
        ('あう', VerbForm.CAUSATIVE, False, True, 'あわせます'),
        ('あう', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, True, 'あわせられます'),

        ('あう', VerbForm.PRESENT, True, True, 'あいません'),
        ('あう', VerbForm.PAST, True, True, 'あいませんでした'),
        ('あう', VerbForm.PRESUMPTIVE, True, True, 'あわないでしょう'),
        ('あう', VerbForm.CONDITIONAL_RA, True, True, 'あいませんでしたら'),
        ('あう', VerbForm.POTENTIAL, True, True, 'あえません'),
        ('あう', VerbForm.PASSIVE, True, True, 'あわれません'),
        ('あう', VerbForm.CAUSATIVE, True, True, 'あわせません'),
        ('あう', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, True, 'あわせられません'),
    ]
)
def test_godan_u_1(verb, tense, negative, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('あう', VerbForm.IMPERATIVE, False, 'あえ'),
        ('あう', VerbForm.IMPERATIVE, True, 'あうな'),
        ('あう', VerbForm.TE_FORM, False, 'あって'),
        ('あう', VerbForm.TE_FORM, True, 'あわなくて'),
        ('あう', VerbForm.CONDITIONAL_EBA, False, 'あえば'),
        ('あう', VerbForm.CONDITIONAL_EBA, True, 'あわなければ'),
    ]
)
def test_godan_u_2(verb, tense, negative, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('あう', VerbForm.VOLITIONAL, False, 'あおう'),
        ('あう', VerbForm.VOLITIONAL, True, 'あいましょう'),
    ]
)
def test_godan_u_3(verb, tense, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings
