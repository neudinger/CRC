# /usr/bin/env python3
__author__ = "Barre Kevin"
__maintainer__ = "Barre kevin"
__version__ = "1.0.0"
__credits__ = ["Stanislas de Maigret (INA-engineer)",
               "https://foxcub.fr/"]
__email__ = "kevin.barre@epitech.eu"
__status__ = "Production"
__contact__ = "https://www.linkedin.com/in/kevin-barre-neudinger/"
__license__ = "EUPL"


from functools import reduce

# 9 bits (CRC-8)


def crc8(string: str, initial: int = 0, finalXorVal: int = 0) -> int:  # byte or char
    """Return the CRC-8 of string.
    8-bits Int

    Parameters:
    string      (int): input string
    initial     (int): initial value default 0
    finalXorVal (int): final xor default 0

    Returns:
    int: Returning int

    crc8() returns crc8 of the string.
    chr(crc8("")) print coresponding char
    string cannot be None

    >>> crc8("foo")
    132
    >>> crc8()
    Traceback (most recent call last):
    ...
    TypeError: crc8() missing 1 required positional argument: 'string'
    >>> crc8("foo", 1)
    239
    >>> three = crc8("Hello "+"World", initial=0, finalXorVal=1)
    >>> chr(three)
    '$'
    >>> values = crc8("foo")
    >>> values = crc8("bar"+chr(values))
    >>> chr(values)
    'Ê'
    """
    try:
        from polytables import polyTable8Bits
    except ImportError:
        from .polytables import polyTable8Bits
    return int(reduce(lambda prev, next: polyTable8Bits[(
        prev ^ ord(next)) & 0xFF], string, initial) ^ finalXorVal)

# CRC-CCITT (0xFFFF)


def crc16(string: str, initial: int = 0xFFFF) -> int:  # 2 bytes
    """Return the CRC-8 of string.
    8-bits Int

    Parameters:
    string      (int): input string
    initial     (int): initial value default 0xFFFF

    Returns:
    int: Returning int

    crc16() returns crc16CCITT of the string.
    string cannot be None

    >>> crc16("foo")
    25354
    >>> crc16()
    Traceback (most recent call last):
    ...
    TypeError: crc16() missing 1 required positional argument: 'string'
    >>> crc16("foo", 1)
    40103
    >>> three = crc16("Hello "+"World", initial=0)
    >>> three
    39210
    >>> values = crc16("foo")
    >>> values = crc16("bar"+chr(values))
    >>> chr(values)
    '遠'
    """
    try:
        from polytables import crc16CCITT
    except ImportError:
        from .polytables import crc16CCITT
    return reduce(crc16CCITT, string, initial)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
