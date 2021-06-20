import re


def escape_special_chars(delimiter):
    special_chars = '.\+*?[^]$(){}=!|:-'
    if delimiter in special_chars:
        delimiter = '\\' + delimiter
    return delimiter


def validate_numbers(numbers):
    negative_numbers = [x for x in numbers if x < 0]
    if negative_numbers:
        raise ValueError("negatives not allowed: %s" % negative_numbers)


def filter_numbers(numbers):
    return [x for x in numbers if x < 1001]


def get_numbers(delimiter, numbers):
    if not numbers:
        return []
    return [int(x) for x in re.split(delimiter, numbers)]


def parse_input(s, delimiter='[,\n]'):
    numbers = s
    m = re.search(r'\/\/\[?(.*?)\]?\n(.*?)$', s, re.IGNORECASE | re.MULTILINE)
    if m:
        delimiter = ''.join([escape_special_chars(c) for c in m.group(1)])
        numbers = m.group(2)

    return delimiter, numbers


def add(s):
    delimiter, raw_numbers = parse_input(s)
    numbers = get_numbers(delimiter, raw_numbers)
    validate_numbers(numbers)
    filtered_numbers = filter_numbers(numbers)
    return sum(filtered_numbers)
