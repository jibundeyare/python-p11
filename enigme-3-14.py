# 3.14 Nombre palindromes
#
#  Il y a 18 nombres palindromes non nuls inférieurs à 100 : 1, 2, 3, 4,
# 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88 et 99.
#
#  Combien existe-t-il de nombres palindromes non nuls inférieurs
# à 1 000 000 ?

# méthode 1 : brute force, crible, méthode calculatoire

# le compteur de palindromes
n = 0

for i in range(1, 1000000):
    # conversion du nombre en chaîne de caractères
    i_str = str(i)
    # copie de la chaîne de caractères en sens inverse
    i_str_reversed = i_str[::-1]

    # la chaîne de caractères est-elle identique à la version inversée ?
    if i_str == i_str_reversed:
        # si oui, on incrémente le compteur
        n += 1

print(f'{n = }')

# n = 1998

# méthode 2 : analytique

# @todo détailler la méthode...
