import pytest
from mikan import KuruVerb, VerbForm

@pytest.mark.parametrize(
    "tense,negative,polite,expkana,expkanji",
    [
        (VerbForm.PRESENT, False, False, 'くる', '来る'),
        (VerbForm.PAST, False, False, 'きた', '来た'),
        (VerbForm.PRESUMPTIVE, False, False, 'くるだろう', '来るだろう'),
        (VerbForm.CONDITIONAL_RA, False, False, 'きたら', '来たら'),
        (VerbForm.POTENTIAL, False, False, 'こられる', '来られる'),
        (VerbForm.PASSIVE, False, False, 'こられる', '来られる'),
        (VerbForm.CAUSATIVE, False, False, 'こさせる', '来させる'),
        ((VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, False, 'こさせられる', '来させられる'),

        (VerbForm.PRESENT, True, False, 'こない', '来ない'),
        (VerbForm.PAST, True, False, 'こなかった', '来なかった'),
        (VerbForm.PRESUMPTIVE, True, False, 'こないだろう', '来ないだろう'),
        (VerbForm.CONDITIONAL_RA, True, False, 'こなかったら', '来なかったら'),
        (VerbForm.POTENTIAL, True, False, 'こられない', '来られない'),
        (VerbForm.PASSIVE, True, False, 'こられない', '来られない'),
        (VerbForm.CAUSATIVE, True, False, 'こさせない', '来させない'),
        ((VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, False, 'こさせられない', '来させられない'),

        (VerbForm.PRESENT, False, True, 'きます', '来ます'),
        (VerbForm.PAST, False, True, 'きました', '来ました'),
        (VerbForm.PRESUMPTIVE, False, True, 'くるでしょう', '来るでしょう'),
        (VerbForm.CONDITIONAL_RA, False, True, 'きましたら', '来ましたら'),
        (VerbForm.POTENTIAL, False, True, 'こられます', '来られます'),
        (VerbForm.PASSIVE, False, True, 'こられます', '来られます'),
        (VerbForm.CAUSATIVE, False, True, 'こさせます', '来させます'),
        ((VerbForm.CAUSATIVE, VerbForm.PASSIVE), False, True, 'こさせられます', '来させられます'),

        (VerbForm.PRESENT, True, True, 'きません', '来ません'),
        (VerbForm.PAST, True, True, 'きませんでした', '来ませんでした'),
        (VerbForm.PRESUMPTIVE, True, True, 'こないでしょう', '来ないでしょう'),
        (VerbForm.CONDITIONAL_RA, True, True, 'きませんでしたら', '来ませんでしたら'),
        (VerbForm.POTENTIAL, True, True, 'こられません', '来られません'),
        (VerbForm.PASSIVE, True, True, 'こられません', '来られません'),
        (VerbForm.CAUSATIVE, True, True, 'こさせません', '来させません'),
        ((VerbForm.CAUSATIVE, VerbForm.PASSIVE), True, True, 'こさせられません', '来させられません'),
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
        (VerbForm.IMPERATIVE, False, 'こい', '来い'),
        (VerbForm.IMPERATIVE, True, 'くるな', '来るな'),
        (VerbForm.TE_FORM, False, 'きて', '来て'),
        (VerbForm.TE_FORM, True, 'こなくて', '来なくて'),
        (VerbForm.CONDITIONAL_EBA, False, 'くれば', '来れば'),
        (VerbForm.CONDITIONAL_EBA, True, 'こなければ', '来なければ'),
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
        (VerbForm.VOLITIONAL, False, 'こよう', '来よう'),
        (VerbForm.VOLITIONAL, True, 'きましょう', '来ましょう'),
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
        ('もってくる', VerbForm.PRESENT, False, True, 'もってきます'),
        ('もってくる', VerbForm.PRESENT, False, False, 'もってくる'),
    ]
)
def test_kuru_4(verb, tense, negative, polite, expected):

    v = KuruVerb(verb)
    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings
