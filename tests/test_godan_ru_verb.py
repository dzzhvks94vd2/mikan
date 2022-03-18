import pytest
from mikan import GodanVerb, Form

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('きる', Form.PRESENT, False, False, 'きる'),
        ('きる', Form.PAST, False, False, 'きった'),
        ('きる', Form.PRESUMPTIVE, False, False, 'きるだろう'),
        ('きる', Form.CONDITIONAL_RA, False, False, 'きったら'),
        ('きる', Form.POTENTIAL, False, False, 'きれる'),
        ('きる', Form.PASSIVE, False, False, 'きられる'),
        ('きる', Form.CAUSATIVE, False, False, 'きらせる'),
        ('きる', (Form.CAUSATIVE, Form.PASSIVE), False, False, 'きらせられる'),

        ('きる', Form.PRESENT, True, False, 'きらない'),
        ('きる', Form.PAST, True, False, 'きらなかった'),
        ('きる', Form.PRESUMPTIVE, True, False, 'きらないだろう'),
        ('きる', Form.CONDITIONAL_RA, True, False, 'きらなかったら'),
        ('きる', Form.POTENTIAL, True, False, 'きれない'),
        ('きる', Form.PASSIVE, True, False, 'きられない'),
        ('きる', Form.CAUSATIVE, True, False, 'きらせない'),
        ('きる', (Form.CAUSATIVE, Form.PASSIVE), True, False, 'きらせられない'),

        ('きる', Form.PRESENT, False, True, 'きります'),
        ('きる', Form.PAST, False, True, 'きりました'),
        ('きる', Form.PRESUMPTIVE, False, True, 'きるでしょう'),
        ('きる', Form.CONDITIONAL_RA, False, True, 'きりましたら'),
        ('きる', Form.POTENTIAL, False, True, 'きれます'),
        ('きる', Form.PASSIVE, False, True, 'きられます'),
        ('きる', Form.CAUSATIVE, False, True, 'きらせます'),
        ('きる', (Form.CAUSATIVE, Form.PASSIVE), False, True, 'きらせられます'),

        ('きる', Form.PRESENT, True, True, 'きりません'),
        ('きる', Form.PAST, True, True, 'きりませんでした'),
        ('きる', Form.PRESUMPTIVE, True, True, 'きらないでしょう'),
        ('きる', Form.CONDITIONAL_RA, True, True, 'きりませんでしたら'),
        ('きる', Form.POTENTIAL, True, True, 'きれません'),
        ('きる', Form.PASSIVE, True, True, 'きられません'),
        ('きる', Form.CAUSATIVE, True, True, 'きらせません'),
        ('きる', (Form.CAUSATIVE, Form.PASSIVE), True, True, 'きらせられません'),
    ]
)
def test_godan_ru_1(verb, tense, negative, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('きる', Form.IMPERATIVE, False, 'きれ'),
        ('きる', Form.IMPERATIVE, True, 'きるな'),
        ('きる', Form.TE, False, 'きって'),
        ('きる', Form.TE, True, 'きらなくて'),
        ('きる', Form.CONDITIONAL_EBA, False, 'きれば'),
        ('きる', Form.CONDITIONAL_EBA, True, 'きらなければ'),
    ]
)
def test_godan_ru_2(verb, tense, negative, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('きる', Form.VOLITIONAL, False, 'きろう'),
        ('きる', Form.VOLITIONAL, True, 'きりましょう'),
    ]
)
def test_godan_ru_3(verb, tense, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings
