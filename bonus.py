import random

users = ['foo', 'bar', 'baz']

# boucle for classique
# cette boucle est la même que celle de js
# for (let i = 0, i < n; i++) {}
for i in range(len(users)):
    print(i, users[i])

# boucle for classique avec un pas de 2 (step)
# seule cette boucle permet de sauter des éléments dans une liste
for i in range(0, len(users), 2):
    print(i, users[i])

# boucle for each
for user in users:
    print(user)

# boucle for each avec enumerate
# équivalent fonctionnel de la boucle for classique
# mais celle-ci est préférée par les codeurs python
for i, user in enumerate(users):
    print(i, user)

# une boucle while
while True:
    r = random.randint(1, 100)
    print(r)

    if r == 100:
        break

# équivalent fonctionnel de la boucle while précédente
r = random.randint(1, 100)
print(r)

while r != 100:
    r = random.randint(1, 100)
    print(r)

text1 = 'foo bar baz foo'


