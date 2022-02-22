ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyz"

def encode(n):
    try:
        return ALPHABET[n]
    except IndexError:
        raise Exception("cannot encode: %s" % n)

def dec_to_base(dec = 0, base = 16):
    if dec < base:
        return encode(dec)
    else:
        return dec_to_base (dec // base, base) + encode(dec % base)

def decode(s):
    try:
        return ALPHABET.index(s)
    except ValueError:
        raise Exception("cannot decode: %s" % s)

def base_to_dec(s, base = 16, pow = 0):
    if s == "":
        return 0
    else:
        return base_to_dec(s[:-1], base, pow + 1) + decode(s[-1]) * (base ** pow)


def base_to_base(s, base_from = 16, base_to = 10):
    to_decimal = base_to_dec(s, base = base_from)
    from_decimal = dec_to_base(to_decimal, base = base_to)
    return(from_decimal)


def num_system_math(num_1, sys_1, num_2, sys_2, sys_out, operation):
    # Perform math on two given numbers in two different number systems.
    # Output in the number system defined by sys_out.
    def math(num_1, num_2, sys_1, sys_2, sys_out):
        # Convert both numbers to decimal.
        num_1_dec = base_to_dec(num_1, sys_1)
        num_2_dec = base_to_dec(num_2, sys_2)
        # Perform the math.
        if operation == "addition":
            num_out_dec = num_1_dec + num_2_dec
        elif operation == "subtraction":
            num_out_dec = num_1_dec - num_2_dec
        elif operation == "multiply":
            num_out_dec = num_1_dec * num_2_dec
        elif operation == "divide":
            num_out_dec = num_1_dec / num_2_dec
        else:
            raise ValueError("Unknown operation")
        # Convert the output to the desired number system.
        num_out = dec_to_base(num_out_dec, sys_out)
        return num_out

    # Check if the number systems are valid.
    if sys_1 not in range(2, 37) or sys_2 not in range(2, 37) or sys_out not in range(2, 37):
        raise Exception("Invalid number system.")
    # Check if the numbers are valid.
    if base_to_dec(num_1, sys_1) == 0 or base_to_dec(num_2, sys_2) == 0:
        raise Exception("Invalid number.")

    return math(num_1, num_2, sys_1, sys_2, sys_out)


def main():
    """num_to_convert = input("Enter a number to convert: ")
    base_from = int(input("Enter the base of the number: "))
    base_to = int(input("Enter the base to convert to: "))
    print(base_to_base(num_to_convert, base_from, base_to))"""

    print(num_system_math(num_1 = input("Enter the first number: "), sys_1 = int(input("Enter the base of the first number: ")), num_2 = input("Enter the second number: "), sys_2 = int(input("Enter the base of the second number: ")), sys_out = int(input("Enter the base to convert to: ")), operation = input("Enter the operation to perform: ")))

if __name__ == "__main__":
    main()
