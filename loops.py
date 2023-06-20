import random

# while : c'est comme un "if" mais qui est répété
while False:
    print("ce message ne s'affiche pas")

# ctrl+c pour arrêter le programme 
# while True:
#     # continue permet de reprendre au début de la boucle suivante
#     continue
#     print("ce message est affiché en boucle")
#     # break permet de sortir d'une boucle
#     break

# premier tirage
dice = random.randint(1, 6)

while dice != 6:
    print(f"Je n'ai pas tiré un 6, mais un {dice}")
    print("Je recommence un nouveau tirage")
    dice = random.randint(1, 6)

print("J'ai tiré un 6")

# recréation de la boucle for classique avec une boucle while
i = 0
while i < 10:
    print(f'{i = }')
    i += 1

# boucle for classique en python
# 0 est inclus mais 10 est exclu
for i in range(0, 10):
    print(f'{i = }')

# boucle à rebours
for i in range(10, 0, -1):
    print(f'{i = }')
# boucle for each
users = ['foo', 'bar', 'baz']

for user in users:
    print(user)

# enumerate permet de récupérer l'index de chaque élément
for i, user in enumerate(users):
    print(f"{i = }, {user = }")

# boucle for
for i in range(0, len(users)):
    user = users[i]
    print(f"{i = }, {user = }")

# accumulateur
accumulateur = 0
for i in range(1, 11):
    accumulateur += i
    print(f"{i = }")
    print(f"{accumulateur = }")

print()
print(f"{accumulateur = }")

# liste 2D
players = [
    [42000, 46400, 32103],
    [16700, 44667, 57987],
]

line = 0
col = 0
print(players[line][col])

for line_index in range(0, len(players)):
    line = players[line_index]

    for col_index in range(0, len(line)):
        score = line[col_index]

        print(score)

# previous dans une boucle
