# Module Tests

## Raison d’être

Le répertoire `tests/` contient l’ensemble des tests automatisés du projet.

Son objectif est de :

- Vérifier le bon fonctionnement des opérations arithmétiques
- Valider la logique de traitement des expressions
- Détecter les bogues présents dans la base de code
- Garantir que les correctifs apportés ne réintroduisent pas d’erreurs

Ce module joue un rôle essentiel dans l’assurance qualité et la stabilité de l’application.

---

## Fichiers principaux

### test_operators.py

Contient les tests unitaires du module `operators.py`.

Responsabilités :
- Vérifier l’addition
- Vérifier la soustraction
- Vérifier la multiplication
- Vérifier la division
- Tester les cas limites (ex. division par zéro)

Ces tests valident la logique métier isolément du reste de l’application.

---

### test_app.py

Contient les tests liés à la logique applicative et aux routes Flask.

Responsabilités :
- Tester la fonction `calculate()`
- Vérifier le comportement face aux expressions invalides
- Tester la route principale `/`
- Vérifier que les requêtes GET et POST fonctionnent correctement

Ces tests assurent que l’intégration backend fonctionne comme prévu.

---

## Dépendances

- Python 3.10+
- pytest
- L’application doit être accessible via le module `src`

Installation de pytest :

```bash
pip install pytest
````

---

## Exécution des tests

Depuis la racine du projet :

```bash
pytest
```

Exécution détaillée :

```bash
pytest -v
```

Tous les tests doivent passer avant toute fusion dans la branche principale.

---

## Hypothèses

* Les opérations doivent respecter le comportement mathématique standard.
* Une expression ne contient qu’un seul opérateur.
* Les erreurs doivent lever des exceptions appropriées.
* Toute modification du code doit conserver la compatibilité avec les tests existants.

---

## Bonnes pratiques

* Ajouter un test pour toute nouvelle fonctionnalité.
* Ajouter un test avant de corriger un bogue (test reproductible).
* Ne jamais fusionner une branche si un test échoue.


