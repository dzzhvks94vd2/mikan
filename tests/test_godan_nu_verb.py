import pytest
from mikan import GodanVerb, Form

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('しぬ', Form.PRESENT, False, False, 'しぬ'),
        ('しぬ', Form.PAST, False, False, 'しんだ'),
        ('しぬ', Form.PRESUMPTIVE, False, False, 'しぬだろう'),
        ('しぬ', Form.CONDITIONAL_RA, False, False, 'しんだら'),
        ('しぬ', Form.POTENTIAL, False, False, 'しねる'),
        ('しぬ', Form.PASSIVE, False, False, 'しなれる'),
        ('しぬ', Form.CAUSATIVE, False, False, 'しなせる'),
        ('しぬ', (Form.CAUSATIVE, Form.PASSIVE), False, False, 'しなせられる'),

        ('しぬ', Form.PRESENT, True, False, 'しなない'),
        ('しぬ', Form.PAST, True, False, 'しななかった'),
        ('しぬ', Form.PRESUMPTIVE, True, False, 'しなないだろう'),
        ('しぬ', Form.CONDITIONAL_RA, True, False, 'しななかったら'),
        ('しぬ', Form.POTENTIAL, True, False, 'しねない'),
        ('しぬ', Form.PASSIVE, True, False, 'しなれない'),
        ('しぬ', Form.CAUSATIVE, True, False, 'しなせない'),
        ('しぬ', (Form.CAUSATIVE, Form.PASSIVE), True, False, 'しなせられない'),

        ('しぬ', Form.PRESENT, False, True, 'しにます'),
        ('しぬ', Form.PAST, False, True, 'しにました'),
        ('しぬ', Form.PRESUMPTIVE, False, True, 'しぬでしょう'),
        ('しぬ', Form.CONDITIONAL_RA, False, True, 'しにましたら'),
        ('しぬ', Form.POTENTIAL, False, True, 'しねます'),
        ('しぬ', Form.PASSIVE, False, True, 'しなれます'),
        ('しぬ', Form.CAUSATIVE, False, True, 'しなせます'),
        ('しぬ', (Form.CAUSATIVE, Form.PASSIVE), False, True, 'しなせられます'),

        ('しぬ', Form.PRESENT, True, True, 'しにません'),
        ('しぬ', Form.PAST, True, True, 'しにませんでした'),
        ('しぬ', Form.PRESUMPTIVE, True, True, 'しなないでしょう'),
        ('しぬ', Form.CONDITIONAL_RA, True, True, 'しにませんでしたら'),
        ('しぬ', Form.POTENTIAL, True, True, 'しねません'),
        ('しぬ', Form.PASSIVE, True, True, 'しなれません'),
        ('しぬ', Form.CAUSATIVE, True, True, 'しなせません'),
        ('しぬ', (Form.CAUSATIVE, Form.PASSIVE), True, True, 'しなせられません'),
    ]
)
def test_godan_nu_1(verb, tense, negative, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('しぬ', Form.IMPERATIVE, False, 'しね'),
        ('しぬ', Form.IMPERATIVE, True, 'しぬな'),
        ('しぬ', Form.TE, False, 'しんで'),
        ('しぬ', Form.TE, True, 'しななくて'),
        ('しぬ', Form.CONDITIONAL_EBA, False, 'しねば'),
        ('しぬ', Form.CONDITIONAL_EBA, True, 'しななければ'),
    ]
)
def test_godan_nu_2(verb, tense, negative, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('しぬ', Form.VOLITIONAL, False, 'しのう'),
        ('しぬ', Form.VOLITIONAL, True, 'しにましょう'),
    ]
)
def test_godan_nu_3(verb, tense, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings
