import sys
sys.path.append("../src")

import encoder
import pytest
import re


def is_word_a_match(pattern, word):
    if re.match(pattern, word):
        return True
    else:
        return False


def test_make_weird_words():
    patterns = ['A', 'v(e|r){2}y', 'l(a|r|g){3}e', 's(e|n|t|e|n|c){6}e']
    weird_words = encoder.make_weird_words(['A', 'very', 'large', 'sentence'])
    result = False
    for i in range(len(weird_words)):
        if is_word_a_match(patterns[i], weird_words[i]):
            result = True
        else:
            result = False
    assert(result)
