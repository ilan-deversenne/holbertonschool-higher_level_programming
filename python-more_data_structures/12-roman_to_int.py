#!/usr/bin/python3

def alphabet_to_int(letter):
    letters_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    return letters_int.get(letter, 0)


def roman_to_int(roman_string):
    result = 0
    old_char = ""

    if not isinstance(roman_string, str) or len(roman_string) == 0:
        return None

    for char in roman_string:
        result += alphabet_to_int(char)

        if old_char == "I":
            result -= 2

        old_char = char

    return result
