import pytest
from mikan import GodanVerb, VerbForm

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('しぬ', VerbForm.PRESENT, False, False, 'しぬ'),
        ('しぬ', VerbForm.PAST, False, False, 'しんだ'),
        ('しぬ', VerbForm.PRESUMPTIVE, False, False, 'しぬだろう'),
        ('しぬ', VerbForm.CONDITIONAL_RA, False, False, 'しんだら'),
        ('しぬ', VerbForm.POTENTIAL, False, False, 'しねる'),
        ('しぬ', VerbForm.PASSIVE, False, False, 'しなれる'),
        ('しぬ', VerbForm.CAUSATIVE, False, False, 'しなせる'),
        ('しぬ', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, False, 'しなせられる'),

        ('しぬ', VerbForm.PRESENT, True, False, 'しなない'),
        ('しぬ', VerbForm.PAST, True, False, 'しななかった'),
        ('しぬ', VerbForm.PRESUMPTIVE, True, False, 'しなないだろう'),
        ('しぬ', VerbForm.CONDITIONAL_RA, True, False, 'しななかったら'),
        ('しぬ', VerbForm.POTENTIAL, True, False, 'しねない'),
        ('しぬ', VerbForm.PASSIVE, True, False, 'しなれない'),
        ('しぬ', VerbForm.CAUSATIVE, True, False, 'しなせない'),
        ('しぬ', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, False, 'しなせられない'),

        ('しぬ', VerbForm.PRESENT, False, True, 'しにます'),
        ('しぬ', VerbForm.PAST, False, True, 'しにました'),
        ('しぬ', VerbForm.PRESUMPTIVE, False, True, 'しぬでしょう'),
        ('しぬ', VerbForm.CONDITIONAL_RA, False, True, 'しにましたら'),
        ('しぬ', VerbForm.POTENTIAL, False, True, 'しねます'),
        ('しぬ', VerbForm.PASSIVE, False, True, 'しなれます'),
        ('しぬ', VerbForm.CAUSATIVE, False, True, 'しなせます'),
        ('しぬ', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, True, 'しなせられます'),

        ('しぬ', VerbForm.PRESENT, True, True, 'しにません'),
        ('しぬ', VerbForm.PAST, True, True, 'しにませんでした'),
        ('しぬ', VerbForm.PRESUMPTIVE, True, True, 'しなないでしょう'),
        ('しぬ', VerbForm.CONDITIONAL_RA, True, True, 'しにませんでしたら'),
        ('しぬ', VerbForm.POTENTIAL, True, True, 'しねません'),
        ('しぬ', VerbForm.PASSIVE, True, True, 'しなれません'),
        ('しぬ', VerbForm.CAUSATIVE, True, True, 'しなせません'),
        ('しぬ', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, True, 'しなせられません'),
    ]
)
def test_godan_nu_1(verb, tense, negative, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('しぬ', VerbForm.IMPERATIVE, False, 'しね'),
        ('しぬ', VerbForm.IMPERATIVE, True, 'しぬな'),
        ('しぬ', VerbForm.TE_FORM, False, 'しんで'),
        ('しぬ', VerbForm.TE_FORM, True, 'しななくて'),
        ('しぬ', VerbForm.CONDITIONAL_EBA, False, 'しねば'),
        ('しぬ', VerbForm.CONDITIONAL_EBA, True, 'しななければ'),
    ]
)
def test_godan_nu_2(verb, tense, negative, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('しぬ', VerbForm.VOLITIONAL, False, 'しのう'),
        ('しぬ', VerbForm.VOLITIONAL, True, 'しにましょう'),
    ]
)
def test_godan_nu_3(verb, tense, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings
