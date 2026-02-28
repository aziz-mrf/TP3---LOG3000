# Module Static

## Raison d’être

Le dossier `static/` contient les ressources statiques utilisées
par l’interface utilisateur.

Ces fichiers ne contiennent aucune logique backend.

---

## Fichiers principaux

### style.css

Feuille de style principale de l’application.

Responsabilités :
- Définir la mise en page générale
- Styliser la calculatrice
- Gérer l’apparence des boutons
- Fournir un retour visuel lors des interactions (hover, active)

---

## Dépendances

- Chargé via url_for('static', filename='style.css') dans index.html
- Aucun lien direct avec la logique backend

---

## Hypothèses

- L’interface HTML respecte les classes définies dans le CSS
- Le rendu visuel est optimisé pour un affichage centré