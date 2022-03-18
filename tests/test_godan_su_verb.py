import pytest
from mikan import GodanVerb, Form

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('かす', Form.PRESENT, False, False, 'かす'),
        ('かす', Form.PAST, False, False, 'かした'),
        ('かす', Form.PRESUMPTIVE, False, False, 'かすだろう'),
        ('かす', Form.CONDITIONAL_RA, False, False, 'かしたら'),
        ('かす', Form.POTENTIAL, False, False, 'かせる'),
        ('かす', Form.PASSIVE, False, False, 'かされる'),
        ('かす', Form.CAUSATIVE, False, False, 'かさせる'),
        ('かす', (Form.CAUSATIVE, Form.PASSIVE), False, False, 'かさせられる'),

        ('かす', Form.PRESENT, True, False, 'かさない'),
        ('かす', Form.PAST, True, False, 'かさなかった'),
        ('かす', Form.PRESUMPTIVE, True, False, 'かさないだろう'),
        ('かす', Form.CONDITIONAL_RA, True, False, 'かさなかったら'),
        ('かす', Form.POTENTIAL, True, False, 'かせない'),
        ('かす', Form.PASSIVE, True, False, 'かされない'),
        ('かす', Form.CAUSATIVE, True, False, 'かさせない'),
        ('かす', (Form.CAUSATIVE, Form.PASSIVE), True, False, 'かさせられない'),

        ('かす', Form.PRESENT, False, True, 'かします'),
        ('かす', Form.PAST, False, True, 'かしました'),
        ('かす', Form.PRESUMPTIVE, False, True, 'かすでしょう'),
        ('かす', Form.CONDITIONAL_RA, False, True, 'かしましたら'),
        ('かす', Form.POTENTIAL, False, True, 'かせます'),
        ('かす', Form.PASSIVE, False, True, 'かされます'),
        ('かす', Form.CAUSATIVE, False, True, 'かさせます'),
        ('かす', (Form.CAUSATIVE, Form.PASSIVE), False, True, 'かさせられます'),

        ('かす', Form.PRESENT, True, True, 'かしません'),
        ('かす', Form.PAST, True, True, 'かしませんでした'),
        ('かす', Form.PRESUMPTIVE, True, True, 'かさないでしょう'),
        ('かす', Form.CONDITIONAL_RA, True, True, 'かしませんでしたら'),
        ('かす', Form.POTENTIAL, True, True, 'かせません'),
        ('かす', Form.PASSIVE, True, True, 'かされません'),
        ('かす', Form.CAUSATIVE, True, True, 'かさせません'),
        ('かす', (Form.CAUSATIVE, Form.PASSIVE), True, True, 'かさせられません'),
    ]
)
def test_godan_su_1(verb, tense, negative, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('かす', Form.IMPERATIVE, False, 'かせ'),
        ('かす', Form.IMPERATIVE, True, 'かすな'),
        ('かす', Form.TE, False, 'かして'),
        ('かす', Form.TE, True, 'かさなくて'),
        ('かす', Form.CONDITIONAL_EBA, False, 'かせば'),
        ('かす', Form.CONDITIONAL_EBA, True, 'かさなければ'),
    ]
)
def test_godan_su_2(verb, tense, negative, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('かす', Form.VOLITIONAL, False, 'かそう'),
        ('かす', Form.VOLITIONAL, True, 'かしましょう'),
    ]
)
def test_godan_su_3(verb, tense, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings
