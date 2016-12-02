def check_instance(obj, t, msg):
    if not isinstance(obj, t):
        raise ValueError(msg)


def check_integer(obj, msg):
    if not (isinstance(obj, int) or isinstance(obj, long)):
        raise ValueError(msg)


def gcd(a, b):
    # type: (long, long) -> long
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def lcm(a, b):
    # type: (long, long) -> long
    return (a * b) / gcd(a, b)
