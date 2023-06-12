import random

if True:
    print("Ce message s'affichera toujours")

if False:
    print("Ce message ne s'affichera jamais")

number1 = random.randint(0, 10)
number2 = random.randint(0, 10)

print(f'{number1 = }')
print(f'{number2 = }')

# block if1
if number1 < number2:
    print("La variable number1 est plus petite que number2")

# block if2
if number1 < number2:
    print("La variable number1 est plus petite que number2")
else: # number1 >= number2
    print("La variable number1 est plus grande ou égale à number2")

# block if3
if number1 < number2:
    print("La variable number1 est plus petite que number2")
elif number1 > number2:
    print("La variable number1 est plus grande que number2")
else:
    print("Les deux variables number1 et number2 sont égales")

# elif == else if

# block if4
# réécriture du block if3 avec des if imbriqués
if number1 < number2:
    print("La variable number1 est plus petite que number2")
else:
    if number1 > number2:
        print("La variable number1 est plus grande que number2")
    else:
        print("Les deux variables number1 et number2 sont égales")

# opérateurs booléens

# négation
print(not True)
print(not False)

# table de vérité de l'opérateur de négation
# A     not A
# True  False
# False True

# OU logique
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# table de vérité de l'opérateur OU logique
# A     B       A or B
# True  True    True
# True  False   True
# False True    True
# False False   False

# pour retrouver la table, remplacez :
# - A par "j'ai du cash"
# - B par "j'ai ma cb"
# - "A or B" par "puis-je faire mes courses ?"

# ET logique
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# table de vérité de l'opérateur ET logique
# A     B       A and B
# True  True    True
# True  False   False
# False True    False
# False False   False

# table de vérité de l'opérateur NAND (not and)
# A     B       A and B     not (A and B)
# True  True    True        False
# True  False   False       True
# False True    False       True
# False False   False       True
