import re


def get_delimiter(str):
    delimiter = '[,\n]'
    special_chars = '.\+*?[^]$(){}=!|:-'
    m = re.search(r'\/\/(.)', str, re.IGNORECASE | re.MULTILINE)
    if m:
        delimiter = m.group(1)
        if delimiter in special_chars:
            delimiter = '\\' + delimiter
    return delimiter


def parse_numbers(input):
    numbers = input
    m = re.search(r'\/\/.\n(.*)$', input, re.IGNORECASE | re.MULTILINE)
    if m:
        numbers = m.group(1)
    return numbers


def add(input):
    result = 0
    numbers = parse_numbers(input)
    delimiter = get_delimiter(input)

    if numbers:
        result = sum([int(x) for x in re.split(delimiter, numbers)])
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    add('1,2')
