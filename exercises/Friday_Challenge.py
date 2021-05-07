#Question - 1
import string


def one(input1,input2):
  if len(input1) > len(input2):
    return input1
  elif len(input2) > len(input1):
    return input2
  elif len(input1) == len(input2):
    return (f'{input1} {input2}')

#Question - 2
def two(arg1):
  if arg1 % 3 == 0 and arg1 % 5 == 0:
    return "fizz buzz"
  elif arg1 % 3 == 0:
    return "fizz"
  elif arg1 % 5 == 0:
    return "buzz"
  else:
    return "null"

#Question - 3
def three(input):
    vowels=0
    for i in input:
        if i in "aeiou":
            vowels=vowels+1
    return vowels

def four(input):
    if "ie" in input:
        return True
    elif "cei" in input:
        return True
    elif "ei" in input:
        return False
    elif "cie" in input:
        return False

#Question - 5
def five(input):
    result = 1
    inp = input+1
    for x in range(1,inp):
        result = result * x
    return(result)

#Question - 6
def six(string, int, char):
    int = int-1
    place = string[int]
    length = len(string)
    if int > length:
        return False
    elif place == char:
        return True
    else:
        return False

#Question - 7
def seven(inputString, char):
    x = inputString.find(char)
    x = x+1
    return x

test = seven("hello", "l")
print(test)

