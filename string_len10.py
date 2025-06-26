def main(s):
    """
    A string of length three is given. Check that it is a palindrome.
    Return True if the palindrome is False otherwise

    Args:
        s: str
    Returns:
        bool: answer
    """
    s = len(s)
    if s==3:
        return True
    else:
        return False
print(main('0pm'))