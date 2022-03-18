import pytest
from mikan import AruVerb, Form

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('ある', Form.PRESENT, False, False, 'ある'),
        ('ある', Form.PAST, False, False, 'あった'),
        ('ある', Form.PRESUMPTIVE, False, False, 'あるだろう'),
        ('ある', Form.CONDITIONAL_RA, False, False, 'あったら'),
        ('ある', Form.POTENTIAL, False, False, 'あれる'),
        ('ある', Form.PASSIVE, False, False, 'あられる'),
        ('ある', Form.CAUSATIVE, False, False, 'あらせる'),
        ('ある', (Form.CAUSATIVE, Form.PASSIVE), False, False, 'あらせられる'),

        ('ある', Form.PRESENT, True, False, 'ない'),
        ('ある', Form.PAST, True, False, 'なかった'),
        ('ある', Form.PRESUMPTIVE, True, False, 'ないだろう'),
        ('ある', Form.CONDITIONAL_RA, True, False, 'なかったら'),
        ('ある', Form.POTENTIAL, True, False, 'あれない'),
        ('ある', Form.PASSIVE, True, False, 'あられない'),
        ('ある', Form.CAUSATIVE, True, False, 'あらせない'),
        ('ある', (Form.CAUSATIVE, Form.PASSIVE), True, False, 'あらせられない'),

        ('ある', Form.PRESENT, False, True, 'あります'),
        ('ある', Form.PAST, False, True, 'ありました'),
        ('ある', Form.PRESUMPTIVE, False, True, 'あるでしょう'),
        ('ある', Form.CONDITIONAL_RA, False, True, 'ありましたら'),
        ('ある', Form.POTENTIAL, False, True, 'あれます'),
        ('ある', Form.PASSIVE, False, True, 'あられます'),
        ('ある', Form.CAUSATIVE, False, True, 'あらせます'),
        ('ある', (Form.CAUSATIVE, Form.PASSIVE), False, True, 'あらせられます'),

        ('ある', Form.PRESENT, True, True, 'ありません'),
        ('ある', Form.PAST, True, True, 'ありませんでした'),
        ('ある', Form.PRESUMPTIVE, True, True, 'ないでしょう'),
        ('ある', Form.CONDITIONAL_RA, True, True, 'ありませんでしたら'),
        ('ある', Form.POTENTIAL, True, True, 'あれません'),
        ('ある', Form.PASSIVE, True, True, 'あられません'),
        ('ある', Form.CAUSATIVE, True, True, 'あらせません'),
        ('ある', (Form.CAUSATIVE, Form.PASSIVE), True, True, 'あらせられません'),
    ]
)
def test_aru_1(verb, tense, negative, polite, expected):

    v = AruVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('ある', Form.IMPERATIVE, False, 'あれ'),
        ('ある', Form.IMPERATIVE, True, 'あるな'),
        ('ある', Form.TE, False, 'あって'),
        ('ある', Form.TE, True, 'なくて'),
        ('ある', Form.CONDITIONAL_EBA, False, 'あれば'),
        ('ある', Form.CONDITIONAL_EBA, True, 'なければ'),
    ]
)
def test_aru_2(verb, tense, negative, expected):

    v = AruVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('ある', Form.VOLITIONAL, False, 'あろう'),
        ('ある', Form.VOLITIONAL, True, 'ありましょう'),
    ]
)
def test_aru_3(verb, tense, polite, expected):

    v = AruVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings
