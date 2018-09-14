import sys
sys.path.append("../src")

import decoder
import pytest


def test_make_words_translations():
    result = decoder.make_words_translations(
        ['Two', 'wrdos'], ['Two', 'words'])
    assert result == {'Two': 'Two', 'wrdos': 'words'}
