import pytest
from mikan import GodanVerb, VerbForm

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('まつ', VerbForm.PRESENT, False, False, 'まつ'),
        ('まつ', VerbForm.PAST, False, False, 'まった'),
        ('まつ', VerbForm.PRESUMPTIVE, False, False, 'まつだろう'),
        ('まつ', VerbForm.CONDITIONAL_RA, False, False, 'まったら'),
        ('まつ', VerbForm.POTENTIAL, False, False, 'まてる'),
        ('まつ', VerbForm.PASSIVE, False, False, 'またれる'),
        ('まつ', VerbForm.CAUSATIVE, False, False, 'またせる'),
        ('まつ', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, False, 'またせられる'),

        ('まつ', VerbForm.PRESENT, True, False, 'またない'),
        ('まつ', VerbForm.PAST, True, False, 'またなかった'),
        ('まつ', VerbForm.PRESUMPTIVE, True, False, 'またないだろう'),
        ('まつ', VerbForm.CONDITIONAL_RA, True, False, 'またなかったら'),
        ('まつ', VerbForm.POTENTIAL, True, False, 'まてない'),
        ('まつ', VerbForm.PASSIVE, True, False, 'またれない'),
        ('まつ', VerbForm.CAUSATIVE, True, False, 'またせない'),
        ('まつ', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, False, 'またせられない'),

        ('まつ', VerbForm.PRESENT, False, True, 'まちます'),
        ('まつ', VerbForm.PAST, False, True, 'まちました'),
        ('まつ', VerbForm.PRESUMPTIVE, False, True, 'まつでしょう'),
        ('まつ', VerbForm.CONDITIONAL_RA, False, True, 'まちましたら'),
        ('まつ', VerbForm.POTENTIAL, False, True, 'まてます'),
        ('まつ', VerbForm.PASSIVE, False, True, 'またれます'),
        ('まつ', VerbForm.CAUSATIVE, False, True, 'またせます'),
        ('まつ', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, True, 'またせられます'),

        ('まつ', VerbForm.PRESENT, True, True, 'まちません'),
        ('まつ', VerbForm.PAST, True, True, 'まちませんでした'),
        ('まつ', VerbForm.PRESUMPTIVE, True, True, 'またないでしょう'),
        ('まつ', VerbForm.CONDITIONAL_RA, True, True, 'まちませんでしたら'),
        ('まつ', VerbForm.POTENTIAL, True, True, 'まてません'),
        ('まつ', VerbForm.PASSIVE, True, True, 'またれません'),
        ('まつ', VerbForm.CAUSATIVE, True, True, 'またせません'),
        ('まつ', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, True, 'またせられません'),
    ]
)
def test_godan_tsu_1(verb, tense, negative, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('まつ', VerbForm.IMPERATIVE, False, 'まて'),
        ('まつ', VerbForm.IMPERATIVE, True, 'まつな'),
        ('まつ', VerbForm.TE_FORM, False, 'まって'),
        ('まつ', VerbForm.TE_FORM, True, 'またなくて'),
        ('まつ', VerbForm.CONDITIONAL_EBA, False, 'まてば'),
        ('まつ', VerbForm.CONDITIONAL_EBA, True, 'またなければ'),
    ]
)
def test_godan_tsu_2(verb, tense, negative, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('まつ', VerbForm.VOLITIONAL, False, 'まとう'),
        ('まつ', VerbForm.VOLITIONAL, True, 'まちましょう'),
    ]
)
def test_godan_tsu_3(verb, tense, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings
