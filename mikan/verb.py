from typing import Dict, Tuple, Callable, Union, List, Optional

from mikan.adjective import IAdjective
from mikan.base import BaseWord, Form
from mikan.exceptions import InvalidConjugation
from mikan.word import Word
from mikan.writing import Writing

__all__ = [
    'GodanVerb',
    'IchidanVerb',
    'KuruVerb',
    'SuruVerb',
    'IkuVerb',
    'AruVerb',
]

class Verb:
    """A Verb."""

    _ENDINGS: Dict[
        Form,
        Dict[
            bool,
            Dict[
                bool,
                Callable[
                    [Tuple[Dict[str, BaseWord], bool]],
                    BaseWord
                ]
            ]
        ]
    ] = {
        Form.PRESENT: {
            False: {
                False: lambda x: x[0]['self'],
                True: lambda x: x[0]['masu'] + 'ます',
            },
            True: {
                False: lambda x: x[0]['nai'] + 'ない',
                True: lambda x: x[0]['masu'] + 'ません',
            },
        },
        Form.PAST: {
            False: {
                False: lambda x: x[0]['ta'] + ('だ' if x[1] else 'た'),
                True: lambda x: x[0]['masu'] + 'ました',
            },
            True: {
                False: lambda x: x[0]['nai'] + 'なかった',
                True: lambda x: x[0]['masu'] + 'ませんでした',
            },
        },
        Form.IMPERATIVE: {
            False: {
                False: lambda x: x[0]['imp'],
            },
            True: {
                False: lambda x: x[0]['self'] + 'な',
            },
        },
        Form.TE: {
            False: {
                False: lambda x: x[0]['ta'] + ('で' if x[1] else 'て'),
            },
            True: {
                False: lambda x: x[0]['nai'] + 'なくて',
            },
        },
        Form.CONDITIONAL_EBA: {
            False: {
                False: lambda x: x[0]['e'] + 'ば',
            },
            True: {
                False: lambda x: x[0]['nai'] + 'なければ',
            },
        },
        Form.CONDITIONAL_RA: {
            False: {
                False: lambda x: x[0]['ta'] + ('だ' if x[1] else 'た') + 'ら',
                True: lambda x: x[0]['masu'] + 'ましたら',
            },
            True: {
                False: lambda x: x[0]['nai'] + 'なかったら',
                True: lambda x: x[0]['masu'] + 'ませんでしたら',
            },
        },
        Form.PRESUMPTIVE: {
            False: {
                False: lambda x: x[0]['self'] + 'だろう',
                True: lambda x: x[0]['self'] + 'でしょう',
            },
            True: {
                False: lambda x: x[0]['nai'] + 'ないだろう',
                True: lambda x: x[0]['nai'] + 'ないでしょう',
            },
        },
        Form.VOLITIONAL: {
            False: {
                False: lambda x: x[0]['vol'] + 'う',
                True: lambda x: x[0]['masu'] + 'ましょう',
            },
        },
    }

    def __init__(self, forms: Tuple[Dict[str, BaseWord], bool]) -> None:

        self._forms = forms

    def conjugate(
        self,
        forms: Optional[Union[Form, List[Form]]]=None,
        polite: bool=False,
        negative: bool=False
    ) -> BaseWord:
        """Conjugate the verb in the given tense."""

        if forms is None:
            forms = Form.PRESENT

        if isinstance(forms, Form):
            current = forms
            follow = [Form.PRESENT]
        else:
            current = forms[0]
            follow = forms[1:] if len(forms) > 1 else [Form.PRESENT]

        if current == Form.POTENTIAL:
            return IchidanVerb(self._forms[0]['pot'] + 'る').conjugate(follow, polite, negative)
        if current == Form.PASSIVE:
            return IchidanVerb(self._forms[0]['pas'] + 'れる').conjugate(follow, polite, negative)
        if current == Form.CAUSATIVE:
            return IchidanVerb(self._forms[0]['cau'] + 'せる').conjugate(follow, polite, negative)
        if current == Form.TAI:
            return IAdjective(self._forms[0]['masu'] + 'たい').conjugate(follow, negative)

        if current not in self._ENDINGS:
            raise InvalidConjugation("This form is not supported")

        if negative not in self._ENDINGS[current]:
            raise InvalidConjugation("There's no negative for this form")

        if polite not in self._ENDINGS[current][negative]:
            raise InvalidConjugation("There's no polite for this form")

        return self._ENDINGS[current][negative][polite](self._forms)

class IchidanVerb(Verb, Word):
    """An ichidan (AKA group 2) verb."""

    def __init__(self, *args: Union[str, Writing, BaseWord]) -> None:

        Word.__init__(self, *args)

        base, ending = self.split_okurigana(1)
        if ending != 'る':
            raise ValueError('This is not an ichidan verb')

        Verb.__init__(self, ({
            'ta': base,
            'pot': base + 'られ',
            'pas': base + 'ら',
            'cau': base + 'さ',
            'nai': base,
            'masu': base,
            'imp': base + 'ろ',
            'e': base + 'れ',
            'vol': base + 'よ',
            'self': self,
        }, False))

