# Mikan

Mikan is a Japanese language manipulation library.

```python
import mikan

eat = mikan.IchidanVerb('食べる', 'たべる')

want_to_eat = eat.conjugate(mikan.Form.TAI)

did_not_want_to_eat = eat.conjugate(mikan.Form.TAI, mikan.Form.PAST, negative=True)

three_small_animals = mikan.Number(3) + mikan.Counter('匹', 'ひき')

cat = mikan.Word('猫', 'ねこ')

sentence = cat + 'が' + three_small_animals + did_not_want_to_eat + 'です'

reading = sentence.readings.pop()

print(sentence) # 猫が3匹食べたくなかったです
print(reading) # ねこがさんびきたべたくなかったです
print(mikan.to_romaji(reading)) # nekogasanbikitabetakunakattadesu
```

## Motivation

I wanted to learn japanese, but it proved to be hard. So I wrote some Python app mixing a dictionary and a SRS system, with generated items (like inflected verbs), to help me. But the code became messy and hard to manage, so I moved the generation code into a Python library. I named it Mikan, because I like how the みかん hiragana looks like (though fruit names tends to be written with katakana...). Now I'm working on this library and my app is kind of stale. And I'm still not speaking japanese.

## Words, writings and readings

In Mikan, most class classes inherits from the `Word` class. A word is a list of writings. Each writing can also be a reading.

For example:
```python
import mikan

# create a word with three writings: 日本, にほん and にっぽん
# にほん and にっぽん are readings too
japan = mikan.Word('日本', 'にほん', 'にっぽん')

print(japan.writings) # ['日本', 'にほん', 'にっぽん']
print(japan.readings) # ['にほん', 'にっぽん']
```

Words can be combined to create compounds:

```python
import mikan

japan = mikan.Word('日本', 'にほん')
cooking = mikan.Word('料理', 'りょうり')

japanese_cooking = japan + cooking
print(japanese_cooking.writings) # ['日本料理', 'にほんりょうり']
print(japanese_cooking.readings) # ['にほんりょうり']
```

## Inflections

### Forms

- `mikan.Form.PRESENT`
- `mikan.Form.PAST`
- `mikan.Form.IMPERATIVE`
- `mikan.Form.TE`
- `mikan.Form.CONDITIONAL_EBA`
- `mikan.Form.CONDITIONAL_RA`
- `mikan.Form.PRESUMPTIVE`
- `mikan.Form.VOLITIONAL`
- `mikan.Form.POTENTIAL`
- `mikan.Form.PASSIVE`
- `mikan.Form.CAUSATIVE`
- `mikan.Form.TAI`
- `mikan.Form.ADVERB`

### Verbs

Verbs have a `conjugate` method that returns the inflected form of a verb.

`conjugate(forms, negative=False, polite=False)`

`forms` can be a form or a list of forms.

### Adjectives

Mikan only has support for i-adjectives yet, available using the `IAdjective` class.

`conjugate(forms, negative=False)`

## Numbers

Numbers are created with the `Number` and can be created from python integers or from kanjis:

```python
import mikan

a1 = mikan.Number(42)
a2 = mikan.Number('四十二')

assert a1 == a2
```

## Counters

Mikan includes a generic class `Counter` and some specific classes for reading exceptions:

- `DayHourCounter` for hours of day counter (よじ, くじ)
- `MonthDayCounter` for days of month counter (ついたち, ふつか, ...)
- `MonthCounter` for months counter (しがつ, しちがつ, ...)
- `TsuCounter` for the generic つ counter (ひとつ, ふたつ, ...)

Combining numbers and counters produce the required reading changes:

```python
import mikan

number = mikan.Number(1)
hon = mikan.Counter('本', 'ほん')

assert 'いっぽん' in (number + hon).readings
```

## Datetime

Mikan has a wrapper for Python `datetime.date` class:

```python
import datetime
import mikan

mikan_date = mikan.Date(datetime.date(year=2020, month=3, day=16))

print(mikan_date) # 2020年3月16日
```

## Romaji

Some functions are provided to convert between romaji and kana:

- `to_romaji` converts string in kana to romaji/hepburn
- `to_hiragana` converts string in romaji/hepburn to hiragana
- `to_katakana` converts string in romaji/hepburn to katakana

```python
import mikan

friday = mikan.to_romaji('きんようび')
kinyoubi = mikan.to_hiragana(friday)

print(friday) # kin'youbi
print(kinyoubi) # きんようび
```
