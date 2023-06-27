# scope = portée des variables

my_var1 = 123

def my_func1():
    print(my_var1)
    print(my_var2)

my_var2 = 42

# la fonction voit les variables définies à l'extérieur, au préalable ou à posteriori
my_func1()

def my_func2():
    my_var3 = 3.14

my_func2()

# il n'est pas possible d'accéder à une variable définie à l'intérieur d'une fonction, que celle-ci ait été exécutée ou non
# principe du verre tinté (comme avec une limousine)
# NameError: name 'my_var3' is not defined.
# print(my_var3)

my_var4 = 'foo'

def my_func3(my_var4):
    # le paramètre my_var4 masque la variable définie à l'extérieur de la fonction
    print(my_var4)

# cet appel affiche 'bar'
my_func3('bar')

my_var4 = 'foo'

def my_func4():
    # la variable my_var4 fait de l'ombre (shadowing) à la variable définie à l'extérieur de la fonction
    my_var4 = 'baz'
    print(my_var4)

my_func4()
# la variable my_var4 définie à l'extérieur de la fonction reste inchangée
print(my_var4)

def my_func5(my_var5):
    my_var5 = 'foo'
    print(my_var5)

my_var6 = 123
# les variables de type int, float, bool ou str sont passées par valeur
# c-à-d que la fonction ne peut pourra accéder qu'à une copie de la variable originale définie à l'extérieur 
my_func5(my_var6)
print(my_var6)

def my_func6(my_var7: list):
    my_var7.append('foo')

my_var8 = [123, 42, 3.14]
# les variables de type list, dict, tuple ou objet sont passées par référence
# c-à-d que la fonction pourra accéder à la variable originale définie à l'extérieur 
my_func6(my_var8)
print(my_var8)
