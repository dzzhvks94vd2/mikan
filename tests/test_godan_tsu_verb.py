import pytest
from mikan import GodanVerb, Form

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('まつ', Form.PRESENT, False, False, 'まつ'),
        ('まつ', Form.PAST, False, False, 'まった'),
        ('まつ', Form.PRESUMPTIVE, False, False, 'まつだろう'),
        ('まつ', Form.CONDITIONAL_RA, False, False, 'まったら'),
        ('まつ', Form.POTENTIAL, False, False, 'まてる'),
        ('まつ', Form.PASSIVE, False, False, 'またれる'),
        ('まつ', Form.CAUSATIVE, False, False, 'またせる'),
        ('まつ', (Form.CAUSATIVE, Form.PASSIVE), False, False, 'またせられる'),

        ('まつ', Form.PRESENT, True, False, 'またない'),
        ('まつ', Form.PAST, True, False, 'またなかった'),
        ('まつ', Form.PRESUMPTIVE, True, False, 'またないだろう'),
        ('まつ', Form.CONDITIONAL_RA, True, False, 'またなかったら'),
        ('まつ', Form.POTENTIAL, True, False, 'まてない'),
        ('まつ', Form.PASSIVE, True, False, 'またれない'),
        ('まつ', Form.CAUSATIVE, True, False, 'またせない'),
        ('まつ', (Form.CAUSATIVE, Form.PASSIVE), True, False, 'またせられない'),

        ('まつ', Form.PRESENT, False, True, 'まちます'),
        ('まつ', Form.PAST, False, True, 'まちました'),
        ('まつ', Form.PRESUMPTIVE, False, True, 'まつでしょう'),
        ('まつ', Form.CONDITIONAL_RA, False, True, 'まちましたら'),
        ('まつ', Form.POTENTIAL, False, True, 'まてます'),
        ('まつ', Form.PASSIVE, False, True, 'またれます'),
        ('まつ', Form.CAUSATIVE, False, True, 'またせます'),
        ('まつ', (Form.CAUSATIVE, Form.PASSIVE), False, True, 'またせられます'),

        ('まつ', Form.PRESENT, True, True, 'まちません'),
        ('まつ', Form.PAST, True, True, 'まちませんでした'),
        ('まつ', Form.PRESUMPTIVE, True, True, 'またないでしょう'),
        ('まつ', Form.CONDITIONAL_RA, True, True, 'まちませんでしたら'),
        ('まつ', Form.POTENTIAL, True, True, 'まてません'),
        ('まつ', Form.PASSIVE, True, True, 'またれません'),
        ('まつ', Form.CAUSATIVE, True, True, 'またせません'),
        ('まつ', (Form.CAUSATIVE, Form.PASSIVE), True, True, 'またせられません'),
    ]
)
def test_godan_tsu_1(verb, tense, negative, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('まつ', Form.IMPERATIVE, False, 'まて'),
        ('まつ', Form.IMPERATIVE, True, 'まつな'),
        ('まつ', Form.TE, False, 'まって'),
        ('まつ', Form.TE, True, 'またなくて'),
        ('まつ', Form.CONDITIONAL_EBA, False, 'まてば'),
        ('まつ', Form.CONDITIONAL_EBA, True, 'またなければ'),
    ]
)
def test_godan_tsu_2(verb, tense, negative, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('まつ', Form.VOLITIONAL, False, 'まとう'),
        ('まつ', Form.VOLITIONAL, True, 'まちましょう'),
    ]
)
def test_godan_tsu_3(verb, tense, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings
