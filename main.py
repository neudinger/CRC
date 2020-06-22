from crc import crc16, crc8
if __name__ == "__main__":
    print(crc8("ss"))
    val = crc8("Hello "+"World", initial=0, finalXorVal=1)
    print(chr(val))
    print(crc16("World"))
    print(crc16("Hello "+"World"))
    val = crc16("Hello "+chr(crc16("World")), initial=0)
    print(val)

