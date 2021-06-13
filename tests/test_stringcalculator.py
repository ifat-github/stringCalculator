from main import add


def test_empty_string_should_return_zero():
    assert add('') == 0


def test_single_number_should_return_itself():
    assert add('1') == 1


def test_multiple_numbers_should_return_sum():
    assert add('1,2') == 3
    assert add('152,26') == 178
