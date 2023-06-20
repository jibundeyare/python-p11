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

# type hinting
def mult(a: int, b: int) -> int:
    """Cette fonction ...

    a ...
    b ...
    return ...
    """
    return a * b

result = mult(2, 5)
print(result)
# mais les autres types de données passent quand même
# result = mult('abc', 5)

# le nom de la fonction + ses paramètres + sont type de retour = signature de la fonction
# def mult(a: int, b: int) -> int:
