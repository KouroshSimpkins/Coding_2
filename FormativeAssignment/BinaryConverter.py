"""Create a module that exposes the underlying binary representation of any primitive typed variables given to it.
(Must cover at least Int, Floats, and Strings in ASCII)"""


def toBinary(denary):
    """Given a number in denary, return the binary value"""
    binary = ""
    while denary > 0:
        binary = str(denary % 2) + binary
        denary = denary // 2
    return binary


def stringToBinary(string):
    """Given a string, return the binary value"""
    binary = ""
    for char in string:
        binary += toBinary(ord(char))
        binary += " "
    return binary


def floatToBinary(float):
    """Given a float, return the binary value"""
    import numpy as np
    int32bits = np.asarray(float, dtype=np.float32).view(np.int32).item()
    return '{:032b}'.format(int32bits)


def main():
    """Main function"""
    dec_val = input("Enter a number to convert: ")
    print(stringToBinary(str(dec_val)))


if __name__ == "__main__":
    main()