class GodanVerb(Verb, Word):
    """A godan (AKA group 1) verb."""

    _GODAN_ENDINGS = {
        'う': ({
            'i': 'い',
            'ta': 'っ',
            'a': 'わ',
            'e': 'え',
            'o': 'お',
        }, False),
        'る': ({
            'i': 'り',
            'ta': 'っ',
            'a': 'ら',
            'e': 'れ',
            'o': 'ろ',
        }, False),
        'む' : ({
            'i': 'み',
            'ta': 'ん',
            'a': 'ま',
            'e': 'め',
            'o': 'も',
        }, True),
        'ぬ' : ({
            'i': 'に',
            'ta': 'ん',
            'a': 'な',
            'e': 'ね',
            'o': 'の',
        }, True),
        'く': ({
            'i': 'き',
            'ta': 'い',
            'a': 'か',
            'e': 'け',
            'o': 'こ',
        }, False),
        'ぐ': ({
            'i': 'ぎ',
            'ta': 'い',
            'a': 'が',
            'e': 'げ',
            'o': 'ご',
        }, True),
        'ぶ': ({
            'i': 'び',
            'ta': 'ん',
            'a': 'ば',
            'e': 'べ',
            'o': 'ぼ',
        }, True),
        'す': ({
            'i': 'し',
            'ta': 'し',
            'a': 'さ',
            'e': 'せ',
            'o': 'そ',
        }, False),
        'つ': ({
            'i': 'ち',
            'ta': 'っ',
            'a': 'た',
            'e': 'て',
            'o': 'と',
        }, False),
    }

    def __init__(self, *args: Union[str, Writing, BaseWord]) -> None:

        Word.__init__(self, *args)

        base, ending = self.split_okurigana(1)
        if ending not in self._GODAN_ENDINGS:
            raise ValueError('Not a godan verb')

        forms = ({
            'ta': base + self._GODAN_ENDINGS[ending][0]['ta'],
            'pot': base + self._GODAN_ENDINGS[ending][0]['e'],
            'pas': base + self._GODAN_ENDINGS[ending][0]['a'],
            'cau': base + self._GODAN_ENDINGS[ending][0]['a'],
            'nai': base + self._GODAN_ENDINGS[ending][0]['a'],
            'masu': base + self._GODAN_ENDINGS[ending][0]['i'],
            'imp': base + self._GODAN_ENDINGS[ending][0]['e'],
            'e': base + self._GODAN_ENDINGS[ending][0]['e'],
            'vol': base + self._GODAN_ENDINGS[ending][0]['o'],
            'self': self,
        }, self._GODAN_ENDINGS[ending][1])

        Verb.__init__(self, forms)

class KuruVerb(Verb, Word):
    """The kuru (come) verb."""

    def __init__(self, *args: Union[str, Writing, BaseWord]) -> None:

        Word.__init__(self, *args)

        base_writings = []
        for writing in self.writings:
            ending = writing[-2:]
            if not ending in ('来る', 'くる'):
                raise ValueError('Not a kuru verb')
            if writing[:-2]:
                base_writings.append(writing[:-2])
        self._base = Word(*base_writings) if len(base_writings) > 0 else None

        Verb.__init__(self, ({
            'ta': Word('来', 'き'),
            'pot': Word('来られ', 'こられ'),
            'pas': Word('来ら', 'こら'),
            'cau': Word('来さ', 'こさ'),
            'nai': Word('来', 'こ'),
            'masu': Word('来', 'き'),
            'imp': Word('来い', 'こい'),
            'e': Word('来れ', 'くれ'),
            'vol': Word('来よ', 'こよ'),
            'self': Word('来る', 'くる'),
        }, False))

    def conjugate(
        self,
        forms: Optional[Union[Form, List[Form]]]=None,
        polite: bool=False,
        negative: bool=False
    ) -> BaseWord:

        conj = super().conjugate(forms, polite, negative)
        return self._base + conj if self._base else conj

class SuruVerb(Verb, Word):
    """The suru (do) verb."""

    def __init__(self, *args: Union[str, Writing, BaseWord]) -> None:

        if len(args) > 0:
            self._base: Optional[BaseWord] = Word(*args)
        else:
            self._base = None

        Word.__init__(self, Word('する'))
        Verb.__init__(self, ({
            'ta': Word('し'),
            'pot': Word('でき'),
            'pas': Word('さ'),
            'cau': Word('さ'),
            'nai': Word('し'),
            'masu': Word('し'),
            'imp': Word('しろ'),
            'e': Word('すれ'),
            'vol': Word('しよ'),
            'self': self,
        }, False))

    def conjugate(
        self,
        forms: Optional[Union[Form, List[Form]]]=None,
        polite: bool=False,
        negative: bool=False
    ) -> BaseWord:

        conj = super().conjugate(forms, polite, negative)
        return self._base + conj if self._base else conj

class IkuVerb(GodanVerb):

    def __init__(self, *args: Union[str, Writing, BaseWord]) -> None:

        super().__init__(*args)

        for writing in self.writings:
            ending = writing[-2:]
            if not ending in ('行く', 'いく'):
                raise ValueError('Not an iku verb')

        sbase, _ = self.split_okurigana(1)

        self._forms[0]['ta'] = sbase + 'っ'

class AruVerb(GodanVerb):

    def __init__(self, *args: Union[str, Writing, BaseWord]) -> None:

        super().__init__(*args)

        for writing in self.writings:
            ending = writing[-2:]
            if ending != 'ある':
                raise ValueError('Not an aru verb')

        sbase, _ = self.split_okurigana(2)

        self._forms[0]['nai'] = sbase
