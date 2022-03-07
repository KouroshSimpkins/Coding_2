"""Using bitwise operators, write a program that takes an
arbitrary user input and outputs an interesteing manipulation of the input."""


def main():
    """Perform bitwise operators on an input"""
    # Get the input.
    num = input("Enter a number: ")
    # Convert the input to binary.
    num_bin = bin(int(num))[2:]
    # Reverse the input.
    num_bin_rev = num_bin[::-1]
    # Convert the reversed input to decimal.
    num_dec = int(num_bin_rev, 2)
    # Convert the decimal input to hexadecimal.
    num_hex = hex(num_dec)[2:]
    # Convert the hexadecimal input to octal.
    num_oct = oct(num_dec)[2:]
    # Print the results.
    print(f"Binary: {num_bin}")
    print(f"Reversed binary: {num_bin_rev}")
    print(f"Hexadecimal: {num_hex}")
    print(f"Decimal: {num_dec}")
    print(f"Octal: {num_oct}")

    # Print the 2's complement representation of the input.
    print(f"2's complement: {bin(int(num) + 1)[2:]}")

    # Print the 1's complement representation of the input.
    print(f"1's complement: {bin(int(num) * -1)[2:]}")

    # Get a second input.
    num_2 = input("Enter a second number: ")
    # Convert the second input to binary.
    num_2_bin = bin(int(num_2))[2:]
    # Reverse the second input.
    num_2_bin_rev = num_2_bin[::-1]
    # Convert the reversed second input to decimal.
    num_2_dec = int(num_2_bin_rev, 2)
    # Convert the decimal second input to hexadecimal.
    num_2_hex = hex(num_2_dec)[2:]
    # Convert the hexadecimal second input to octal.
    num_2_oct = oct(num_2_dec)[2:]
    # Print the results.
    print(f"Binary: {num_2_bin}")
    print(f"Reversed binary: {num_2_bin_rev}")
    print(f"Hexadecimal: {num_2_hex}")
    print(f"Decimal: {num_2_dec}")
    print(f"Octal: {num_2_oct}")

    # And the two numbers
    print(f"And: {bin(int(num) & int(num_2))[2:]}")

    # Or the two numbers
    print(f"Or: {bin(int(num) | int(num_2))[2:]}")

    # Xor the two numbers
    print(f"Xor: {bin(int(num) ^ int(num_2))[2:]}")

    # Left shift the first number
    print(f"Left shift: {bin(int(num) << int(num_2))[2:]}")

    # Right shift the first number
    print(f"Right shift: {bin(int(num) >> int(num_2))[2:]}")

    # Left shift the second number
    print(f"Left shift: {bin(int(num_2) << int(num))[2:]}")

    # Right shift the second number
    print(f"Right shift: {bin(int(num_2) >> int(num))[2:]}")

    # Print the decimal representation of a left shift
    print(f"Left shift integer: {int(num) << int(num_2)}")

    # Print the decimal representation of a right shift
    print(f"Right shift integer: {int(num) >> int(num_2)}")


if __name__ == "__main__":
    main()
