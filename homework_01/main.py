def power_numbers(*numbers):

    squares = [number ** 2 for number in numbers if isinstance(number, int)]
    return squares


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def filter_numbers(numbers, filter_type):

    if filter_type == ODD:
        return [number for number in numbers if number % 2 != 0]
    elif filter_type == EVEN:
        return [number for number in numbers if number % 2 == 0]
    elif filter_type == PRIME:
        return [number for number in numbers if is_prime(number)]
