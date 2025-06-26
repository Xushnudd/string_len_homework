def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    a = len(s)
    b = a//2
    if b%2==1:
        return s[b-1:b+1]
    else:
        return s[b]
print(main("cool"))