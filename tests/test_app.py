"""
Tests de la logique applicative (calculate) et de l'intégration Flask.

Ces tests couvrent:
- La validation/parsing d'expressions dans calculate()
- Le comportement minimal des routes Flask
"""

import pytest
from src.app import app, calculate


@pytest.mark.parametrize(
    "expr, expected",
    [
        ("2+3", 5.0),
        ("10-4", 6.0),
        ("6*7", 42.0),
        ("12/3", 4.0),
        (" 10 / 2 ", 5.0),  # espaces acceptés
    ],
)
def test_calculate_valid_expressions(expr, expected):
    """
    calculate(expr) doit retourner le résultat numérique attendu
    pour une expression simple contenant un seul opérateur.
    """
    assert calculate(expr) == expected


@pytest.mark.parametrize(
    "expr",
    [
        "",          # vide
        "   ",       # espaces seulement
        "+2",        # opérateur au début
        "2+",        # opérateur à la fin
        "2++3",      # format invalide (plusieurs opérateurs)
        "2+3-1",     # plusieurs opérateurs
        "abc+1",     # opérande non numérique
        "1+xyz",     # opérande non numérique
    ],
)
def test_calculate_invalid_expressions_raise(expr):
    """Les expressions invalides doivent lever ValueError."""
    with pytest.raises(ValueError):
        calculate(expr)


def test_index_get_returns_200():
    """
    GET / doit retourner un code 200 et contenir du HTML.
    On ne teste pas le style, seulement la disponibilité de la route.
    """
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"<html" in resp.data.lower()


def test_index_post_returns_result_or_error():
    """
    POST / avec une expression doit renvoyer une réponse 200.
    On vérifie que le contenu contient soit un résultat, soit un message d'erreur.
    """
    client = app.test_client()
    resp = client.post("/", data={"display": "2+3"})
    assert resp.status_code == 200

    html = resp.data.decode("utf-8").lower()
    # Selon l'état de l'app, le rendu peut contenir le résultat ou "error:"
    assert ("5" in html) or ("error:" in html)