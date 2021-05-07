import pytest

def word(x):
    if x % 3 == 0:
        ans = "Fizz"
    elif x % 5 == 0:
        ans = "Buzz"
    else:
        x = "null"
    return x

word()