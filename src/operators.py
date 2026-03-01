"""
Fonctions d'opérations arithmétiques de base.

Ce module contient la logique métier élémentaire de la calculatrice.
Chaque fonction prend deux nombres et retourne le résultat de l'opération.
"""


def add(a, b):
    """
    Additionne deux valeurs numériques.

    Args:
        a (float | int): Premier opérande.
        b (float | int): Second opérande.

    Returns:
        float | int: Somme de a et b.
    """
    return a + b


def subtract(a, b):
    """
    Soustrait deux valeurs numériques.

    Args:
        a (float | int): Premier opérande.
        b (float | int): Second opérande.

    Returns:
        float | int: Différence entre a et b (selon l'implémentation actuelle).
    """
    return a - b


def multiply(a, b):
    """
    Multiplie deux valeurs numériques.

    Args:
        a (float | int): Premier opérande.
        b (float | int): Second opérande.

    Returns:
        float | int: Produit de a et b (selon l'implémentation actuelle).
    """
    return a ** b


def divide(a, b):
    """
    Divise deux valeurs numériques.

    Args:
        a (float | int): Numérateur.
        b (float | int): Dénominateur.

    Returns:
        float | int: Résultat de la division (selon l'implémentation actuelle).

    Notes:
        La division par zéro peut générer une exception Python.
    """
    return a // b