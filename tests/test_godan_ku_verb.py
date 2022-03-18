import pytest
from mikan import GodanVerb, Form

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('はたらく', Form.PRESENT, False, False, 'はたらく'),
        ('はたらく', Form.PAST, False, False, 'はたらいた'),
        ('はたらく', Form.PRESUMPTIVE, False, False, 'はたらくだろう'),
        ('はたらく', Form.CONDITIONAL_RA, False, False, 'はたらいたら'),
        ('はたらく', Form.POTENTIAL, False, False, 'はたらける'),
        ('はたらく', Form.PASSIVE, False, False, 'はたらかれる'),
        ('はたらく', Form.CAUSATIVE, False, False, 'はたらかせる'),
        ('はたらく', (Form.CAUSATIVE, Form.PASSIVE), False, False, 'はたらかせられる'),

        ('はたらく', Form.PRESENT, True, False, 'はたらかない'),
        ('はたらく', Form.PAST, True, False, 'はたらかなかった'),
        ('はたらく', Form.PRESUMPTIVE, True, False, 'はたらかないだろう'),
        ('はたらく', Form.CONDITIONAL_RA, True, False, 'はたらかなかったら'),
        ('はたらく', Form.POTENTIAL, True, False, 'はたらけない'),
        ('はたらく', Form.PASSIVE, True, False, 'はたらかれない'),
        ('はたらく', Form.CAUSATIVE, True, False, 'はたらかせない'),
        ('はたらく', (Form.CAUSATIVE, Form.PASSIVE), True, False, 'はたらかせられない'),

        ('はたらく', Form.PRESENT, False, True, 'はたらきます'),
        ('はたらく', Form.PAST, False, True, 'はたらきました'),
        ('はたらく', Form.PRESUMPTIVE, False, True, 'はたらくでしょう'),
        ('はたらく', Form.CONDITIONAL_RA, False, True, 'はたらきましたら'),
        ('はたらく', Form.POTENTIAL, False, True, 'はたらけます'),
        ('はたらく', Form.PASSIVE, False, True, 'はたらかれます'),
        ('はたらく', Form.CAUSATIVE, False, True, 'はたらかせます'),
        ('はたらく', (Form.CAUSATIVE, Form.PASSIVE), False, True, 'はたらかせられます'),

        ('はたらく', Form.PRESENT, True, True, 'はたらきません'),
        ('はたらく', Form.PAST, True, True, 'はたらきませんでした'),
        ('はたらく', Form.PRESUMPTIVE, True, True, 'はたらかないでしょう'),
        ('はたらく', Form.CONDITIONAL_RA, True, True, 'はたらきませんでしたら'),
        ('はたらく', Form.POTENTIAL, True, True, 'はたらけません'),
        ('はたらく', Form.PASSIVE, True, True, 'はたらかれません'),
        ('はたらく', Form.CAUSATIVE, True, True, 'はたらかせません'),
        ('はたらく', (Form.CAUSATIVE, Form.PASSIVE), True, True, 'はたらかせられません'),
    ]
)
def test_godan_ku_1(verb, tense, negative, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,expected",
    [
        ('はたらく', Form.IMPERATIVE, False, 'はたらけ'),
        ('はたらく', Form.IMPERATIVE, True, 'はたらくな'),
        ('はたらく', Form.TE, False, 'はたらいて'),
        ('はたらく', Form.TE, True, 'はたらかなくて'),
        ('はたらく', Form.CONDITIONAL_EBA, False, 'はたらけば'),
        ('はたらく', Form.CONDITIONAL_EBA, True, 'はたらかなければ'),
    ]
)
def test_godan_ku_2(verb, tense, negative, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "verb,tense,polite,expected",
    [
        ('はたらく', Form.VOLITIONAL, False, 'はたらこう'),
        ('はたらく', Form.VOLITIONAL, True, 'はたらきましょう'),
    ]
)
def test_godan_ku_3(verb, tense, polite, expected):

    v = GodanVerb(verb)

    assert expected in v.conjugate(tense, polite=polite).readings
