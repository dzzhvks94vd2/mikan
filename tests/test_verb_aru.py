import pytest
from mikan import AruVerb, VerbForm

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('ある', VerbForm.PRESENT, False, False, 'ある'),
        ('ある', VerbForm.PAST, False, False, 'あった'),
        ('ある', VerbForm.PRESUMPTIVE, False, False, 'あるだろう'),
        ('ある', VerbForm.CONDITIONAL_RA, False, False, 'あったら'),
        ('ある', VerbForm.POTENTIAL, False, False, 'あれる'),
        ('ある', VerbForm.PASSIVE, False, False, 'あられる'),
        ('ある', VerbForm.CAUSATIVE, False, False, 'あらせる'),
        ('ある', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, False, 'あらせられる'),

        ('ある', VerbForm.PRESENT, True, False, 'ない'),
        ('ある', VerbForm.PAST, True, False, 'なかった'),
        ('ある', VerbForm.PRESUMPTIVE, True, False, 'ないだろう'),
        ('ある', VerbForm.CONDITIONAL_RA, True, False, 'なかったら'),
        ('ある', VerbForm.POTENTIAL, True, False, 'あれない'),
        ('ある', VerbForm.PASSIVE, True, False, 'あられない'),
        ('ある', VerbForm.CAUSATIVE, True, False, 'あらせない'),
        ('ある', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, False, 'あらせられない'),

        ('ある', VerbForm.PRESENT, False, True, 'あります'),
        ('ある', VerbForm.PAST, False, True, 'ありました'),
        ('ある', VerbForm.PRESUMPTIVE, False, True, 'あるでしょう'),
        ('ある', VerbForm.CONDITIONAL_RA, False, True, 'ありましたら'),
        ('ある', VerbForm.POTENTIAL, False, True, 'あれます'),
        ('ある', VerbForm.PASSIVE, False, True, 'あられます'),
        ('ある', VerbForm.CAUSATIVE, False, True, 'あらせます'),
        ('ある', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, True, 'あらせられます'),

        ('ある', VerbForm.PRESENT, True, True, 'ありません'),
        ('ある', VerbForm.PAST, True, True, 'ありませんでした'),
        ('ある', VerbForm.PRESUMPTIVE, True, True, 'ないでしょう'),
        ('ある', VerbForm.CONDITIONAL_RA, True, True, 'ありませんでしたら'),
        ('ある', VerbForm.POTENTIAL, True, True, 'あれません'),
        ('ある', VerbForm.PASSIVE, True, True, 'あられません'),
        ('ある', VerbForm.CAUSATIVE, True, True, 'あらせません'),
        ('ある', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, True, 'あらせられません'),
    ]
)
def test_aru_1(verb, tense, negative, polite, expected):

    v = AruVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('ある', VerbForm.IMPERATIVE, False, 'あれ'),
        ('ある', VerbForm.IMPERATIVE, True, 'あるな'),
        ('ある', VerbForm.TE_FORM, False, 'あって'),
        ('ある', VerbForm.TE_FORM, True, 'なくて'),
        ('ある', VerbForm.CONDITIONAL_EBA, False, 'あれば'),
        ('ある', VerbForm.CONDITIONAL_EBA, True, 'なければ'),
    ]
)
def test_aru_2(verb, tense, negative, expected):

    v = AruVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('ある', VerbForm.VOLITIONAL, False, 'あろう'),
        ('ある', VerbForm.VOLITIONAL, True, 'ありましょう'),
    ]
)
def test_aru_3(verb, tense, polite, expected):

    v = AruVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings
