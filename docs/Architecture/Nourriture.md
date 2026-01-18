# La nourriture

La classe `Food` représente les ressources énergétiques dispersées sur la carte. 

## Attributs
| Attribut     | Description                                               |
| :----------- | :-------------------------------------------------------- |
| `x`          | Position x                                                |
| `y`          | Position y                                                |
| `size`       | La taille de l'affichage                                  |
| `color`      | La couleur de la nourriture                               |
| `valeur`     | La valeur nutritive (la quantité de satiété que ça donne) |
| `to_destroy` | indique si la nourriture doit être supprimée              |

## Cycle de vie : 
1. **Apparition** : Généré par l'`Engine` soit au début, soit lors du réaprovisionnement, dans une zone d'abondance ou non.
2. **Consommation** : Lorsqu'un Minos consomme la nourriture, elle est marquée to_destroy. Elle est donc ignorée par les autres Minos avant d'être détruite au prochain tour de boucle. 
3. **Disparition** : La nourriture est marquée to_destroy si elle est mangée ou si elle était dans une zone d'abondance qui vient de se déplacer. A chaque tour de boucle, les nourritures marquées to_destroy ne sont pas régénérées et sont exclues de la grille. 


