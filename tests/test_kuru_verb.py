import pytest
from mikan import KuruVerb, Form

@pytest.mark.parametrize(
    "tense,negative,polite,expkana,expkanji",
    [
        (Form.PRESENT, False, False, 'くる', '来る'),
        (Form.PAST, False, False, 'きた', '来た'),
        (Form.PRESUMPTIVE, False, False, 'くるだろう', '来るだろう'),
        (Form.CONDITIONAL_RA, False, False, 'きたら', '来たら'),
        (Form.POTENTIAL, False, False, 'こられる', '来られる'),
        (Form.PASSIVE, False, False, 'こられる', '来られる'),
        (Form.CAUSATIVE, False, False, 'こさせる', '来させる'),
        ((Form.CAUSATIVE, Form.PASSIVE), False, False, 'こさせられる', '来させられる'),

        (Form.PRESENT, True, False, 'こない', '来ない'),
        (Form.PAST, True, False, 'こなかった', '来なかった'),
        (Form.PRESUMPTIVE, True, False, 'こないだろう', '来ないだろう'),
        (Form.CONDITIONAL_RA, True, False, 'こなかったら', '来なかったら'),
        (Form.POTENTIAL, True, False, 'こられない', '来られない'),
        (Form.PASSIVE, True, False, 'こられない', '来られない'),
        (Form.CAUSATIVE, True, False, 'こさせない', '来させない'),
        ((Form.CAUSATIVE, Form.PASSIVE), True, False, 'こさせられない', '来させられない'),

        (Form.PRESENT, False, True, 'きます', '来ます'),
        (Form.PAST, False, True, 'きました', '来ました'),
        (Form.PRESUMPTIVE, False, True, 'くるでしょう', '来るでしょう'),
        (Form.CONDITIONAL_RA, False, True, 'きましたら', '来ましたら'),
        (Form.POTENTIAL, False, True, 'こられます', '来られます'),
        (Form.PASSIVE, False, True, 'こられます', '来られます'),
        (Form.CAUSATIVE, False, True, 'こさせます', '来させます'),
        ((Form.CAUSATIVE, Form.PASSIVE), False, True, 'こさせられます', '来させられます'),

        (Form.PRESENT, True, True, 'きません', '来ません'),
        (Form.PAST, True, True, 'きませんでした', '来ませんでした'),
        (Form.PRESUMPTIVE, True, True, 'こないでしょう', '来ないでしょう'),
        (Form.CONDITIONAL_RA, True, True, 'きませんでしたら', '来ませんでしたら'),
        (Form.POTENTIAL, True, True, 'こられません', '来られません'),
        (Form.PASSIVE, True, True, 'こられません', '来られません'),
        (Form.CAUSATIVE, True, True, 'こさせません', '来させません'),
        ((Form.CAUSATIVE, Form.PASSIVE), True, True, 'こさせられません', '来させられません'),
    ]
)
def test_kuru_1(tense, negative, polite, expkana, expkanji):

    v = KuruVerb('来る', 'くる')
    conj = v.conjugate(tense, negative=negative, polite=polite)
    assert expkana in conj.readings
    assert expkanji in conj.writings

@pytest.mark.parametrize(
    "tense,negative,expkana,expkanji",
    [
        (Form.IMPERATIVE, False, 'こい', '来い'),
        (Form.IMPERATIVE, True, 'くるな', '来るな'),
        (Form.TE, False, 'きて', '来て'),
        (Form.TE, True, 'こなくて', '来なくて'),
        (Form.CONDITIONAL_EBA, False, 'くれば', '来れば'),
        (Form.CONDITIONAL_EBA, True, 'こなければ', '来なければ'),
    ]
)
def test_kuru_2(tense, negative, expkana, expkanji):

    v = KuruVerb('来る', 'くる')
    conj = v.conjugate(tense, negative=negative)
    assert expkana in conj.readings
    assert expkanji in conj.writings

@pytest.mark.parametrize(
    "tense,polite,expkana,expkanji",
    [
        (Form.VOLITIONAL, False, 'こよう', '来よう'),
        (Form.VOLITIONAL, True, 'きましょう', '来ましょう'),
    ]
)
def test_kuru_3(tense, polite, expkana, expkanji):

    v = KuruVerb('来る', 'くる')
    conj = v.conjugate(tense, polite=polite)
    assert expkana in conj.readings
    assert expkanji in conj.writings

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('もってくる', Form.PRESENT, False, True, 'もってきます'),
        ('もってくる', Form.PRESENT, False, False, 'もってくる'),
    ]
)
def test_kuru_4(verb, tense, negative, polite, expected):

    v = KuruVerb(verb)
    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings
