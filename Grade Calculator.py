'''name = int(input("enter your number: "))
lucky = int(input("enter your lucky number: "))
lucky = int(lucky)
answer = name + lucky
print(answer)
'''

'''def add_calc (x, y):
    answer = x + y
    return answer

def add_calc2 (x,y):
    answer = x * y
    return answer

initial = int(input("enter first number my guy: "))
second = int(input("enter second number my guy: "))

calc1 = add_calc(initial, second)
calc2 = add_calc2(initial, second)
print(calc1)
print(calc2)'''

'''def balance(a, b, c, d):
    balance = a + b + c + d
    return balance

a = int(input("how much money do you have in your bank: "))
b = int(input("how much money do you have in your wallet: "))
c = int(input("how much money do you have in your safe: "))
d = int(input("how much money do you have in assets: "))
final = balance(a,b,c,d)
print(final)'''


'''def value (num):
    if num >= 5:
        return "your value is bigger than 0"
    else:
        return "your value is smaller than 0"

input1 = value(int(input("enter number")))
input2 = value(int(input("enter a second number")))
print(input1)
print(input2)'''


def grade (a, b, c, d):
    print(f'Hello {a}')
    calc = (b+c+d)
    calc2 = (calc / 175)
    calc3 = (calc2 * 100)
    return calc3

name = input("Enter your name: ")
homework = int(input("Enter your homework grade ( /25): "))
assessment = int(input("Enter your assessment grade ( /50): "))
final = int(input("Enter your final grade ( /100): "))

output = grade(name,homework,assessment,final)
print(output)
