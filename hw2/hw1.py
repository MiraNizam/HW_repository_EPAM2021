"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from collections import namedtuple
from unicodedata import category
from typing import List
import string

Token = namedtuple("Token", ['type', 'value'])


def tokenize(file_input):
    """ Return tokens"""
    buffer = ""
    symbol = file_input.read(1)
    while symbol:
        if symbol == "":
            break
        if category(symbol).startswith("L"):
            buffer += symbol
            symbol = file_input.read(1)
            continue
        if symbol == "-":
            symbol = file_input.read(1)
            if symbol == "\n":
                symbol = file_input.read(1)
                buffer += symbol
                symbol = file_input.read(1)
            continue
        if buffer:
            yield Token("word", buffer)
            buffer = ""
        yield Token("symbol", symbol)
        symbol = file_input.read(1)
    yield Token("word", buffer)


def get_longest_diverse_words(file_name: str) -> List[str]:
    """Find 10 longest words consisting from largest amount of unique symbols"""
    unique_words = {}
    with open(file_name, mode="r", encoding='unicode-escape') as fi:
        for token in tokenize(fi):
            if token.type != "word":
                continue
            if len(unique_words) < 10:
                unique_words[token.value] = len(set(token.value))
            else:
                min_value = min(unique_words, key=lambda x: unique_words[x])
                if len(set(token.value)) > unique_words[min_value]:
                    del unique_words[min_value]
                    unique_words[token.value] = len(set(token.value))
                else:
                    continue
    return sorted(unique_words.keys())


def get_rarest_char(file_name: str) -> str:
    """Find rarest symbol for document"""
    chars = {}
    with open(file_name, mode="r", encoding='unicode-escape') as fi:
        for char in fi.read():
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
    return min(chars, key=lambda x: chars[x])


def count_punctuation_chars(file_name: str) -> int:
    """Count every punctuation char"""
    punctuation_counter = 0
    with open(file_name, mode="r", encoding='unicode-escape') as fi:
        for punctuation in fi.read():
            if punctuation in string.punctuation:
                punctuation_counter += 1
    return punctuation_counter


def count_non_ascii_chars(file_name: str) -> int:
    """ Count every non ascii char """
    non_ascii_chars_counter = 0
    with open(file_name, mode="r", encoding='unicode-escape') as fi:
        for char in fi.read():
            if not char.isascii():
                non_ascii_chars_counter += 1
    return non_ascii_chars_counter


def get_most_common_non_ascii_char(file_name: str) -> str:
    """Find most common non ascii char for document"""
    chars = {}
    with open(file_name, mode="r", encoding='unicode-escape') as fi:
        for char in fi.read():
            if not char.isascii():
                if char not in chars:
                    chars[char] = 1
                else:
                    chars[char] += 1
    return max(chars, key=lambda x: chars[x])
