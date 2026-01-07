# 🛒 Python Shopping List Manager

### 👤 Développeur : Enzo Méresse
**Bachelor 3 Administrateur Systèmes, Réseaux et Bases de Données (ASRBD) | EPSI**

---

## 📖 Présentation du projet
Ce projet est un utilitaire en ligne de commande (CLI) développé en **Python** permettant de gérer de manière interactive une liste de courses. 

Conçu dans le cadre de mon apprentissage du scripting, il démontre la maîtrise des structures de données fondamentales (`dict`, `list`) et la mise en œuvre de contrôles de saisie robustes. L'objectif est de garantir la stabilité du programme face aux erreurs de saisie utilisateur, une compétence clé pour l'automatisation en environnement SysOps.

## 🛠️ Fonctionnalités
L'application propose un menu interactif complet :
* **Ajout dynamique** : Insertion de nouveaux produits avec gestion des quantités.
* **Suppression intuitive** : Retrait d'articles via leur index numérique pour éviter les erreurs de frappe.
* **Modification en temps réel** : Mise à jour rapide des quantités pour les produits déjà présents.
* **Visualisation formatée** : Affichage propre, trié et numéroté de l'ensemble de la liste.
* **Sécurisation des entrées** : Utilisation de la méthode `.isdigit()` pour valider chaque saisie numérique, empêchant ainsi les plantages de type `ValueError`.
