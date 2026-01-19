# Machine Learning

Ici, vous trouverez un "journal de bord" des principales étapes de la création de mon modèle de Machine Learning. (Cette page me servira de mémento aussi).

D'abord, j'ai créé une nouvelle branche sur GitHub intitulée "V3-ML". Cette branche aura moins d'interface et sera moins "user-friendly" que les autres versions. Cela se déroulera principalement dans la console où l'utilisateur aura le choix de comment remplir ses données. Il pourra choisir l'espérance et la variance de ses attributs. Il pourra aussi choisir le nombre de fois que toutes les simulations vont se répéter pour des données plus solides. Une fois cela fait, le modèle de ML lui dira quels sont les gènes les plus importants dans une simulation pauvre, une simulation équilibrée et une simulation riche (qui seront déjà définies). Le modèle sera capable de prédire sur ces données un échantillon de Minos qui sont susceptibles de survivre le plus longtemps. Enfin, l'utilisateur aura la possibilité de regarder X simulations où les Minos susceptibles de survivre auront un marquage.

Ici, j'ai fait le choix discutable de « linéariser » artificiellement mes données. J'ai modifié les constantes de récompense et de coût afin que mes données soient plus linéaires et qu'il soit plus facile pour moi de créer mon premier modèle de ML.

**À voir :** ajouter du multiprocessing pour plus d'efficacité des simulations

## Documentation

Voici les ressources que j'ai utilisées pour mon apprentissage :
- https://www.datacamp.com/fr/tutorial/linear-regression-in-python?dc_referrer=https%3A%2F%2Fwww.google.com%2F
- https://www.youtube.com/watch?v=CCzGRyO2CTc

## Plan d'action

Après des recherches, j'ai trouvé que le modèle de ML qui conviendrait à mon projet et pas trop difficile à prendre en main est le modèle de régression linéaire multiple. Ici, pas de réseaux de neurones difficiles, on commence par les bases.

### 1. Préparation et normalisation

- [ ] Ne garder que les colonnes intéressantes (résistance, vitesse, satiété, vision, nb_minos, ratio_food) (X) et time_lived (Y)
- [ ] Garder dans un fichier config.json toutes les données de la config par défaut des simulations multiples
- [ ] Standardisation : $z = \frac{x - \mu}{\sigma}$ (écart par rapport à la moyenne au lieu de entre 0 et 1)
- [ ] Mélanger les données et garder 20% pour tester et 80% pour entraîner

## Notes de cours

Ici, l'objectif est d'expliquer quels gènes ont un rôle important et de prédire le temps de vie d'un Minos en fonction de ses gènes.

- "Expliquer une variable quantitative Y en fonction de p variables quantitatives $x_1, \ldots, x_p$"
- "Prédire de nouvelles valeurs pour Y"

## Formule régression simple

Pour tout $i$ de $1$ à $n$ :
$$Y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$$

avec $\varepsilon_i$ iid, $\mathbb{E}(\varepsilon_i) = 0$, $\mathbb{V}(\varepsilon_i) = \sigma^2$

$\varepsilon_i$ correspond à :
- erreur de mesure
- erreur d'échantillonnage
- facteur mal contrôlé (une valeur de x mal mesurée)
- oubli de facteur

**Solution :** introduction de variables supplémentaires pour réduire cette variabilité résiduelle (mieux expliquer Y)

## Définition du modèle de régression multiple

Expliquer une variable réponse Y en fonction de p variables explicatives $x_1, x_2, \ldots, x_p$

Pour tout $i$ de $1$ à $n$ :

$$Y_i = \beta_0 + \beta_1 x_{i1} + \cdots + \beta_j x_{ij} + \cdots + \beta_p x_{ip} + \varepsilon_i$$

avec $\varepsilon_i$ iid, $\mathbb{E}(\varepsilon_i) = 0$, $\mathbb{V}(\varepsilon_i) = \sigma^2$

Le modèle traduit l'influence de chaque variable sur Y :
- **Linéarité du modèle :** linéarité par rapport aux paramètres
- **Additivité :** les effets des variables s'additionnent
- **Modèle polynomial possible :** $Y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_i^2 + \varepsilon_i$ (important pour ne pas étudier que les effets linéaires)

