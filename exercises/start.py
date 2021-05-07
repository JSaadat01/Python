'''def sum_double(a, b):
  x = a + b
  if a == b:
    return x*2
  else:
    return x'''

'''def diff21(n):
  x = n - 21
  y = 21 - n
  if n > 21:
    return x*2
  else:
    return y'''



'''def makes10(a, b):
  if a == 10 or b == 10:
    return True
  elif a+b == 10:
    return True
  else:
    return False'''



'''def two_strings(string1,string2):
  if len(string1) > len(string2):
    return string1
  elif len(string2) > len(string1):
    return string2
  elif len(string1) == len(string2):
    return (f'{string1} {string2}')

x = two_strings("h34","hi4")
print(x)'''

'''def fizz_buzz(x):
  if x % 3 == 0 and x % 5 == 0:
    return "fizz buzz"
  elif x % 3 == 0:
    return "fizz"
  elif x % 5 == 0:
    return "buzz"
  else:
    return "null"

num = fizz_buzz(3)
print(num)'''

'''def string(input):
    vowels=0
    for i in input:
        if i in "aeiou":
            vowels=vowels+1
    return vowels

test = string("hello0oae00000")
print(test)'''

'''def values(n):
    return abs(100-n) <=10 or abs(200-n) <= 10

test=values(20)
print(test)'''


'''def not_string(string):
    if "not" in string:
        return (string)
    else:
        return (f'not {string}')

hello = not_string("kebabschocolate")
print(hello)'''

#Question - 4
def four(input):
    if "ie" or "cei" in input:
        return "ok"
    elif "ei" or "cie" in input:
        return "chocolate"
    else:
        return "bye"

test = four("receive")
print(four)








