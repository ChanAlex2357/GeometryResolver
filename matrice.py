import numpy as np

def create_matrix_from_coefficients(coeffs):
    a, b, c, d, e, f = coeffs['a'], coeffs['b'], coeffs['c'], coeffs['d'], coeffs['e'], coeffs['f']
    
    # Vérifier si on doit créer une matrice R3
    if all(v != 0 for v in [a, b, c, d, e, f]):
        M = np.array([
            [a, e / 2, d / 2],
            [e / 2, b, f / 2],
            [d / 2, f / 2, c]
        ])
        return M
    
    # Vérifier si on doit créer une matrice R2
    elif all(v != 0 for v in [a, b, e]):
        M = np.array([
            [a, e / 2],
            [e / 2, b]
        ])
        return M
    
    # Si les conditions ne sont pas remplies, retourner None
    return None

def calculate_determinant(matrix):
    if matrix is not None:
        return np.linalg.det(matrix)
    else:
        return None