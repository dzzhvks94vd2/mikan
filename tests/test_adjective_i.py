import pytest
from mikan import IAdjective, YoiAdjective, AdjectiveForm

@pytest.mark.parametrize(
    "adj,tense,negative,expected",
    [
        ('おいしい', AdjectiveForm.PRESENT, False, 'おいしい'),
        ('おいしい', AdjectiveForm.PAST, False, 'おいしかった'),

        ('おいしい', AdjectiveForm.PRESENT, True, 'おいしくない'),
        ('おいしい', AdjectiveForm.PAST, True, 'おいしくなかった'),
    ]
)
def test_i_adjective_1(adj, tense, negative, expected):

    a = IAdjective(adj)
    assert expected in a.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "adj,tense,expected",
    [
        ('おいしい', AdjectiveForm.TE_FORM, 'おいしくて'),
        ('おいしい', AdjectiveForm.ADVERB, 'おいしく'),
    ]
)
def test_i_adjective_2(adj, tense, expected):

    a = IAdjective(adj)
    assert expected in a.conjugate(tense).readings

@pytest.mark.parametrize(
    "adj,tense,negative,expected",
    [
        ('よい', AdjectiveForm.PRESENT, False, 'いい'),
        ('よい', AdjectiveForm.PAST, False, 'よかった'),

        ('よい', AdjectiveForm.PRESENT, True, 'よくない'),
        ('よい', AdjectiveForm.PAST, True, 'よくなかった'),
    ]
)
def test_yoi_adjective_1(adj, tense, negative, expected):

    a = YoiAdjective(adj)
    assert expected in a.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "adj,expected",
    [
        ('よい', 'いい'),
        ('あたまがよい', 'あたまがいい'),
    ]
)
def test_yoi_adjective_2(adj, expected):

    a = YoiAdjective(adj)
    assert expected in a.readings
