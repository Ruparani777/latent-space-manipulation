import numpy as np
from sklearn.decomposition import PCA

def get_direction(latents, labels):
    # Assume binary labels (e.g., smiling vs. not smiling)
    pca = PCA(n_components=1)
    return pca.fit(latents[labels == 1] - latents[labels == 0]).components_[0]

def interpolate(latent1, latent2, steps=5):
    return [(1 - alpha) * latent1 + alpha * latent2 for alpha in np.linspace(0, 1, steps)]
