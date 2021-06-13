
def add(numbers):
    result = 0
    if numbers:
        result = sum([int(x) for x in numbers.split(',')])
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    add('')