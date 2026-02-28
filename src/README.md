# Module Backend (src)

## Raison d’être

Le répertoire `src/` contient la logique backend de l’application.
Il regroupe la configuration du serveur Flask ainsi que la logique métier
responsable du traitement des expressions arithmétiques.

Ce module est le cœur fonctionnel de l’application.

---

## Fichiers principaux

### app.py

Point d’entrée de l’application Flask.

Responsabilités :
- Configuration du serveur Flask
- Définition des routes HTTP
- Traitement des requêtes GET et POST
- Validation et parsing des expressions
- Gestion des erreurs utilisateur
- Rendu du template HTML

La fonction centrale `calculate()` analyse une expression contenant un seul opérateur
et délègue l’opération au module `operators.py`.

---

### operators.py

Module contenant les fonctions arithmétiques de base :

- add(a, b)
- subtract(a, b)
- multiply(a, b)
- divide(a, b)

Ce module sépare la logique métier du reste de l’application
afin d’améliorer la maintenabilité et la testabilité.

---

## Dépendances

- Flask
- Python 3.10+
- Le dossier `templates/`
- Le dossier `static/`

---

## Hypothèses

- Une expression contient exactement un seul opérateur.
- Les opérandes sont convertibles en float.
- La validation complète des cas complexes n’est pas prise en charge.