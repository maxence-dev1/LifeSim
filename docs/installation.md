# Guide d'installation

Suivez ces étapes pour mettre en place l'environnement et utiliser le logiciel sur votre machine locale. 

# 1. Prérequis
Avant de commencer, assurez vous d'avoir installé les éléments suivants : 

- **Python 3.10**
- **Git** 
- **Pip**

# 2. Téléchargement du programme

Clonez le dépôt distant ou télechargez l'archive du projet :

    git clone https://github.com/maxence-dev1/LifeSim.git
    cd LifeSim

# 3. Installation des dépendances

Il est fortement recommandé d'utiliser un ennvironnement virtuel afin de ne pas polluer votre système.

    python -m venv venv

    # (Windows)
    venv\Scripts\activate

    # (Mac/Linux)
    source venv/bin/activate

    pip install -r requirements.txt

# 4. Lancement de la simulation

    python main.py