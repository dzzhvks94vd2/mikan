import pytest
from mikan import GodanVerb, Form

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('のむ', Form.PRESENT, False, False, 'のむ'),
        ('のむ', Form.PAST, False, False, 'のんだ'),
        ('のむ', Form.PRESUMPTIVE, False, False, 'のむだろう'),
        ('のむ', Form.CONDITIONAL_RA, False, False, 'のんだら'),
        ('のむ', Form.POTENTIAL, False, False, 'のめる'),
        ('のむ', Form.PASSIVE, False, False, 'のまれる'),
        ('のむ', Form.CAUSATIVE, False, False, 'のませる'),
        ('のむ', (Form.CAUSATIVE, Form.PASSIVE), False, False, 'のませられる'),

        ('のむ', Form.PRESENT, True, False, 'のまない'),
        ('のむ', Form.PAST, True, False, 'のまなかった'),
        ('のむ', Form.PRESUMPTIVE, True, False, 'のまないだろう'),
        ('のむ', Form.CONDITIONAL_RA, True, False, 'のまなかったら'),
        ('のむ', Form.POTENTIAL, True, False, 'のめない'),
        ('のむ', Form.PASSIVE, True, False, 'のまれない'),
        ('のむ', Form.CAUSATIVE, True, False, 'のませない'),
        ('のむ', (Form.CAUSATIVE, Form.PASSIVE), True, False, 'のませられない'),

        ('のむ', Form.PRESENT, False, True, 'のみます'),
        ('のむ', Form.PAST, False, True, 'のみました'),
        ('のむ', Form.PRESUMPTIVE, False, True, 'のむでしょう'),
        ('のむ', Form.CONDITIONAL_RA, False, True, 'のみましたら'),
        ('のむ', Form.POTENTIAL, False, True, 'のめます'),
        ('のむ', Form.PASSIVE, False, True, 'のまれます'),
        ('のむ', Form.CAUSATIVE, False, True, 'のませます'),
        ('のむ', (Form.CAUSATIVE, Form.PASSIVE), False, True, 'のませられます'),

        ('のむ', Form.PRESENT, True, True, 'のみません'),
        ('のむ', Form.PAST, True, True, 'のみませんでした'),
        ('のむ', Form.PRESUMPTIVE, True, True, 'のまないでしょう'),
        ('のむ', Form.CONDITIONAL_RA, True, True, 'のみませんでしたら'),
        ('のむ', Form.POTENTIAL, True, True, 'のめません'),
        ('のむ', Form.PASSIVE, True, True, 'のまれません'),
        ('のむ', Form.CAUSATIVE, True, True, 'のませません'),
        ('のむ', (Form.CAUSATIVE, Form.PASSIVE), True, True, 'のませられません'),
    ]
)
def test_godan_mu_1(verb, tense, negative, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('のむ', Form.IMPERATIVE, False, 'のめ'),
        ('のむ', Form.IMPERATIVE, True, 'のむな'),
        ('のむ', Form.TE, False, 'のんで'),
        ('のむ', Form.TE, True, 'のまなくて'),
        ('のむ', Form.CONDITIONAL_EBA, False, 'のめば'),
        ('のむ', Form.CONDITIONAL_EBA, True, 'のまなければ'),
    ]
)
def test_godan_mu_2(verb, tense, negative, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('のむ', Form.VOLITIONAL, False, 'のもう'),
        ('のむ', Form.VOLITIONAL, True, 'のみましょう'),
    ]
)
def test_godan_mu_3(verb, tense, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings
