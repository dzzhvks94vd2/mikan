import pytest
from mikan import GodanVerb, Form

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('およぐ', Form.PRESENT, False, False, 'およぐ'),
        ('およぐ', Form.PAST, False, False, 'およいだ'),
        ('およぐ', Form.PRESUMPTIVE, False, False, 'およぐだろう'),
        ('およぐ', Form.CONDITIONAL_RA, False, False, 'およいだら'),
        ('およぐ', Form.POTENTIAL, False, False, 'およげる'),
        ('およぐ', Form.PASSIVE, False, False, 'およがれる'),
        ('およぐ', Form.CAUSATIVE, False, False, 'およがせる'),
        ('およぐ', (Form.CAUSATIVE, Form.PASSIVE), False, False, 'およがせられる'),

        ('およぐ', Form.PRESENT, True, False, 'およがない'),
        ('およぐ', Form.PAST, True, False, 'およがなかった'),
        ('およぐ', Form.PRESUMPTIVE, True, False, 'およがないだろう'),
        ('およぐ', Form.CONDITIONAL_RA, True, False, 'およがなかったら'),
        ('およぐ', Form.POTENTIAL, True, False, 'およげない'),
        ('およぐ', Form.PASSIVE, True, False, 'およがれない'),
        ('およぐ', Form.CAUSATIVE, True, False, 'およがせない'),
        ('およぐ', (Form.CAUSATIVE, Form.PASSIVE), True, False, 'およがせられない'),

        ('およぐ', Form.PRESENT, False, True, 'およぎます'),
        ('およぐ', Form.PAST, False, True, 'およぎました'),
        ('およぐ', Form.PRESUMPTIVE, False, True, 'およぐでしょう'),
        ('およぐ', Form.CONDITIONAL_RA, False, True, 'およぎましたら'),
        ('およぐ', Form.POTENTIAL, False, True, 'およげます'),
        ('およぐ', Form.PASSIVE, False, True, 'およがれます'),
        ('およぐ', Form.CAUSATIVE, False, True, 'およがせます'),
        ('およぐ', (Form.CAUSATIVE, Form.PASSIVE), False, True, 'およがせられます'),

        ('およぐ', Form.PRESENT, True, True, 'およぎません'),
        ('およぐ', Form.PAST, True, True, 'およぎませんでした'),
        ('およぐ', Form.PRESUMPTIVE, True, True, 'およがないでしょう'),
        ('およぐ', Form.CONDITIONAL_RA, True, True, 'およぎませんでしたら'),
        ('およぐ', Form.POTENTIAL, True, True, 'およげません'),
        ('およぐ', Form.PASSIVE, True, True, 'およがれません'),
        ('およぐ', Form.CAUSATIVE, True, True, 'およがせません'),
        ('およぐ', (Form.CAUSATIVE, Form.PASSIVE), True, True, 'およがせられません'),
    ]
)
def test_godan_gu_1(verb, tense, negative, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('およぐ', Form.IMPERATIVE, False, 'およげ'),
        ('およぐ', Form.IMPERATIVE, True, 'およぐな'),
        ('およぐ', Form.TE, False, 'およいで'),
        ('およぐ', Form.TE, True, 'およがなくて'),
        ('およぐ', Form.CONDITIONAL_EBA, False, 'およげば'),
        ('およぐ', Form.CONDITIONAL_EBA, True, 'およがなければ'),
    ]
)
def test_godan_gu_2(verb, tense, negative, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('およぐ', Form.VOLITIONAL, False, 'およごう'),
        ('およぐ', Form.VOLITIONAL, True, 'およぎましょう'),
    ]
)
def test_godan_gu_3(verb, tense, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings
