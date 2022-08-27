from typing import Optional, Tuple, Dict, List, Callable, Iterable
from mikan.exceptions import ConversionError

__all__ = [
    'to_hiragana',
    'to_katakana',
    'to_romaji',
]

def _is_one_hiragana(char: str) -> bool:
    if (ord(char) < 0x3041) or (ord(char) > 0x309E):
        return False
    return True

def _is_one_katakana(char: str) -> bool:
    if (ord(char) < 0x30A0) or (ord(char) > 0x30FE):
        return False
    return True

def _is_one_kana(char: str) -> bool:
    return _is_one_hiragana(char) or _is_one_katakana(char)

def is_hiragana(string: str) -> bool:
    return all(_is_one_hiragana(char) for char in string)

def is_katakana(string: str) -> bool:
    return all(_is_one_katakana(char) for char in string)

def is_kana(string: str) -> bool:
    return all(_is_one_kana(char) for char in string)

_SYMBOLS = [
    ['a',       'あ',       'ア'],
    ['ba',      'ば',       'バ'],
    ['be',      'べ',       'ベ'],
    ['bi',      'び',       'ビ'],
    ['bo',      'ぼ',       'ボ'],
    ['bu',      'ぶ',       'ブ'],
    ['bya',     'びゃ',     'ビャ'],
    ['byo',     'びょ',     'ビョ'],
    ['byu',     'びゅ',     'ビュ'],
    ['cha',     'ちゃ',     'チャ'],
    ['che',     'ちぇ',     'チェ'],
    ['chi',     'ち',       'チ'],
    ['cho',     'ちょ',     'チョ'],
    ['chu',     'ちゅ',     'チュ'],
    ['da',      'だ',       'ダ'],
    ['de',      'で',       'デ'],
    ['dhi',     'でぃ',     'ディ'],
    ['dhu',     'でゅ',     'デュ'],
    ['dji',     'ぢ',       'ヂ'],
    ['djo',     'ぢょ',     'ヂョ'],
    ['do',      'ど',       'ド'],
    ['du',      'どぅ',     'ドゥ'],
    ['dzu',     'づ',       'ヅ'],
    ['e',       'え',       'エ'],
    ['fa',      'ふぁ',     'ファ'],
    ['fe',      'ふぇ',     'フェ'],
    ['fi',      'ふぃ',     'フィ'],
    ['fo',      'ふぉ',     'フォ'],
    ['fu',      'ふ',       'フ'],
    ['ga',      'が',       'ガ'],
    ['ge',      'げ',       'ゲ'],
    ['gi',      'ぎ',       'ギ'],
    ['go',      'ご',       'ゴ'],
    ['gu',      'ぐ',       'グ'],
    ['gya',     'ぎゃ',     'ギャ'],
    ['gyo',     'ぎょ',     'ギョ'],
    ['gyu',     'ぎゅ',     'ギュ'],
    ['ha',      'は',       'ハ'],
    ['he',      'へ',       'ヘ'],
    ['hi',      'ひ',       'ヒ'],
    ['ho',      'ほ',       'ホ'],
    ['hya',     'ひゃ',     'ヒャ'],
    ['hyo',     'ひょ',     'ヒョ'],
    ['hyu',     'ひゅ',     'ヒュ'],
    ['i',       'い',       'イ'],
    ['ja',      'じゃ',     'ジャ'],
    ['je',      'じぇ',     'ジェ'],
    ['ji',      'じ',       'ジ'],
    ['jo',      'じょ',     'ジョ'],
    ['ju',      'じゅ',     'ジュ'],
    ['ka',      'か',       'カ'],
    ['ke',      'け',       'ケ'],
    ['ki',      'き',       'キ'],
    ['ko',      'こ',       'コ'],
    ['ku',      'く',       'ク'],
    ['kya',     'きゃ',     'キャ'],
    ['kyo',     'きょ',     'キョ'],
    ['kyu',     'きゅ',     'キュ'],
    ['ma',      'ま',       'マ'],
    ['me',      'め',       'メ'],
    ['mi',      'み',       'ミ'],
    ['mo',      'も',       'モ'],
    ['mu',      'む',       'ム'],
    ['mya',     'みゃ',     'ミャ'],
    ['myo',     'みょ',     'ミョ'],
    ['myu',     'みゅ',     'ミュ'],
    ['n',       'ん',       'ン'],
    ["n'yo",    'んよ',     'ンヨ'],
    ['na',      'な',       'ナ'],
    ['ne',      'ね',       'ネ'],
    ['ni',      'に',       'ニ'],
    ['no',      'の',       'ノ'],
    ['nu',      'ぬ',       'ヌ'],
    ['nya',     'にゃ',     'ニャ'],
    ['nyo',     'にょ',     'ニョ'],
    ['nyu',     'にゅ',     'ニュ'],
    ['o',       'お',       'オ'],
    ['pa',      'ぱ',       'パ'],
    ['pe',      'ぺ',       'ペ'],
    ['pi',      'ぴ',       'ピ'],
    ['po',      'ぽ',       'ポ'],
    ['pya',     'ぴゃ',     'ピャ'],
    ['pyo',     'ぴょ',     'ピョ'],
    ['pu',      'ぷ',       'プ'],
    ['pyu',     'ぴゅ',     'ピュ'],
    ['ra',      'ら',       'ラ'],
    ['re',      'れ',       'レ'],
    ['ri',      'り',       'リ'],
    ['ro',      'ろ',       'ロ'],
    ['ru',      'る',       'ル'],
    ['rya',     'りゃ',     'リャ'],
    ['ryo',     'りょ',     'リョ'],
    ['ryu',     'りゅ',     'リュ'],
    ['sa',      'さ',       'サ'],
    ['se',      'せ',       'セ'],
    ['sha',     'しゃ',     'シャ'],
    ['she',     'しぇ',     'シェ'],
    ['shi',     'し',       'シ'],
    ['sho',     'しょ',     'ショ'],
    ['shu',     'しゅ',     'シュ'],
    ['so',      'そ',       'ソ'],
    ['su',      'す',       'ス'],
    ['ta',      'た',       'タ'],
    ['te',      'て',       'テ'],
    ['thi',     'てぃ',     'ティ'],
    ['thu',     'てゅ',     'テュ'],
    ['to',      'と',       'ト'],
    ['tsu',     'つ',       'ツ'],
    ['tu',      'とぅ',     'トゥ'],
    ['u',       'う',       'ウ'],
    ['va',      'ゔぁ',     'ヴァ'],
    ['ve',      'ゔぇ',     'ヴェ'],
    ['vi',      'ゔぃ',     'ヴィ'],
    ['vo',      'ゔぉ',     'ヴォ'],
    ['vu',      'ゔ',       'ヴ'],
    ['wa',      'わ',       'ワ'],
    ['whe',     'うぇ',     'ウェ'],
    ['whi',     'うぃ',     'ウィ'],
    ['who',     'うぉ',     'ウォ'],
    ['wo',      'を',       'ヲ'],
    ['ya',      'や',       'ヤ'],
    ['yo',      'よ',       'ヨ'],
    ['yu',      'ゆ',       'ユ'],
    ['za',      'ざ',       'ザ'],
    ['ze',      'ぜ',       'ゼ'],
    ['zo',      'ぞ',       'ゾ'],
    ['zu',      'ず',       'ズ'],
]

def _tsu(symbols: Iterable[List[str]]) -> Iterable[List[str]]:
    for symbol in symbols:
        romaji, hiragana, katakana = symbol
        yield symbol
        if not romaji[0] in ('a', 'e', 'n', 'i', 'o', 'u'):
            yield [romaji[0] + romaji, 'っ' + hiragana, 'ッ' + katakana]

def _build_enhancer(
    *args: Callable[[Iterable[List[str]]], Iterable[List[str]]]
) -> Callable[[List[List[str]]], Iterable[List[str]]]:

    def _enhance(symbols: Iterable[List[str]]) -> Iterable[List[str]]:
        for func in args:
            symbols = func(symbols)
        return symbols
    return _enhance

def _on_error_fail(todecode: str, string: str) -> Tuple[str, List[str]]:
    raise ConversionError(f"Cannot convert {todecode} in {string}")

def _on_error_ignore(todecode: str, _: str) -> Tuple[str, List[str]]:
    sub = todecode[0]
    return sub, [sub, sub, sub]

_ERRORS = {
    "fail": _on_error_fail,
    "ignore": _on_error_ignore,
}

class Converter:

    def __init__(self) -> None:

        self._symbols: Dict[str, List[str]] = {}

        enhancer = _build_enhancer(_tsu)

        for symbol in enhancer(_SYMBOLS):
            romaji, hiragana, katakana = symbol

            if romaji in self._symbols:
                raise Exception(f'duplicate symbol {romaji}')
            self._symbols[romaji] = symbol

            if hiragana in self._symbols:
                raise Exception(f'duplicate symbol {hiragana}')
            self._symbols[hiragana] = symbol

            if katakana in self._symbols:
                raise Exception(f'duplicate symbol {katakana}')
            self._symbols[katakana] = symbol

        self._symbols['/'] = ['/', '・', '・']
        self._symbols['・'] = ['/', '・', '・']
        self._symbols['-'] = ['-', 'ー', 'ー']
        self._symbols['ー'] = ['-', 'ー', 'ー']

    def next_symbol(self, string: str) -> Tuple[Optional[str], Optional[List[str]]]:

        for length in range(4, 0, -1):
            sub = string[0:length]
            if sub in self._symbols:
                return sub, self._symbols[sub]
        return None, None

    def _convert(self, string: str, index: int, errors: Optional[str]=None) -> str:

        if errors is None:
            errors = "fail"

        todecode = string

        symbols = []
        while todecode:
            sub, symbol = self.next_symbol(todecode)
            if (sub is None) or (symbol is None):
                sub, symbol = _ERRORS[errors](todecode, string)
            symbols.append(symbol[index])
            todecode = todecode[len(sub):]

        return ''.join(symbols)

    def to_romaji(self, string: str, errors: Optional[str]=None) -> str:

        return self._convert(string, 0, errors)

    def to_hiragana(self, string: str, errors: Optional[str]=None) -> str:

        return self._convert(string, 1, errors)

    def to_katakana(self, string: str, errors: Optional[str]=None) -> str:

        return self._convert(string, 2, errors)

def to_katakana(string: str, errors: Optional[str]=None) -> str:
    converter = Converter()
    return converter.to_katakana(string, errors)

def to_hiragana(string: str, errors: Optional[str]=None) -> str:
    converter = Converter()
    return converter.to_hiragana(string, errors)

def to_romaji(string: str, errors: Optional[str]=None) -> str:
    converter = Converter()
    return converter.to_romaji(string, errors)
