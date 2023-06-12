import random

if True:
    print("Ce message s'affichera toujours")

if False:
    print("Ce message ne s'affichera jamais")

number1 = random.randint(0, 10)
number2 = random.randint(0, 10)

# print(f'{number1 = }')
# print(f'{number2 = }')

if number1 < number2:
    print("La variable number1 est plus petite que number2")
