"""Convert a decimal number to binary using only builtin functions"""

def toBinary(denary):
    """Given a number in denary, return the binary value"""
    binary = ""
    while denary > 0:
        binary = str(denary % 2) + binary
        denary = denary // 2
    return binary


def main():
    """Main function"""
    dec_val = input("Enter a number to convert: ")
    print(toBinary(int(dec_val)))


if __name__ == "__main__":
    main()
