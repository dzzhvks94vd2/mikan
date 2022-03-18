import pytest
from mikan import GodanVerb, Form

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('とぶ', Form.PRESENT, False, False, 'とぶ'),
        ('とぶ', Form.PAST, False, False, 'とんだ'),
        ('とぶ', Form.PRESUMPTIVE, False, False, 'とぶだろう'),
        ('とぶ', Form.CONDITIONAL_RA, False, False, 'とんだら'),
        ('とぶ', Form.POTENTIAL, False, False, 'とべる'),
        ('とぶ', Form.PASSIVE, False, False, 'とばれる'),
        ('とぶ', Form.CAUSATIVE, False, False, 'とばせる'),
        ('とぶ', (Form.CAUSATIVE, Form.PASSIVE), False, False, 'とばせられる'),

        ('とぶ', Form.PRESENT, True, False, 'とばない'),
        ('とぶ', Form.PAST, True, False, 'とばなかった'),
        ('とぶ', Form.PRESUMPTIVE, True, False, 'とばないだろう'),
        ('とぶ', Form.CONDITIONAL_RA, True, False, 'とばなかったら'),
        ('とぶ', Form.POTENTIAL, True, False, 'とべない'),
        ('とぶ', Form.PASSIVE, True, False, 'とばれない'),
        ('とぶ', Form.CAUSATIVE, True, False, 'とばせない'),
        ('とぶ', (Form.CAUSATIVE, Form.PASSIVE), True, False, 'とばせられない'),

        ('とぶ', Form.PRESENT, False, True, 'とびます'),
        ('とぶ', Form.PAST, False, True, 'とびました'),
        ('とぶ', Form.PRESUMPTIVE, False, True, 'とぶでしょう'),
        ('とぶ', Form.CONDITIONAL_RA, False, True, 'とびましたら'),
        ('とぶ', Form.POTENTIAL, False, True, 'とべます'),
        ('とぶ', Form.PASSIVE, False, True, 'とばれます'),
        ('とぶ', Form.CAUSATIVE, False, True, 'とばせます'),
        ('とぶ', (Form.CAUSATIVE, Form.PASSIVE), False, True, 'とばせられます'),

        ('とぶ', Form.PRESENT, True, True, 'とびません'),
        ('とぶ', Form.PAST, True, True, 'とびませんでした'),
        ('とぶ', Form.PRESUMPTIVE, True, True, 'とばないでしょう'),
        ('とぶ', Form.CONDITIONAL_RA, True, True, 'とびませんでしたら'),
        ('とぶ', Form.POTENTIAL, True, True, 'とべません'),
        ('とぶ', Form.PASSIVE, True, True, 'とばれません'),
        ('とぶ', Form.CAUSATIVE, True, True, 'とばせません'),
        ('とぶ', (Form.CAUSATIVE, Form.PASSIVE), True, True, 'とばせられません'),
    ]
)
def test_godan_bu_1(verb, tense, negative, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('とぶ', Form.IMPERATIVE, False, 'とべ'),
        ('とぶ', Form.IMPERATIVE, True, 'とぶな'),
        ('とぶ', Form.TE, False, 'とんで'),
        ('とぶ', Form.TE, True, 'とばなくて'),
        ('とぶ', Form.CONDITIONAL_EBA, False, 'とべば'),
        ('とぶ', Form.CONDITIONAL_EBA, True, 'とばなければ'),
    ]
)
def test_godan_bu_2(verb, tense, negative, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('とぶ', Form.VOLITIONAL, False, 'とぼう'),
        ('とぶ', Form.VOLITIONAL, True, 'とびましょう'),
    ]
)
def test_godan_bu_3(verb, tense, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings
