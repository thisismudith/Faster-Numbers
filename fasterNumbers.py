from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from math import log
import sys


REF = ascii_lowercase  # The reference string
BASE = len(REF)


def lengthPossiblity(n: int = 1, start: int = 0, length: bool = True) -> int:
    """Gives the total possible numbers with character length

    Args:
        n (int, optional): The value. Defaults to 1.
        length(bool, optional): Treats n as length if true, else total possiblities. Defaults to True.

    Returns:
        int: The total possible numbers that can be written

    Note:
        → This function depends on the software capabilities.
        → Based upon the calculating of the CPU, the length of accuracy might change (if Alternate chosen).
    """

    if length:  # Get total numbers that can be written
        return sum(BASE ** (i + 1) for i in range(n)) + (start - 1)
        # return int(BASE/(BASE-1) * (BASE**n - 1)) + (start - 1) [Alternate but less accurate]
    else:  # Get number of characters required
        return int(log((n * (BASE - 1) / BASE) + 1, BASE)) + start


def charToNum(char: str, start: int = 0) -> int:
    """Converts the given character into numbers where:
        Usually, BASE = 26
        a = start ; z = start + BASE - 1 ; aa = start + BASE and so on...

    Args:
        char (str): The string input
        start (int, optional): Default value for a. Defaults to 0.

    Returns:
        int: The converted number
    """

    res = start - 1
    for i, c in enumerate(char[::-1]):
        res += (REF.index(c) + 1) * BASE**i

    return res


def numToChar(num, start: int = 0) -> str:
    """Converts the given number into characters:
        Usually, BASE = 26
        a = start ; z = start + BASE - 1 ; aa = start + BASE and so on...

    Args:
        num (int): The string input
        start (int, optional): Default value for a. Defaults to 0.

    Returns:
        str: The converted char
    """
    if num < start:
        raise Exception("The number can't be smaller or equal to the starting index.")

    num -= start - 1

    q, r = num, None
    res = ""
    while q > 0:
        q, r = divmod(q, BASE)
        res += REF[r - 1]
        if r == 0:
            q -= 1

    return res[::-1]