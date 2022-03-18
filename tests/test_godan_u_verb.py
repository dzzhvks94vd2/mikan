import pytest
from mikan import GodanVerb, Form

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('あう', Form.PRESENT, False, False, 'あう'),
        ('あう', Form.PAST, False, False, 'あった'),
        ('あう', Form.PRESUMPTIVE, False, False, 'あうだろう'),
        ('あう', Form.CONDITIONAL_RA, False, False, 'あったら'),
        ('あう', Form.POTENTIAL, False, False, 'あえる'),
        ('あう', Form.PASSIVE, False, False, 'あわれる'),
        ('あう', Form.CAUSATIVE, False, False, 'あわせる'),
        ('あう', (Form.CAUSATIVE, Form.PASSIVE), False, False, 'あわせられる'),

        ('あう', Form.PRESENT, True, False, 'あわない'),
        ('あう', Form.PAST, True, False, 'あわなかった'),
        ('あう', Form.PRESUMPTIVE, True, False, 'あわないだろう'),
        ('あう', Form.CONDITIONAL_RA, True, False, 'あわなかったら'),
        ('あう', Form.POTENTIAL, True, False, 'あえない'),
        ('あう', Form.PASSIVE, True, False, 'あわれない'),
        ('あう', Form.CAUSATIVE, True, False, 'あわせない'),
        ('あう', (Form.CAUSATIVE, Form.PASSIVE), True, False, 'あわせられない'),

        ('あう', Form.PRESENT, False, True, 'あいます'),
        ('あう', Form.PAST, False, True, 'あいました'),
        ('あう', Form.PRESUMPTIVE, False, True, 'あうでしょう'),
        ('あう', Form.CONDITIONAL_RA, False, True, 'あいましたら'),
        ('あう', Form.POTENTIAL, False, True, 'あえます'),
        ('あう', Form.PASSIVE, False, True, 'あわれます'),
        ('あう', Form.CAUSATIVE, False, True, 'あわせます'),
        ('あう', (Form.CAUSATIVE, Form.PASSIVE), False, True, 'あわせられます'),

        ('あう', Form.PRESENT, True, True, 'あいません'),
        ('あう', Form.PAST, True, True, 'あいませんでした'),
        ('あう', Form.PRESUMPTIVE, True, True, 'あわないでしょう'),
        ('あう', Form.CONDITIONAL_RA, True, True, 'あいませんでしたら'),
        ('あう', Form.POTENTIAL, True, True, 'あえません'),
        ('あう', Form.PASSIVE, True, True, 'あわれません'),
        ('あう', Form.CAUSATIVE, True, True, 'あわせません'),
        ('あう', (Form.CAUSATIVE, Form.PASSIVE), True, True, 'あわせられません'),
    ]
)
def test_godan_u_1(verb, tense, negative, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('あう', Form.IMPERATIVE, False, 'あえ'),
        ('あう', Form.IMPERATIVE, True, 'あうな'),
        ('あう', Form.TE, False, 'あって'),
        ('あう', Form.TE, True, 'あわなくて'),
        ('あう', Form.CONDITIONAL_EBA, False, 'あえば'),
        ('あう', Form.CONDITIONAL_EBA, True, 'あわなければ'),
    ]
)
def test_godan_u_2(verb, tense, negative, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('あう', Form.VOLITIONAL, False, 'あおう'),
        ('あう', Form.VOLITIONAL, True, 'あいましょう'),
    ]
)
def test_godan_u_3(verb, tense, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings
