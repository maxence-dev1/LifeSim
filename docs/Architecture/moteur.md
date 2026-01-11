# Architecture du moteur

Cette section détaille le fonctionnement interne de la simulation, du point d'entrée (`main`) jusqu'à la logique du coeur (`Engine`)

---

## 1. Point d'entrée : Main

Le fichier `main.py` a le role de chef d'orchestre, il initialise les composant et gère la boucle principale.

### Boucle principale (`running`)
En simulation simple ou multiple, la boucle principale suit les mêmes étapes:

1. Input : récupération des commandes utilisateur (quitter, echap...)
2. Update logique : Actualise les éléments de la simulation (Minos, nourriture)
3. Vérification des conditions : Vérifie les conditions de fin de simulation
4. Rendu : Appel aux fonctions d'affichage (uniquement si activé)

## 2. Configuration (`SimulationConfig`)

Cette classe centralise les variables globales et le paramétrage. Elle garantit l'initialisation et la juste distributions des variables globale et des constante.

### Paramètre de la simulation :
| Catégorie         | Attribut                   | Description                                      |
| :---------------- | :------------------------- | :----------------------------------------------- |
| **Affichage**     | `full_screen`              | Mode plein écran ou fenêtré.                     |
|                   | `fps`                      | Plafond d'images par seconde (-1 pour illimité). |
|                   | `print_vision`             | Affiche les rayons de vision des Minos.          |
| **Biologie**      | `resistance_mu` / `_sigma` | Loi Normale pour la jauge de faim.               |
|                   | `vitesse_mu` / `_sigma`    | Loi Normale pour la vitesse de déplacement.      |
|                   | `vision_mu` / `_sigma`     | Loi Normale pour la distance de vue.             |
| **Environnement** | `nb_minos`                 | Population initiale.                             |
|                   | `ratio_food`               | Quantité de nourriture disponible par Minos.     |
|                   | `abundance_zone`           | Activation de la zone d'abondance                |


!!! info "Configuration Dynamique" 
    Les méthodes `init_unique_simulation` et `init_several_simulation` génèrent automatiquement les menus permettant à l'utilisateur de modifier ces valeurs sans redémarrer le programme.

## 3. Le Moteur (`Engine`)
La classe `Engine` est le coeur technique. Elle est conçue pour être modulaire et étanche, elle peut fonctionner sans interface graphique.

### Organisation des attributs :
Voici comment les principaux attributs de `Engine` sont structurés :

- **Gestion d'interface** (optionnel) : 
    - `draw`, `screen`, `manager` : référence vers le système d'interface, initialisés uniquement si nécessaire
- **Gestion des entités** : 
    - `minos_list` : liste de tous les Minos de la simulation
    - `food_list`: Liste des nourritures sur la carte
    - `minos_dead` : nombre de Minos mort
- **Mécanisme internes**:
    - `grid` : Référence vers la grille
    - `abundance_zone` : rectangle de la zone d'abondance [x,y,width, height]


### Le temps : 
La simulation utilise les **frames** comme unité de temps. Cela assure que peu importe la puissance de la machine, la simulation reste valable. 

### L'espace : 
Pour optimiser les performances, l'espace est divisé en différents secteurs via une grille. 

!!! info "Optimisation" 
    Au lieu de scanner toute la carte pour trouver sa prochaine destination, le minos va uniquement regarder les cases de la grille où il est actuellement. 

### Fonctions clés : 
- `update_all_minos` : Actualise entierement chaque Minos ainsi que les données à récolter.
- `update_food` : Gère la reconstruction de la grille et l'apparition de la nourriture.
- `update_abundance_zone` : Gère les déplacements de la zone d'abondance.


## Principales fonctions : 
Voici la liste des fonctions interessantes :
différentes fonctions init_ pour initier certaines composantes
update_food : Actualiser la nourriture sur la carte
update_all_minos : Actualise les minos









L'espace : Le monde dans lequel se déroule la simulatione est une carte 2d de taille variable. 
Le temps : La gestion du temps est basées sur les frames. Ainsi, peu importe les performances de la machine, on obtiendra des résultats parlant
