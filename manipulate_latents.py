import numpy as np
import joblib

def load_latents(path):
    return np.load(path)

def normalize_direction(direction):
    return direction / np.linalg.norm(direction)

def manipulate(latents, direction, intensity=1.0):
    direction = normalize_direction(direction)
    return latents + intensity * direction
