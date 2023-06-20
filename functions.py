import library

# définition
def hello():
    print('Hello Python!')

# appel ou exécution
hello()

# paramètre
def hello2(name):
    print(f"Hello {name}!")

hello2('Foo')

# paramètres + retour de valeur
def addition(a, b):
    return a + b

resultat = addition(42, 123)
print(resultat)

# appel d'une fonction stockée dans un autre module
resultat = library.oui_non(False)
print(resultat)
print(library.oui_non(True))

# reverse lookup
my_list = [42, 123, 3.14]

result = library.reverse_lookup(my_list, 3.14)
print(result)
