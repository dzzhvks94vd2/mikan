import pytest
from mikan import GodanVerb, VerbForm

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('きる', VerbForm.PRESENT, False, False, 'きる'),
        ('きる', VerbForm.PAST, False, False, 'きった'),
        ('きる', VerbForm.PRESUMPTIVE, False, False, 'きるだろう'),
        ('きる', VerbForm.CONDITIONAL_RA, False, False, 'きったら'),
        ('きる', VerbForm.POTENTIAL, False, False, 'きれる'),
        ('きる', VerbForm.PASSIVE, False, False, 'きられる'),
        ('きる', VerbForm.CAUSATIVE, False, False, 'きらせる'),
        ('きる', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, False, 'きらせられる'),

        ('きる', VerbForm.PRESENT, True, False, 'きらない'),
        ('きる', VerbForm.PAST, True, False, 'きらなかった'),
        ('きる', VerbForm.PRESUMPTIVE, True, False, 'きらないだろう'),
        ('きる', VerbForm.CONDITIONAL_RA, True, False, 'きらなかったら'),
        ('きる', VerbForm.POTENTIAL, True, False, 'きれない'),
        ('きる', VerbForm.PASSIVE, True, False, 'きられない'),
        ('きる', VerbForm.CAUSATIVE, True, False, 'きらせない'),
        ('きる', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, False, 'きらせられない'),

        ('きる', VerbForm.PRESENT, False, True, 'きります'),
        ('きる', VerbForm.PAST, False, True, 'きりました'),
        ('きる', VerbForm.PRESUMPTIVE, False, True, 'きるでしょう'),
        ('きる', VerbForm.CONDITIONAL_RA, False, True, 'きりましたら'),
        ('きる', VerbForm.POTENTIAL, False, True, 'きれます'),
        ('きる', VerbForm.PASSIVE, False, True, 'きられます'),
        ('きる', VerbForm.CAUSATIVE, False, True, 'きらせます'),
        ('きる', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, True, 'きらせられます'),

        ('きる', VerbForm.PRESENT, True, True, 'きりません'),
        ('きる', VerbForm.PAST, True, True, 'きりませんでした'),
        ('きる', VerbForm.PRESUMPTIVE, True, True, 'きらないでしょう'),
        ('きる', VerbForm.CONDITIONAL_RA, True, True, 'きりませんでしたら'),
        ('きる', VerbForm.POTENTIAL, True, True, 'きれません'),
        ('きる', VerbForm.PASSIVE, True, True, 'きられません'),
        ('きる', VerbForm.CAUSATIVE, True, True, 'きらせません'),
        ('きる', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, True, 'きらせられません'),
    ]
)
def test_godan_ru_1(verb, tense, negative, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('きる', VerbForm.IMPERATIVE, False, 'きれ'),
        ('きる', VerbForm.IMPERATIVE, True, 'きるな'),
        ('きる', VerbForm.TE_FORM, False, 'きって'),
        ('きる', VerbForm.TE_FORM, True, 'きらなくて'),
        ('きる', VerbForm.CONDITIONAL_EBA, False, 'きれば'),
        ('きる', VerbForm.CONDITIONAL_EBA, True, 'きらなければ'),
    ]
)
def test_godan_ru_2(verb, tense, negative, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('きる', VerbForm.VOLITIONAL, False, 'きろう'),
        ('きる', VerbForm.VOLITIONAL, True, 'きりましょう'),
    ]
)
def test_godan_ru_3(verb, tense, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings
