import sys
from fractions import Fraction
# TODO: Do not use fractions module.
for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    frac = Fraction(a, b)
    x = 0
    while frac.numerator != 1:
        x = frac.denominator // frac.numerator + 1
        frac -= Fraction(1, x)
    print(frac.denominator)
