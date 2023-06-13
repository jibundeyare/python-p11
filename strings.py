text1 = "lorem"
text2 = 'ipsum'

# concaténation
text3 = "citation : " + text1 + " " + text2 + ", César"
print(text3)

# interpolation avec une f-string
text3 = f"citation : {text1} {text2}, César"
print(text3)

# attention : la concaténantion ne fonctionne qu'avec des str
# solution : convertir les autres types en str
mails = 52
text4 = "Vous avez " + str(mails) + " non lus"
print(text4)

# répétition de texte
text5 = "foo" * 3
print(text5)

# affichage de valeurs arrondies mais sans arrondir la variable
number1 = 10 / 3
text6 = f"10 / 3 est à peu près égal {number1}"
print(text6)
text6 = f"10 / 3 est à peu près égal {number1:.2f}"
print(text6)

# les fonctions associés aux strings
text7 = "foo bar baz foo"

# longueur (length)
print(len(text7))

# compter des mots
print(text7.count('foo'))

# retrouvre l'emplacement d'un mot
position = text7.find('foo')
print(position)

# pour trouver l'occurence suivante, il faut chercher une position plus loin
print(text7.find('foo', position + 1))

# si le mot est absent, la fonction renvoie -1 
position = text7.find('lorem')
print(position)

# remplacement de mots
text7 = text7.replace('foo', 'lorem')
print(text7)

# split & join
list1 = text7.split(' ')
print(list1)

text8 = "+".join(list1)
print(text8)

# documenter une fonction

def ouiNon(value):
    """Cette fonction renvoie :
    - "oui" si la parmètre passé est True
    - "non" si la parmètre passé est False
    - "" dans les autres cas
    
    value bool valeur qui sera transformée en "oui" ou "non"
    return str
    """

    if value == True:
        return "oui"
    elif value == False:
        return "non"

    return ""

# help(ouiNon)
print(ouiNon.__doc__)
