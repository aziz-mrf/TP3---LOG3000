# LOG3000-TP3 – Web Arithmetic Application

## Informations générales

**Projet :** LOG3000-TP3 – Web Arithmetic Application
**Équipe :** 69
**Cours :** LOG3000

---

# 1. Description du projet

Ce projet consiste en une application web développée avec **Flask (Python)** permettant d’effectuer des opérations arithmétiques simples à partir d’une interface utilisateur accessible via un navigateur web.

La base de code initiale a été fournie dans un état partiellement documenté et susceptible de contenir des erreurs logiques.
L’objectif du projet est donc double :

1. **Rendre l’application fonctionnelle et fiable**
2. **Appliquer des pratiques professionnelles de développement logiciel**

---

# 2. Portée du projet

L’application permet actuellement d’effectuer :

* Addition (`+`)
* Soustraction (`-`)
* Multiplication (`*`)
* Division (`/`)

### Limitations actuelles

* Une seule opération par expression est supportée.
* Les expressions complexes (ex : `2+3*4`) ne sont pas prises en charge.
* Les opérandes doivent être convertibles en nombres (`float`).

---

# 3. Architecture générale

L’application suit une architecture simple de type :

Frontend (HTML/CSS/JS) → Backend Flask → Logique métier Python

Structure du projet :

```
LOG3000-TP3/
│
├── src/
│   ├── app.py
│   ├── operators.py
│   └── README.md
│
├── tests/
│   ├── test_app.py
│   ├── test_operators.py
│   └── README.md
│
├── templates/
│   ├── index.html
│   └── README.md
│
├── static/
│   ├── style.css
│   └── README.md
│
├── requirements.txt
├── pytest.ini
└── README.md
```

### Description des composants

* **app.py** : Point d’entrée de l’application Flask. Gère les routes et le traitement des expressions.
* **operators.py** : Contient les fonctions arithmétiques.
* **templates/index.html** : Interface utilisateur.
* **static/style.css** : Style visuel de l’application.
* **tests/** : Contient les tests unitaires et d’intégration.
* **tests/test_app.py** : Tests de la fonction `calculate()` et des routes Flask.
* **tests/test_operators.py** : Tests unitaires des opérations arithmétiques.

---

# 4. Prérequis

Avant d’installer le projet, assurez-vous d’avoir :

* Python 3.10 ou supérieur
* pip
* Git
* Un navigateur web moderne

Vérifier vos versions :

```bash
python --version
pip --version
git --version
```

---

# 5. Installation (Étape par étape)

### 1️ Cloner le dépôt

```bash
git clone https://github.com/<organisation>/LOG3000-TP3.git
cd LOG3000-TP3
```

---

### 2️ Créer un environnement virtuel (recommandé)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️ Installer toutes les dépendances

```bash
pip install -r requirements.txt
```

Ce fichier installe :

* Flask (application web)
* pytest (tests automatisés)

---

# 6. Lancer l’application

Depuis la racine du projet :

```bash
python -m src.app
```

Si le serveur démarre correctement, vous verrez :

```
* Running on http://127.0.0.1:5000
```

Ouvrez ensuite votre navigateur à l’adresse :

```
http://127.0.0.1:5000
```

Pour arrêter le serveur :

```
Ctrl + C
```

---

# 7. Utilisation de l’application

## Interface

L’interface comprend :

* Un champ d’affichage (lecture seule)
* Des boutons numériques
* Des opérateurs
* Un bouton `=` pour exécuter le calcul
* Un bouton `C` pour effacer

---

## Exemples valides

| Expression | Résultat attendu |
| ---------- | ---------------- |
| `2+3`      | 5                |
| `10-4`     | 6                |
| `6*7`      | 42               |
| `12/3`     | 4                |

---

## Gestion des erreurs

L’application retourne un message d’erreur si :

* L’expression est vide
* Plusieurs opérateurs sont présents
* L’expression est mal formée
* Les opérandes ne sont pas numériques
* Division par zéro

---

# 8. Tests

Le module `tests/` assure la qualité du code.

Les tests vérifient :

* Les fonctions du module `operators.py`
* La fonction `calculate()`
* Les routes Flask

---

## Exécuter les tests

Depuis la racine du projet :

```bash
pytest
```

Mode détaillé :

```bash
pytest -v
```

Tous les tests doivent passer avant toute fusion dans la branche principale.

---

# 9. Flux de contribution

## Gestion des branches

Chaque correction ou fonctionnalité doit être développée sur une branche distincte.

Format :

```
type/description
```

Exemples :

* `fix/division-error`
* `docs/update-readme`
* `test/add-calculate-tests`

---

## Conventions de commit

Format :

```
type: description
```

Types possibles :

* `feat` : ajoute une nouvelle fonctionnalité.
* `fix` : corrige un bogue.
* `docs` : modifie la documentation.
* `test` : ajoute ou ajuste des tests.
* `refactor` : améliore le code sans changer le comportement.
* `chore` : tâches techniques (config, dépendances, nettoyage).

Exemples :

```bash
git commit -m "fix: correct multiplication behavior"
git commit -m "test: add calculate edge case tests"
```

---

## Pull Requests

Avant toute fusion dans `main` :

1. Créer une Pull Request
2. Décrire les changements
3. Référencer l’issue associée
4. Vérifier que tous les tests passent
5. Obtenir une validation d’un membre de l’équipe

---

## Issues

Tout bogue ou amélioration doit être :

* Documenté dans une Issue
* Assigné à un membre de l’équipe
* Résolu via une branche dédiée

---

# 10. Objectif final

Un développeur n’ayant aucun contexte préalable doit pouvoir :

1. Cloner le dépôt
2. Installer les dépendances
3. Lancer l’application
4. Comprendre la structure du projet
5. Exécuter les tests
6. Contribuer en suivant le workflow défini

---

# Licence

Projet réalisé dans un cadre académique pour le cours LOG3000.
Usage pédagogique uniquement.
