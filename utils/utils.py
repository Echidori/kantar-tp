import numpy as np
from scipy.spatial.distance import euclidean
from tqdm import tqdm


# Fonction pour calculer une matrice de distance Euclidienne pondérée
def weighted_distance_matrix(X, weights):
    """
    Calcule une matrice de distance Euclidienne pondérée.
    Chaque élément représente la distance Euclidienne pondérée
    entre deux points dans X, selon les poids donnés.
    """
    n_samples = X.shape[0]
    distance_matrix = np.zeros((n_samples, n_samples))

    for i in tqdm(range(n_samples)):
        for j in range(i + 1, n_samples):
            # Calcul de la distance Euclidienne pondérée entre les points i et j
            dist = euclidean(X[i] * weights[i], X[j] * weights[j])
            distance_matrix[i, j] = dist
            distance_matrix[j, i] = dist  # Matrice symétrique
    return distance_matrix

def select_features(df, features):
    cols = []
    for feature in features:
        cols.append([col for col in df.columns if col == feature])

    sel = [item for sublist in cols for item in sublist]
    return df[sel]