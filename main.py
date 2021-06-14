import re


def add(numbers):
    result = 0
    delimiter = '[,\n]'
    m = re.search(r'\/\/(.)\n(.*)$', numbers, re.IGNORECASE | re.MULTILINE)
    if m:
        delimiter = m.group(1)
        numbers = m.group(2)

    if numbers:
        result = sum([int(x) for x in re.split(delimiter, numbers)])
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    add('')
