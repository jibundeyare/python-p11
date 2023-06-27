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
