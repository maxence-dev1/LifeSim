# Machine Learning

Ici, vous trouverez un "journal de bord" des principales étapes de la création de mon modèle de Machin Learning. (Cette page me servirat de memento aussi).


## Documentation : 
Voici les ressources que j'ai utilisé pour mon apprentissage :
- https://www.datacamp.com/fr/tutorial/linear-regression-in-python?dc_referrer=https%3A%2F%2Fwww.google.com%2F (sans doute nul)
- https://www.youtube.com/watch?v=CCzGRyO2CTc


## Plan d'action : 
Après des recherches, j'ai trouvé que le modèle de ML qui conviendrait à mon projet et pas trop difficile à prendre en main est le modèle de regression linéaire multiple. Ici, pas de réseaux de neurones difficile, on commence par les bases. 

### 1. Préparation et normalisation
- [ ] Ne garder que les colonnes interessantes (resistance, vitesse, satiété, vision, nb_minos, ratio_food) (X) et time_lived (Y)
- [ ] garder dans un fichier config.json toutes les données de la config par défaut des simulations multiples
- [ ] Standardisation : z = (x-mu)/sigma (écart par rapport à la moyenne au lieu de entre 0 et 1)
- [ ] Mélanger les données et garder 20% pour tester et 80% pour entrainer



## Notes de "cours"

Ici, l'objectif est d'expliquer quels gènes on un rôle important et de prédire le temps de vie d'un Minos en fonction de ses gènes. 


- "Expliquer une variable quantitative Y en fonction de p variables quantitatives x1,...,xp"
- "Prédire de nouvelles valeurs pour Y"
