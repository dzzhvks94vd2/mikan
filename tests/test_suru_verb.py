import pytest
from mikan import SuruVerb, Form

@pytest.mark.parametrize(
    "tense,negative,polite,expected",
    [
        (Form.PRESENT, False, False, 'する'),
        (Form.PAST, False, False, 'した'),
        (Form.PRESUMPTIVE, False, False, 'するだろう'),
        (Form.CONDITIONAL_RA, False, False, 'したら'),
        (Form.POTENTIAL, False, False, 'できる'),
        (Form.PASSIVE, False, False, 'される'),
        (Form.CAUSATIVE, False, False, 'させる'),
        ((Form.CAUSATIVE, Form.PASSIVE), False, False, 'させられる'),

        (Form.PRESENT, True, False, 'しない'),
        (Form.PAST, True, False, 'しなかった'),
        (Form.PRESUMPTIVE, True, False, 'しないだろう'),
        (Form.CONDITIONAL_RA, True, False, 'しなかったら'),
        (Form.POTENTIAL, True, False, 'できない'),
        (Form.PASSIVE, True, False, 'されない'),
        (Form.CAUSATIVE, True, False, 'させない'),
        ((Form.CAUSATIVE, Form.PASSIVE), True, False, 'させられない'),

        (Form.PRESENT, False, True, 'します'),
        (Form.PAST, False, True, 'しました'),
        (Form.PRESUMPTIVE, False, True, 'するでしょう'),
        (Form.CONDITIONAL_RA, False, True, 'しましたら'),
        (Form.POTENTIAL, False, True, 'できます'),
        (Form.PASSIVE, False, True, 'されます'),
        (Form.CAUSATIVE, False, True, 'させます'),
        ((Form.CAUSATIVE, Form.PASSIVE), False, True, 'させられます'),

        (Form.PRESENT, True, True, 'しません'),
        (Form.PAST, True, True, 'しませんでした'),
        (Form.PRESUMPTIVE, True, True, 'しないでしょう'),
        (Form.CONDITIONAL_RA, True, True, 'しませんでしたら'),
        (Form.POTENTIAL, True, True, 'できません'),
        (Form.PASSIVE, True, True, 'されません'),
        (Form.CAUSATIVE, True, True, 'させません'),
        ((Form.CAUSATIVE, Form.PASSIVE), True, True, 'させられません'),
    ]
)
def test_suru_1(tense, negative, polite, expected):

    v = SuruVerb()

    assert expected in v.conjugate(tense, negative=negative, polite=polite).readings

@pytest.mark.parametrize(
    "tense,negative,expected",
    [
        (Form.IMPERATIVE, False, 'しろ'),
        (Form.IMPERATIVE, True, 'するな'),
        (Form.TE, False, 'して'),
        (Form.TE, True, 'しなくて'),
        (Form.CONDITIONAL_EBA, False, 'すれば'),
        (Form.CONDITIONAL_EBA, True, 'しなければ'),
    ]
)
def test_suru_2(tense, negative, expected):

    v = SuruVerb()

    assert expected in v.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "tense,polite,expected",
    [
        (Form.VOLITIONAL, False, 'しよう'),
        (Form.VOLITIONAL, True, 'しましょう'),
    ]
)
def test_suru_3(tense, polite, expected):

    v = SuruVerb()

    assert expected in v.conjugate(tense, polite=polite).readings

@pytest.mark.parametrize(
    "verb,tense,negative,polite,expected",
    [
        ('勉強', Form.PRESENT, False, False, '勉強する'),
        ('勉強', Form.PRESENT, False, True, '勉強します'),
    ]
)
def test_suru_4(verb, tense, negative, polite, expected):

    v = SuruVerb(verb)
    assert expected in v.conjugate(tense, negative=negative, polite=polite).writings
