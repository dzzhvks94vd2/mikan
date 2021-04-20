import pytest
from mikan import GodanVerb, VerbForm

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('のむ', VerbForm.PRESENT, False, False, 'のむ'),
        ('のむ', VerbForm.PAST, False, False, 'のんだ'),
        ('のむ', VerbForm.PRESUMPTIVE, False, False, 'のむだろう'),
        ('のむ', VerbForm.CONDITIONAL_RA, False, False, 'のんだら'),
        ('のむ', VerbForm.POTENTIAL, False, False, 'のめる'),
        ('のむ', VerbForm.PASSIVE, False, False, 'のまれる'),
        ('のむ', VerbForm.CAUSATIVE, False, False, 'のませる'),
        ('のむ', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, False, 'のませられる'),

        ('のむ', VerbForm.PRESENT, True, False, 'のまない'),
        ('のむ', VerbForm.PAST, True, False, 'のまなかった'),
        ('のむ', VerbForm.PRESUMPTIVE, True, False, 'のまないだろう'),
        ('のむ', VerbForm.CONDITIONAL_RA, True, False, 'のまなかったら'),
        ('のむ', VerbForm.POTENTIAL, True, False, 'のめない'),
        ('のむ', VerbForm.PASSIVE, True, False, 'のまれない'),
        ('のむ', VerbForm.CAUSATIVE, True, False, 'のませない'),
        ('のむ', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, False, 'のませられない'),

        ('のむ', VerbForm.PRESENT, False, True, 'のみます'),
        ('のむ', VerbForm.PAST, False, True, 'のみました'),
        ('のむ', VerbForm.PRESUMPTIVE, False, True, 'のむでしょう'),
        ('のむ', VerbForm.CONDITIONAL_RA, False, True, 'のみましたら'),
        ('のむ', VerbForm.POTENTIAL, False, True, 'のめます'),
        ('のむ', VerbForm.PASSIVE, False, True, 'のまれます'),
        ('のむ', VerbForm.CAUSATIVE, False, True, 'のませます'),
        ('のむ', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, True, 'のませられます'),

        ('のむ', VerbForm.PRESENT, True, True, 'のみません'),
        ('のむ', VerbForm.PAST, True, True, 'のみませんでした'),
        ('のむ', VerbForm.PRESUMPTIVE, True, True, 'のまないでしょう'),
        ('のむ', VerbForm.CONDITIONAL_RA, True, True, 'のみませんでしたら'),
        ('のむ', VerbForm.POTENTIAL, True, True, 'のめません'),
        ('のむ', VerbForm.PASSIVE, True, True, 'のまれません'),
        ('のむ', VerbForm.CAUSATIVE, True, True, 'のませません'),
        ('のむ', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, True, 'のませられません'),
    ]
)
def test_godan_mu_1(verb, tense, negative, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('のむ', VerbForm.IMPERATIVE, False, 'のめ'),
        ('のむ', VerbForm.IMPERATIVE, True, 'のむな'),
        ('のむ', VerbForm.TE_FORM, False, 'のんで'),
        ('のむ', VerbForm.TE_FORM, True, 'のまなくて'),
        ('のむ', VerbForm.CONDITIONAL_EBA, False, 'のめば'),
        ('のむ', VerbForm.CONDITIONAL_EBA, True, 'のまなければ'),
    ]
)
def test_godan_mu_2(verb, tense, negative, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('のむ', VerbForm.VOLITIONAL, False, 'のもう'),
        ('のむ', VerbForm.VOLITIONAL, True, 'のみましょう'),
    ]
)
def test_godan_mu_3(verb, tense, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings
