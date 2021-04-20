import pytest
from mikan import GodanVerb, VerbForm

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('かす', VerbForm.PRESENT, False, False, 'かす'),
        ('かす', VerbForm.PAST, False, False, 'かした'),
        ('かす', VerbForm.PRESUMPTIVE, False, False, 'かすだろう'),
        ('かす', VerbForm.CONDITIONAL_RA, False, False, 'かしたら'),
        ('かす', VerbForm.POTENTIAL, False, False, 'かせる'),
        ('かす', VerbForm.PASSIVE, False, False, 'かされる'),
        ('かす', VerbForm.CAUSATIVE, False, False, 'かさせる'),
        ('かす', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, False, 'かさせられる'),

        ('かす', VerbForm.PRESENT, True, False, 'かさない'),
        ('かす', VerbForm.PAST, True, False, 'かさなかった'),
        ('かす', VerbForm.PRESUMPTIVE, True, False, 'かさないだろう'),
        ('かす', VerbForm.CONDITIONAL_RA, True, False, 'かさなかったら'),
        ('かす', VerbForm.POTENTIAL, True, False, 'かせない'),
        ('かす', VerbForm.PASSIVE, True, False, 'かされない'),
        ('かす', VerbForm.CAUSATIVE, True, False, 'かさせない'),
        ('かす', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, False, 'かさせられない'),

        ('かす', VerbForm.PRESENT, False, True, 'かします'),
        ('かす', VerbForm.PAST, False, True, 'かしました'),
        ('かす', VerbForm.PRESUMPTIVE, False, True, 'かすでしょう'),
        ('かす', VerbForm.CONDITIONAL_RA, False, True, 'かしましたら'),
        ('かす', VerbForm.POTENTIAL, False, True, 'かせます'),
        ('かす', VerbForm.PASSIVE, False, True, 'かされます'),
        ('かす', VerbForm.CAUSATIVE, False, True, 'かさせます'),
        ('かす', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, True, 'かさせられます'),

        ('かす', VerbForm.PRESENT, True, True, 'かしません'),
        ('かす', VerbForm.PAST, True, True, 'かしませんでした'),
        ('かす', VerbForm.PRESUMPTIVE, True, True, 'かさないでしょう'),
        ('かす', VerbForm.CONDITIONAL_RA, True, True, 'かしませんでしたら'),
        ('かす', VerbForm.POTENTIAL, True, True, 'かせません'),
        ('かす', VerbForm.PASSIVE, True, True, 'かされません'),
        ('かす', VerbForm.CAUSATIVE, True, True, 'かさせません'),
        ('かす', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, True, 'かさせられません'),
    ]
)
def test_godan_su_1(verb, tense, negative, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('かす', VerbForm.IMPERATIVE, False, 'かせ'),
        ('かす', VerbForm.IMPERATIVE, True, 'かすな'),
        ('かす', VerbForm.TE_FORM, False, 'かして'),
        ('かす', VerbForm.TE_FORM, True, 'かさなくて'),
        ('かす', VerbForm.CONDITIONAL_EBA, False, 'かせば'),
        ('かす', VerbForm.CONDITIONAL_EBA, True, 'かさなければ'),
    ]
)
def test_godan_su_2(verb, tense, negative, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('かす', VerbForm.VOLITIONAL, False, 'かそう'),
        ('かす', VerbForm.VOLITIONAL, True, 'かしましょう'),
    ]
)
def test_godan_su_3(verb, tense, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings
