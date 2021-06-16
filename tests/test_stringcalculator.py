import pytest

from main import add


def test_empty_string_should_return_zero():
    assert add('') == 0


def test_single_number_should_return_itself():
    assert add('1') == 1


def test_multiple_numbers_should_return_sum():
    assert add('1,2') == 3
    assert add('152,26') == 178
    assert add('1,2,3') == 6


def test_newline_delimiters():
    assert add('1\n2,3') == 6


def test_different_delimiters():
    assert add('//;\n1;2') == 3
    assert add('//a\n1a2') == 3
    assert add('//?\n1?2') == 3
    assert add('//$\n1$2') == 3


def test_negative_number_throws_exception():
    with pytest.raises(Exception) as e_info:
        add('-1')

    assert str(e_info.value) == "negatives not allowed: [-1]"


def test_negative_numbers_throw_exception():
    with pytest.raises(Exception) as e_info:
        add('//$\n1$2$-1$-2$3')

    assert str(e_info.value) == "negatives not allowed: [-1, -2]"


def test_add_1000():
    assert add('1,1000') == 1001


def test_ignore_numbers_bigger_than_1000():
    assert add('2,1001') == 2


def test_multiple_chars_delimiter():
    assert add('//[www]\n1www2www3') == 6


def test_multiple_special_chars_delimiter():
    assert add('//[***]\n1***2***3') == 6
