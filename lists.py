empty_list = []
users = ['foo', 'bar', 'baz']
mix = [True, 3.14, 'lorem ipsum', None, [123, 42]]

mix = [
    True,
    3.14,
    'lorem ipsum',
    None,
    [123, 42]
]

# accès en lecture
# 0 est l'index du premier élément
print(users[0])

# len - 1 est l'index du dernier élément
i = len(users) - 1
print(users[i])

# l'index dépasse la taille de la liste
# IndexError: list index out of range
# print(users[100 + 42 - i])

# accès en écriture
users[0] = 'lorem'

# ajouter un nouvel élément à la fin
users.append('ipsum')
print(users)

# ajouter un nouvel élément au début ou au milieu
users.insert(0, 'sit')
users.insert(2, 'dolores')
print(users)

# retrait du dernier élément
last_user = users.pop()
print(last_user)
print(users)

# retrait par index
first_user = users.pop(0)
print(first_user)
print(users)

# suppression par valeur
users.remove('bar')
print(users)

fruits = ['ananas', 'banane', 'cerise']
legumes = ['artichaud', 'brocoli', 'carotte']
ingredients = fruits + legumes
print(ingredients)

fruits += legumes
print(fruits)

numbers = ['g', 'd', 'a', 'c', 'b', 'Z']
numbers = sorted(numbers)
print(numbers)
