import re


class State:
    def __init__(self, result=0, input='', delimiter='[,\n]', numbers=None):
        self.result = result
        self.input = input
        self.delimiter = delimiter
        self.numbers = numbers


def escape_special_chars(delimiter):
    special_chars = '.\+*?[^]$(){}=!|:-'
    if delimiter in special_chars:
        delimiter = '\\' + delimiter
    return delimiter


def get_numbers(state):
    result = [int(x) for x in re.split(state.delimiter, state.numbers)]
    negative_numbers = [x for x in result if x < 0]
    if negative_numbers:
        raise ValueError("negatives not allowed: %s" % negative_numbers)

    state.result = [x for x in result if x < 1001]
    return state.result


def parse_input(state):
    m = re.search(r'\/\/\[?(.*?)\]?\n(.*?)$', state.input, re.IGNORECASE | re.MULTILINE)
    if m:
        state.delimiter = ''.join([escape_special_chars(c) for c in m.group(1)])
        state.numbers = m.group(2)

    return state


def add(input):
    state = State(result=0, input=input, numbers=input)
    state = parse_input(state)
    if state.numbers:
        state.result = sum(get_numbers(state))
    return state.result
