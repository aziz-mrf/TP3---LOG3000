"""
Serveur Flask pour une calculatrice web.

Ce module configure l'application Flask et expose une route principale ('/')
qui affiche l'interface de calculatrice et traite une expression arithmétique
soumise par l'utilisateur.

L'application supporte une expression contenant exactement un seul opérateur
parmi: +, -, *, /, et deux opérandes numériques (convertibles en float).
"""

from flask import Flask, request, render_template
from .operators import add, subtract, multiply, divide
import os

# Configuration explicite des chemins vers templates/ et static/.
# Utile lorsque app.py est dans un sous-dossier et que les ressources sont
# situées dans le répertoire parent du fichier.
app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), "..", "templates"),
    static_folder=os.path.join(os.path.dirname(__file__), "..", "static"),
)

# Table de correspondance entre un opérateur et la fonction métier.
# Permet d'éviter des if/elif et centralise les opérations supportées.
OPS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(expr: str):
    """
    Évalue une expression arithmétique simple.

    L'expression doit contenir exactement un seul opérateur parmi (+, -, *, /)
    ainsi que deux opérandes (gauche et droite) convertibles en float.

    Args:
        expr (str): Expression à évaluer (ex: "2+3", " 10 / 2 ").

    Returns:
        float | int: Résultat du calcul, tel que défini par operators.py.

    Raises:
        ValueError: Si l'expression est vide, si elle contient plus d'un opérateur,
                    si le format est invalide, ou si les opérandes ne sont pas numériques.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # On retire les espaces pour accepter une saisie "humaine" (ex: "2 + 3").
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Recherche de l'opérateur : on refuse plusieurs opérateurs pour rester
    # dans la portée simple attendue du TP (pas de priorité d'opérateurs).
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Refuse les cas ambigus/incomplets :
    # - opérateur manquant
    # - opérateur en début/fin (ex: "+2", "2+")
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos + 1 :]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    # Délégation de l'opération au module operators.py (logique métier).
    return OPS[op_char](a, b)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Route principale de l'application.

    - GET : affiche la page de calculatrice avec un affichage vide.
    - POST : récupère l'expression dans le champ 'display', tente de la calculer,
      puis réaffiche la page avec le résultat ou un message d'erreur.

    Returns:
        str: HTML rendu à partir du template 'index.html'.
    """
    result = ""
    if request.method == "POST":
        # .get(...) évite une erreur si le champ est absent (robustesse côté serveur).
        expression = request.form.get("display", "")
        try:
            result = calculate(expression)
        except Exception as e:
            # On renvoie une erreur lisible à l'utilisateur plutôt que de planter l'app.
            result = f"Error: {e}"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    # debug=True est pratique en développement, mais à désactiver en production.
    app.run(debug=True)