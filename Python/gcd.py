import math

# Greater Common Divider algorithm implementation.

def naive_gcd(a, b):
    if a < 0 or b < 0:
        raise ValueError('Parameters should be greater or equal then zero.')

    if a == 0: return b
    if b == 0: return a

    result = 1
    minAB = min(a, b)

    for i in range (2, minAB + 1):
        if a % i == 0 and b % i == 0:
            result = i

    return result


def euclid_gcd(a, b):
    if a == 0: return b
    if b == 0: return a

    if a >= b:
        return euclid_gcd(a % b, b)
    else:
        return euclid_gcd(a, b % a)
