import pytest
from mikan import GodanVerb

def test_not_godan():

    with pytest.raises(ValueError):
        GodanVerb('みかん')
