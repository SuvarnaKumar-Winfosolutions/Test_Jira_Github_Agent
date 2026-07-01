from typing import Union

def is_negative_number(number: Union[int, float]) -> str:
    """
    Determines if a given number is negative and returns a human-readable string.

    This function accepts either an integer or a float and checks if its value
    is less than zero.

    Args:
        number (Union[int, float]): The numeric input to check.

    Returns:
        str: A string indicating whether the number is negative.
             - If negative: "{number} is a negative number."
             - If zero or positive: "{number} is not a negative number."

    Examples:
        >>> is_negative_number(-15)
        '-15 is a negative number.'
        >>> is_negative_number(0)
        '0 is not a negative number.'
        >>> is_negative_number(10)
        '10 is not a negative number.'
        >>> is_negative_number(-0.5)
        '-0.5 is a negative number.'
        >>> is_negative_number(5.2)
        '5.2 is not a negative number.'
    """
    if number < 0:
        return f"{number} is a negative number."
    else:
        return f"{number} is not a negative number."
