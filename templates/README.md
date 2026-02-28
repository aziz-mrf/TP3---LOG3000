# Module Templates

## Raison d’être

Le dossier `templates/` contient les fichiers HTML utilisés par Flask
pour générer l’interface utilisateur.

Ces fichiers définissent la structure visuelle de l’application.

---

## Fichiers principaux

### index.html

Template principal de la calculatrice.

Responsabilités :
- Afficher l’interface utilisateur
- Fournir un formulaire POST vers le backend
- Afficher le résultat retourné par Flask
- Inclure les scripts JavaScript nécessaires à l’interaction

---

## Dépendances

- Flask (mécanisme de rendu via render_template)
- Le dossier `static/` pour le CSS

---

## Hypothèses

- Le backend fournit une variable `result`
- Les interactions utilisateur passent par les boutons JavaScript
- Le champ d’affichage est en lecture seule