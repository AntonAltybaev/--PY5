from random import sample

SYMBOLS = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz0123456789'


def get_random_password(n: int) -> str:
    return ''.join(sample(SYMBOLS, n))


print(get_random_password(10))
