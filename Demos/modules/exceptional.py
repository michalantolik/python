import sys

DIGIT_MAP = {
    'zero':  '0',
    'one':   '1',
    'two':   '2',
    'three': '3',
    'four':  '4',
    'five':  '5',
    'six':   '6',
    'seven': '7',
    'eight': '8',
    'nine':  '9',
}


def convert(s):
    number = ''
    for token in s:
        number += DIGIT_MAP[token]
    x = int(number)
    return x


def tryConvert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("Conversion succeeded! x =", x)
    except KeyError:
        print("Conversion failed!")
        x = -1
    except TypeError:
        print("Conversion failed!")
        x = -1
    return x


def tryConvertShorter(s):
    x = -1                                      # <<< ----- LOOK HERE
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("Conversion succeeded! x =", x)
    except (KeyError, TypeError):               # <<< ----- LOOK HERE
        print("Conversion failed!")
    return x


def tryConvertShorterNoPrint(s):
    x = -1
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("Conversion succeeded! x =", x)
    except (KeyError, TypeError):
        pass                                    # <<< ----- LOOK HERE
    return x


def tryConvertEvenShorterNoPrint(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("Conversion succeeded! x =", x)
    except (KeyError, TypeError):
        return -1                               # <<< ----- LOOK HERE
    return x


def tryConvertPrintExceptionMessage(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("Conversion succeeded! x =", x)
    except (KeyError, TypeError):
        print(f"Conversion error: {e!r}", file=sys.stderr) # <<< ----- LOOK HERE
        return -1
    return x


def tryConvertReraiseException(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("Conversion succeeded! x =", x)
    except (KeyError, TypeError):
        print(f"Conversion error: {e!r}", file=sys.stderr)
        raise                                              # <<< ----- LOOK HERE
    return x


def string_log(s):
    v = convert(s)
    return log(v)


def tryDivideByZeroReplaceAnotherException(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        raise ValueError()
    
    
def tryDivideByZeroReplaceAnotherExceptionBetter(x, y):
    if y == 0:
        raise ValueError("Cannot divde by zero")
    return x / y  
