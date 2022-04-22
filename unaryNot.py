"""Get the not value of a string"""


def get_input():
    """Get the input"""
    return input("Enter a value: ")


def split_string():
    """Split a string into a list of letters"""
    word = get_input()
    return list(word)


def get_binary(val):
    """Return the binary value of a letter"""
    return ord(val)


def get_not_val(val):
    """Return the not value of a letter"""
    binary = bin(get_binary(val))[2:]
    not_binary = []
    for i in range(len(binary)): # pylint: disable=consider-using-enumerate
        if binary[i] == "0":
            not_binary.append("1")
        else:
            not_binary.append("0")
    return int("".join(not_binary), 2)


def binary_to_string(val):
    """Convert a binary value to a string"""
    return chr(val)


def main():
    """Perform bitwise operators on an input string"""
    word = split_string()
    not_word = []
    for i in range(len(word)): # pylint: disable=consider-using-enumerate
        not_word.append(binary_to_string(get_not_val(word[i])))

    print(not_word)
    print(word)

    for letter in word:
        print(f"Binary {letter}: {bin(get_binary(letter))[2:]}")

    for letter in word:
        print(f"Not {letter}: {bin(get_not_val(letter))[2:]}")


if __name__ == "__main__":
    main()
