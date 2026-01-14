#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def main():
    last_digit = number % 10
    if number < 0:
        last_digit = ((number * -1) % 10 * -1)

    end = ""

    is_zero = "and not 0"
    if last_digit == 0:
        is_zero = "and is 0"
        end = is_zero
    else:
        greater_or_less = ""
        if last_digit > 5:
            greater_or_less = "and is greater than 5"
        elif last_digit < 6:
            greater_or_less = f"and is less than 6 {is_zero}"

        end = greater_or_less

    print(f"Last digit of {number} is {last_digit} {end}")


if __name__ == "__main__":
    main()
