def compare_number_to_fifty(number: int | float) -> None:
    """
    Compares a given number to 50 and prints whether it is greater than 50 or not.

    Args:
        number: The numerical input (integer or float) to compare.

    Returns:
        None. The function prints directly to standard output and has no explicit
        return value.
    """
    if number > 50:
        print(f"The number {number} is greater than 50.")
    else:
        print(f"The number {number} is not greater than 50.")
