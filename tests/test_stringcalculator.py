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


# def test_different_delimiters():
#     assert add('//;\n1;2') == 3
#     assert add('//a\n1a2') == 3
#     assert add('//?\n1?2') == 3
