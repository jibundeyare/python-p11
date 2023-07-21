n = 10000000
a = 123
b = 42
# cette opération ne dépend pas de la variable i
# il est plus efficace de la sortir de la boucle
c = a * b

for i in range(n):
    # quand cette opération est effectuée dans la boucle elle alourdi le nombre d'opération qui sont répétées
    # c = a * b
    result = i * c

# comment lire le nième chiffre d'un nombre ?
# méthode int -> str
# position en partant de la gauche
position = 2
n = 12345789
n_str = str(n)
chiffre = n_str[position]
print(chiffre)

# méthode arithmétique
# position en partant de la droite
position = 5
chiffre = n % 10 ** (position + 1)
chiffre //= 10 ** position
print(chiffre)
