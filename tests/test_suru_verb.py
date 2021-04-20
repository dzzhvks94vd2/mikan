import pytest
from mikan import SuruVerb, VerbForm

@pytest.mark.parametrize(
    "tense,negative,polite,expected",
    [
        (VerbForm.PRESENT, False, False, 'する'),
        (VerbForm.PAST, False, False, 'した'),
        (VerbForm.PRESUMPTIVE, False, False, 'するだろう'),
        (VerbForm.CONDITIONAL_RA, False, False, 'したら'),
        (VerbForm.POTENTIAL, False, False, 'できる'),
        (VerbForm.PASSIVE, False, False, 'される'),
        (VerbForm.CAUSATIVE, False, False, 'させる'),
        ((VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, False, 'させられる'),

        (VerbForm.PRESENT, True, False, 'しない'),
        (VerbForm.PAST, True, False, 'しなかった'),
        (VerbForm.PRESUMPTIVE, True, False, 'しないだろう'),
        (VerbForm.CONDITIONAL_RA, True, False, 'しなかったら'),
        (VerbForm.POTENTIAL, True, False, 'できない'),
        (VerbForm.PASSIVE, True, False, 'されない'),
        (VerbForm.CAUSATIVE, True, False, 'させない'),
        ((VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, False, 'させられない'),

        (VerbForm.PRESENT, False, True, 'します'),
        (VerbForm.PAST, False, True, 'しました'),
        (VerbForm.PRESUMPTIVE, False, True, 'するでしょう'),
        (VerbForm.CONDITIONAL_RA, False, True, 'しましたら'),
        (VerbForm.POTENTIAL, False, True, 'できます'),
        (VerbForm.PASSIVE, False, True, 'されます'),
        (VerbForm.CAUSATIVE, False, True, 'させます'),
        ((VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, True, 'させられます'),

        (VerbForm.PRESENT, True, True, 'しません'),
        (VerbForm.PAST, True, True, 'しませんでした'),
        (VerbForm.PRESUMPTIVE, True, True, 'しないでしょう'),
        (VerbForm.CONDITIONAL_RA, True, True, 'しませんでしたら'),
        (VerbForm.POTENTIAL, True, True, 'できません'),
        (VerbForm.PASSIVE, True, True, 'されません'),
        (VerbForm.CAUSATIVE, True, True, 'させません'),
        ((VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, True, 'させられません'),
    ]
)
def test_suru_1(tense, negative, polite, expected):

    v = SuruVerb()

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "tense,negative,expected",
    [
        (VerbForm.IMPERATIVE, False, 'しろ'),
        (VerbForm.IMPERATIVE, True, 'するな'),
        (VerbForm.TE_FORM, False, 'して'),
        (VerbForm.TE_FORM, True, 'しなくて'),
        (VerbForm.CONDITIONAL_EBA, False, 'すれば'),
        (VerbForm.CONDITIONAL_EBA, True, 'しなければ'),
    ]
)
def test_suru_2(tense, negative, expected):

    v = SuruVerb()

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "tense,polite,expected",
    [
        (VerbForm.VOLITIONAL, False, 'しよう'),
        (VerbForm.VOLITIONAL, True, 'しましょう'),
    ]
)
def test_suru_3(tense, polite, expected):

    v = SuruVerb()

    assert expected in v.conjugate(tense, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('勉強', VerbForm.PRESENT, False, True, '勉強します'),
    ]
)
def test_suru_4(verb, tense, negative, polite, expected):

    v = SuruVerb(verb)
    assert expected in v.conjugate(tense, negative=negative, polite=polite).writings
