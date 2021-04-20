import pytest
from mikan import IkuVerb, VerbForm

@pytest.mark.parametrize(
    "verb,tense,expected",
    [
        ('いく', VerbForm.TE_FORM, 'いって'),
        ('いく', VerbForm.PAST, 'いった'),
        ('もっていく', VerbForm.TE_FORM, 'もっていって'),
        ('行く', VerbForm.TE_FORM, '行って'),
    ]
)
def test_godan_ku_exceptions(verb, tense, expected):

    v = IkuVerb(verb)
    assert expected in v.conjugate(tense).writings
