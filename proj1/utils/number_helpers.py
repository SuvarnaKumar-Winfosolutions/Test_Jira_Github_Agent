def classify_number_parity(number: int) -> str:
    """
    Determines if a given integer is odd or even.

    Args:
        number (int): The integer value to classify.

    Returns:
        str: "even" if the number is even, "odd" if the number is odd.

    Raises:
        TypeError: If the input 'number' is not an integer.

    Examples:
        >>> classify_number_parity(4)
        'even'
        >>> classify_number_parity(7)
        'odd'
        >>> classify_number_parity(0)
        'even'
        >>> classify_number_parity(-2)
        'even'
        >>> classify_number_parity(-3)
        'odd'
    """
    if not isinstance(number, int):
        raise TypeError(f"Input must be an integer, got {type(number).__name__}")

    if number % 2 == 0:
        return "even"
    else:
        return "odd"
