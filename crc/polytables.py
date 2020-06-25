__author__ = "Barre Kevin"
__maintainer__ = "Barre kevin"
__version__ = "1.0.0"
__credits__ = ["https://foxcub.fr/"]
__email__ = "kevin.barre@epitech.eu"
__status__ = "Production"

from functools import reduce
from ctypes import c_ushort as ushort
to_bytes = int.to_bytes # Limit Method Lookup In A Loop
DI = 0x07    # init CRC Polynomial
# srvp is shift register value population
# Generate polynomial table.
# https://en.wikipedia.org/wiki/Polynomial_code#Example
polyTable = map(lambda srvp:
                reduce(lambda prev, _: (prev << 1) ^ (DI if (prev & 0x80) else 0),
                       range(8), srvp),
                range(256))

# https://en.wikipedia.org/wiki/Cyclic_redundancy_check#Specification
# bigendian = last = [-1] : MSB (most significant bit)
# little endian = first = [0] : LSB (least significant bit)

# Transform PytonInt to 8-bits table
polyTable8Bits = tuple(
    map(lambda srvp:
        to_bytes(srvp, 2, byteorder='little', signed=False)[0],
        polyTable)
)


# CRC-CCITT (0xFFFF)
def crc16CCITT(prev: int, next: int):
    byte = prev >> 8 ^ ord(next)
    byte ^= byte >> 4
    return ushort(prev << 8).value ^ ushort(byte << 12).value ^ ushort(byte << 5).value ^ ushort(byte).value
