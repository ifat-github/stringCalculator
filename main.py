import re


def escape_special_chars(delimiter):
    special_chars = '.\+*?[^]$(){}=!|:-'
    if delimiter in special_chars:
        delimiter = '\\' + delimiter
    return delimiter


def get_numbers(delimiter, numbers):
    result = [int(x) for x in re.split(delimiter, numbers)]
    negative_numbers = [x for x in result if x < 0]
    if negative_numbers:
        raise ValueError("negatives not allowed: %s" % negative_numbers)

    result = [x for x in result if x < 1001]
    return result


def parse_input(input):
    numbers = input
    delimiter = '[,\n]'
    m = re.search(r'\/\/\[?(.*?)\]?\n(.*?)$', input, re.IGNORECASE | re.MULTILINE)
    if m:
        delimiter = ''.join([escape_special_chars(c) for c in m.group(1)])
        numbers = m.group(2)

    return delimiter, numbers


def add(input):
    result = 0
    delimiter, numbers = parse_input(input)
    if numbers:
        result = sum(get_numbers(delimiter, numbers))
    return result
