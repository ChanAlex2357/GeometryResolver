import equation as eq
import matrisation as mtr

def main():
    # Recuperation des coefficients
    coefficients = eq.get_equation_coefficients_from_file('r3data.txt')
    # Affichage des coefficients
    # print (coefficients)
    # Créer la matrice à partir des coefficients
    
    matrix = mtr.create_matrix_from_coefficients(coefficients)
    # if matrix is not None:
    #     print("Matrice:\n", matrix)
    # else:
    #     print("Les coefficients ne permettent pas de créer une matrice R2 ou R3")

# Maii call
main()