$$\begin{aligned}
Y_1 &= \beta_0 + \beta_1 x_{11} + \cdots + \beta_j x_{1j} + \cdots + \beta_p x_{1p} + \varepsilon_1 \\
\vdots & \quad \vdots \\
Y_i &= \beta_0 + \beta_1 x_{i1} + \cdots + \beta_j x_{ij} + \cdots + \beta_p x_{ip} + \varepsilon_i \\
\vdots & \quad \vdots \\
Y_n &= \beta_0 + \beta_1 x_{n1} + \cdots + \beta_j x_{nj} + \cdots + \beta_p x_{np} + \varepsilon_n
\end{aligned}$$

### Notation matricielle

$$Y = X\beta + E \quad \text{avec } \mathbb{E}(E) = 0, \quad \mathbb{V}(E) = \sigma^2 I_d$$

$$\begin{bmatrix}
Y_1 \\
\vdots \\
Y_i \\
\vdots \\
Y_n
\end{bmatrix}
=
\begin{bmatrix}
1 & x_{11} & \cdots & x_{1j} & \cdots & x_{1p} \\
\vdots & \vdots & & \vdots & & \vdots \\
1 & x_{i1} & & x_{ij} & & x_{ip} \\
\vdots & \vdots & & \vdots & & \vdots \\
1 & x_{n1} & \cdots & x_{nj} & \cdots & x_{np}
\end{bmatrix}
\begin{bmatrix}
\beta_0 \\
\beta_1 \\
\vdots \\
\beta_j \\
\vdots \\
\beta_p
\end{bmatrix}
+
\begin{bmatrix}
\varepsilon_1 \\
\vdots \\
\varepsilon_i \\
\vdots \\
\varepsilon_n
\end{bmatrix}$$

L'objectif est donc d'estimer tous les coefficients $\beta_i$ (le vecteur $\beta$).

## Estimation des paramètres du modèle

Pour estimer les paramètres $\beta$, on va chercher à minimiser l'écart entre une observation et la prévision par le modèle (le tout au carré) :

$$\begin{aligned}
\hat{\beta} &= \underset{\beta_0, \ldots, \beta_p}{\min} \sum_{i=1}^{n} \left( y_i - (\beta_0 + \beta_1 x_{i1} + \cdots + \beta_p x_{ip}) \right)^2 \\
&= \underset{\beta}{\arg\min} \, \| Y - X\beta \|^2 \\
&= \underset{\beta}{\arg\min} \, (Y - X\beta)'(Y - X\beta)
\end{aligned}$$

Minimiser la norme en Y et X$\beta$. Il est possible de trouver les $\beta$ en minimisant cette quantité (dériver cette fonction et annuler la dérivée).

### Dérivée matricielle par rapport à $\beta$

Règles de dérivation : $\frac{\partial(A'Z)}{\partial A} = \frac{\partial(Z'A)}{\partial A} = Z$

$$\begin{aligned}
0 &= \frac{\partial \| Y - X\beta \|^2}{\partial \beta} = \frac{\partial (Y - X\beta)'(Y - X\beta)}{\partial \beta} \\
&= \frac{\partial (Y'Y - Y'X\beta - \beta'X'Y + \beta'X'X\beta)}{\partial \beta} \\
&= -X'Y - X'Y + X'X\beta + X'X\beta \\
&\implies X'X\hat{\beta} = X'Y
\end{aligned}$$

$$\hat{\beta} = (X'X)^{-1}X'Y$$

où le ' désigne la transposée (on inverse les lignes et les colonnes de X).

$X'X$ est inversible quand on a plus de données que de paramètres à estimer ($n > p + 1$). La matrice est en général inversible.

### Propriétés

On veut que $\hat{\beta}$ soit sans biais (en moyenne on ne se trompe pas) :
$$\mathbb{E}(\hat{\beta}) = \beta, \quad \mathbb{V}(\hat{\beta}) = (X'X)^{-1}\sigma^2, \quad \mathbb{V}(\hat{\beta}_j) = [(X'X)^{-1}]_{jj} \sigma^2$$

