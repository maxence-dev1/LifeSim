import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True, precision=3)

def main():
    print("lecture des données...")
    df = pd.read_csv("data.csv")
    print("création des matrices...")
    df["vitesse2"] = df["vitesse"]**2
    df["un"] = 1

    matrix_Y = df["time_lived"].to_numpy()



    matrix_X = df[["un", "resistance", "vitesse", "vitesse2", "satiete", "vision"]].to_numpy()

    matric_X_transpose = matrix_X.transpose()

    matrix_X_produit_transpose = np.dot(matric_X_transpose, matrix_X)

    matrix_X_produit_transpose_invert = np.linalg.inv(matrix_X_produit_transpose)

    matrix_X__before_final = np.dot(matrix_X_produit_transpose_invert, matric_X_transpose)

    print("calcul des coefficients...")
    coef_beta = np.dot(matrix_X__before_final, matrix_Y) #coef_beta est notre modèle de ML, il faut maintenant vérifier qu'il est bon
    print("calcul de l'estimateur...")
    y_chapeau = np.dot(matrix_X, coef_beta)

    print("calcul des résidus...")
    residus = y_chapeau - matrix_Y

    print("calcul de l'estimateur de variabilité résiduelle...")
    estimateur_variabilite_residuelle = np.mean((matrix_Y - y_chapeau)**2) #Erreur total du modèle

    print("calcul de l'estimateur de variabilité naturel...")
    estimateur_variabilite_naturel = np.mean((matrix_Y - np.mean(matrix_Y))**2)

    print("calcul R²...")
    coefficient_determination = 1 - estimateur_variabilite_residuelle/estimateur_variabilite_naturel # R², Ce résultat explique a combien de pourcent les gènes expliquent la survie

    print("calcul de la variance de l'erreur...")
    variance_erreur = np.sum((matrix_Y - y_chapeau)**2)/(len(matrix_Y) - 6) #volume de hasard. Plus il est grand, plus c'est imprévisible

    print("calcul matrice variance covariance...")
    matrice_variance_covariance = matrix_X_produit_transpose_invert * variance_erreur #indique si les Beta risquent de changer si je relance une simulation

    print("calcul ecart type gènes...")
    ecart_type_gene = np.sqrt(np.diag(matrice_variance_covariance)) #Marge d'erreur pour chaque gène. Plus il est gros pour chaque gène, moins il est solide

    print("calcul |T|...")
    t_stat =  coef_beta/ecart_type_gene


    print("--------Résultats----------")
    print(f"R² : {coefficient_determination}")
    print(f"Dans la simulation, la génétique explique {(coefficient_determination*100):.3f}% de la survie d'un Minos, les {(1-coefficient_determination)*100:.3f} sont dues aux aléas de l'environnement. ")
    print(f"|T| : {t_stat}")
    print(f"temps de vie de base {coef_beta[0]:.3f} ({t_stat[0]:.3f} de fiabilité)")

    if (np.abs(t_stat[1])>2):
        impact = "positif" if coef_beta[1]>0 else "negatif"
        print(f"La résistance a un impact {impact} de {coef_beta[1]:.3f}")
    else:
        print("la résistance n'a pas de réel impact")

    if (np.abs(t_stat[2])>2):
        impact = "positif" if coef_beta[2]>0 else "negatif"
        print(f"La vitesse a un impact {impact} de {coef_beta[2]:.3f}")
    else:
        print("la vitesse n'a pas de réel impact")

    if (np.abs(t_stat[4])>2):
        impact = "positif" if coef_beta[4]>0 else "negatif"
        print(f"La satiété a un impact {impact} de {coef_beta[4]:.3f}")
    else:
        print("la satiété n'a pas de réel impact")

    if (np.abs(t_stat[5])>2):
        impact = "positif" if coef_beta[5]>0 else "negatif"
        print(f"La vision a un impact {impact} de {coef_beta[5]:.3f}")
    else:
        print("la vision n'a pas de réel impact")

