"""Create a module that provides the cosecant, secant, and cotangent functions.
Also provide the inverse functions as well."""

import math


def cosecant(x):
    """Return the cosecant of x"""
    return 1 / math.sin(x)


def secant(x):
    """Return the secant of x"""
    return 1 / math.cos(x)


def cotangent(x):
    """Return the cotangent of x"""
    return 1 / math.tan(x)


def inverse_cosecant(x):
    """Return the inverse cosecant of x"""
    return math.asin(1 / x)


def inverse_secant(x):
    """Return the inverse secant of x"""
    return math.acos(1 / x)


def inverse_cotangent(x):
    """Return the inverse cotangent of x"""
    return math.atan(1 / x)


def main():
    """Main function"""
    print("Cosecant: ", cosecant(1))
    print("Secant: ", secant(1))
    print("Cotangent: ", cotangent(1))
    print("Inverse Cosecant: ", inverse_cosecant(1))
    print("Inverse Secant: ", inverse_secant(1))
    print("Inverse Cotangent: ", inverse_cotangent(1))


if __name__ == "__main__":
    main()