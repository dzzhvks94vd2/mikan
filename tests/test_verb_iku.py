import pytest
from mikan import IkuVerb, Form

@pytest.mark.parametrize(
    "verb,tense,expected",
    [
        ('いく', Form.TE, 'いって'),
        ('いく', Form.PAST, 'いった'),
        ('もっていく', Form.TE, 'もっていって'),
        ('行く', Form.TE, '行って'),
    ]
)
def test_godan_ku_exceptions(verb, tense, expected):

    v = IkuVerb(verb)
    assert expected in v.conjugate(tense).writings
