import random

#Create a Dice 1-6
def dice():
    di = random.randint(1,6)
    return di

di = dice()
di2 = dice()
print(f'You have just rolled two dices and the result is: {di} & {di2}.')