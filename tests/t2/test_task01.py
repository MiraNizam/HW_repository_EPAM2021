import hw2.hw1

# path_data = "./tests/homework2/data.txt"


def test_longest_diverse_words():
    """Testing that function finds correct words """
    assert hw2.hw1.get_longest_diverse_words("data2.txt") == ['Entwicklung',
                                                              'Forschung',
                                                              'Frauenfrage',
                                                              'Gefährdung',
                                                              'Gesellschaft',
                                                              'Großväter',
                                                              'Inzwischen',
                                                              'praktische',
                                                              'wenngleich',
                                                              'überhaupt']


def test_get_rarest_char():
    """Testing that function finds rarest symbol for document"""
    assert hw2.hw1.get_rarest_char("data2.txt") == "K"


def test_count_punctuation_chars():
    """Testing that function count every punctuation char"""
    assert hw2.hw1.count_punctuation_chars("data2.txt") == 23


def test_count_non_ascii_chars():
    """Testing that function counts every non ascii chars"""
    assert hw2.hw1.count_non_ascii_chars("data2.txt") == 17


def test_get_most_common_non_ascii_char():
    """Testing that function finds most common non ascii char for document"""
    assert hw2.hw1.get_most_common_non_ascii_char("data2.txt") == "ä"
