import pytest
from mikan import GodanVerb, VerbForm

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('はたらく', VerbForm.PRESENT, False, False, 'はたらく'),
        ('はたらく', VerbForm.PAST, False, False, 'はたらいた'),
        ('はたらく', VerbForm.PRESUMPTIVE, False, False, 'はたらくだろう'),
        ('はたらく', VerbForm.CONDITIONAL_RA, False, False, 'はたらいたら'),
        ('はたらく', VerbForm.POTENTIAL, False, False, 'はたらける'),
        ('はたらく', VerbForm.PASSIVE, False, False, 'はたらかれる'),
        ('はたらく', VerbForm.CAUSATIVE, False, False, 'はたらかせる'),
        ('はたらく', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, False, 'はたらかせられる'),

        ('はたらく', VerbForm.PRESENT, True, False, 'はたらかない'),
        ('はたらく', VerbForm.PAST, True, False, 'はたらかなかった'),
        ('はたらく', VerbForm.PRESUMPTIVE, True, False, 'はたらかないだろう'),
        ('はたらく', VerbForm.CONDITIONAL_RA, True, False, 'はたらかなかったら'),
        ('はたらく', VerbForm.POTENTIAL, True, False, 'はたらけない'),
        ('はたらく', VerbForm.PASSIVE, True, False, 'はたらかれない'),
        ('はたらく', VerbForm.CAUSATIVE, True, False, 'はたらかせない'),
        ('はたらく', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, False, 'はたらかせられない'),

        ('はたらく', VerbForm.PRESENT, False, True, 'はたらきます'),
        ('はたらく', VerbForm.PAST, False, True, 'はたらきました'),
        ('はたらく', VerbForm.PRESUMPTIVE, False, True, 'はたらくでしょう'),
        ('はたらく', VerbForm.CONDITIONAL_RA, False, True, 'はたらきましたら'),
        ('はたらく', VerbForm.POTENTIAL, False, True, 'はたらけます'),
        ('はたらく', VerbForm.PASSIVE, False, True, 'はたらかれます'),
        ('はたらく', VerbForm.CAUSATIVE, False, True, 'はたらかせます'),
        ('はたらく', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, True, 'はたらかせられます'),

        ('はたらく', VerbForm.PRESENT, True, True, 'はたらきません'),
        ('はたらく', VerbForm.PAST, True, True, 'はたらきませんでした'),
        ('はたらく', VerbForm.PRESUMPTIVE, True, True, 'はたらかないでしょう'),
        ('はたらく', VerbForm.CONDITIONAL_RA, True, True, 'はたらきませんでしたら'),
        ('はたらく', VerbForm.POTENTIAL, True, True, 'はたらけません'),
        ('はたらく', VerbForm.PASSIVE, True, True, 'はたらかれません'),
        ('はたらく', VerbForm.CAUSATIVE, True, True, 'はたらかせません'),
        ('はたらく', (VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, True, 'はたらかせられません'),
    ]
)
def test_godan_ku_1(verb, tense, negative, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('はたらく', VerbForm.IMPERATIVE, False, 'はたらけ'),
        ('はたらく', VerbForm.IMPERATIVE, True, 'はたらくな'),
        ('はたらく', VerbForm.TE_FORM, False, 'はたらいて'),
        ('はたらく', VerbForm.TE_FORM, True, 'はたらかなくて'),
        ('はたらく', VerbForm.CONDITIONAL_EBA, False, 'はたらけば'),
        ('はたらく', VerbForm.CONDITIONAL_EBA, True, 'はたらかなければ'),
    ]
)
def test_godan_ku_2(verb, tense, negative, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('はたらく', VerbForm.VOLITIONAL, False, 'はたらこう'),
        ('はたらく', VerbForm.VOLITIONAL, True, 'はたらきましょう'),
    ]
)
def test_godan_ku_3(verb, tense, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings
