# nombre entier, integer
number1 = 123
number1 = 42
print(number1)

# nombre à virgule flottante, float
number2 = 3.14
number2 = 2.71
print(number2)

# chaîne de caractères, string
text1 = 'foo bar baz'
print(text1)

text2 = "foo bar baz"
print(text2)

# booléen, boolean
python_is_cool = True
print(python_is_cool)

python_is_boring = False
print(python_is_boring)

# valeur nulle, null value 
user_accepted_terms = None
print(None)

# types de données
print(type(number1))
print(type(number2))
print(type(text1))
print(type(text2))
print(type(python_is_cool))
print(type(python_is_boring))
print(type(user_accepted_terms))

# vérification du type de données
print(type(number1) is int)
print(type(number1) is str)

# todo: interroger le type des autres variables...

# transtypage int -> str
# typecasting
print(type(str(number1)))
print(str(number1))

# transtypage int -> bool
print(type(bool(number1)))
print(bool(number1))

# convertie en booléen, la valeur 0 donne False
number3 = 0
print(bool(number3))

# transtypage str -> int
# génère l'erreur : ValueError: invalid literal for int() with base 10: 'foo bar baz'
# print(type(int(text1)))

# il ne peut pas y avoir autre chose qu'un nombre
# dans la chaîne de caractères
# si on veut la convertir en int
text3 = "123456789"
print(type(int(text3)))

# les fonctions de transtypage
# str() convertit vers string
# int() convertit vers integer
# float() convertit vers float
# bool() convertit vers boolean

# chaîne de caractères, string
# cette notation permet d'utiliser des sauts de ligne
text4 = """<div>
    <h1>Titre de premier niveau</h1>
</div>
"""

print(text4)

# \n est équivalent à un saut de ligne
# \t est équivalent à une tabulation
text5 = "<div>\n\t<h1>Titre de premier niveau</h1>\n</div>\n"

print(text5)

# la backslash seul est le caractère d'échappement
# \" est équivalent à une guillemet "
# \\ est équivalent à un back slash \
text6 = "Foo \"Bar\" Baz"
print(text6)

text7 = "C:\\Program Files\\Foo"
print(text7)

# permutez les deux variables a et b en utilisant l'opérateur d'affectation et le nom des variables.
a = 123
b = 42

# permutation des valeurs à l'aide d'une variable temporaire
c = b
b = a
a = c

print(a)
print(b)

# permutation des valeurs à l'aide d'opérations arithmétiques
a = a + b
b = a - b
a = a - b

print(a)
print(b)
