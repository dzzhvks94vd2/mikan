import pytest
from mikan import IAdjective, YoiAdjective, Form

@pytest.mark.parametrize(
    "adj,tense,negative,expected",
    [
        ('おいしい', Form.PRESENT, False, 'おいしい'),
        ('おいしい', Form.PAST, False, 'おいしかった'),

        ('おいしい', Form.PRESENT, True, 'おいしくない'),
        ('おいしい', Form.PAST, True, 'おいしくなかった'),
    ]
)
def test_i_adjective_1(adj, tense, negative, expected):

    a = IAdjective(adj)
    assert expected in a.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "adj,tense,expected",
    [
        ('おいしい', Form.TE, 'おいしくて'),
        ('おいしい', Form.ADVERB, 'おいしく'),
    ]
)
def test_i_adjective_2(adj, tense, expected):

    a = IAdjective(adj)
    assert expected in a.conjugate(tense).readings

@pytest.mark.parametrize(
    "adj,tense,negative,expected",
    [
        ('よい', Form.PRESENT, False, 'いい'),
        ('よい', Form.PAST, False, 'よかった'),

        ('よい', Form.PRESENT, True, 'よくない'),
        ('よい', Form.PAST, True, 'よくなかった'),

        ('いい', Form.PRESENT, True, 'よくない'),
    ]
)
def test_yoi_adjective_1(adj, tense, negative, expected):

    a = YoiAdjective(adj)
    assert expected in a.conjugate(tense, negative=negative).readings

@pytest.mark.parametrize(
    "adj,expected",
    [
        ('いい', 'いい'),
        ('よい', 'いい'),
        ('あたまがいい', 'あたまがいい'),
        ('あたまがよい', 'あたまがいい'),
    ]
)
def test_yoi_adjective_2(adj, expected):

    a = YoiAdjective(adj)
    assert expected in a.readings
