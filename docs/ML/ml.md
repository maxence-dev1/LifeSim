# Machine Learning

Ici, vous trouverez un "journal de bord" des principales étapes de la création de mon modèle de Machin Learning. (Cette page me servirat de memento aussi).


D'abord, j'ai créé une nouvelle branche sur github intitulée "V3-ML". Cette branche aura moins d'interface et sera moins "user-friendly" que les autres versions. Cela se déroulera principalement dans la console ou l'utilisateur aura le choix de comment remplir ses données. Il pourra choisir l'esperence et la variance de ses attributs. Il pourra aussi choisir le nombre de fois que toutes les simulations vont se répeter pour des données plus solides. Une fois cela fait, le modèle de ML lui dira quels sont les gènes les plus important dans une simulation pauvre, une simulation équilibrée et une simulation riche (qui seront déjà définies). Le modèle sera capable de prédire sur ces données un échantillon de Minos qui sont susceptible de survivre le plus longtemps.  Enfin, l'utilisateur aura la possibilité de regarder X simulations où les Minos susceptibles de survivre auront un marquage.

Ici, je fais le choix de ne pas modifier ma simulation pour rendre les données linéaires. J'aimerai avoir des données plus claires avec des constantes correctes mais c'est un peu brouillon. je laisse donc mes données en forme de cloche. C'est le modèle de ML qui devra s'adapter à ces données. 


A voir : ajouter du multi processing pour plus d'efficacité des simulations

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
