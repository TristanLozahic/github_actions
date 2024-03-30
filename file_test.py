import pytest

def test_calc_addition():
  # Fonction test du résultat de 2+4
    output = 2+4
    assert output == 6

def test_calc_substraction():
  # Fonction test du résultat de 2-4
    output = 2-4
    assert output == -2

def test_calc_multiply():
  # Fonction test du résultat de 2*4
    output = 2*4
    assert output == 8

def test_coucou():
  # Fonction test si la résultat renvoie 'hello'
    output='hello'
    assert output == 'hello'


def total(liste):
    """ renvoie la somme des éléments d'une liste """

    result : float = 0.0

    for item in liste:
        result += item

    return (result)



# Vérifie le fonctionnement de base :
print(total([1, 2 ,3]) == 5)

# Vérifie que la somme marche avec un nombre négatif et un positif :
print(total([1, -1]) == 0)

# Vérifie que la somme marche avec deux négatifs :
print(total([-1, -1]) == -2)

# Vérifie que la somme marche avec un seul élément :
print(total([1]) == 1)

# Vérifie que la liste vide renvoie bien 0 :
print(total([]) == 0)