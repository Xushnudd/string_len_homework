def main(num1, num2):
    """
    Given two non-negative integers, num1 and num2 represented as string.
    Return the sum of num1 and num2 as a string.

    Args:
        num1: str
        num2: str
    Returns:
        str: answer
    """
    a = len(num1)
    b = len(num2)
    return a*b
print(main('salom', "yaxshi"))