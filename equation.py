import re

def read_equation_from_file(filename):
    with open(filename, 'r') as file:
        equation = file.read().strip()
    return equation

def get_equation_coefficients(equation):
    # Initialiser les coefficients à zéro
    coeffs = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0}

    # Utiliser une expression régulière pour extraire les coefficients
    pattern = re.compile(r'([+-]?\d*\.?\d*/*\d*\.?\d*)(x\^2|y\^2|z\^2|xz|zx|xy|yx|zy|yz|x|y|z)?')
    matches = pattern.findall(equation.replace(" ", ""))
    
    constant_term = re.findall(r'([+-]?\d*\.?\d*/*\d*\.?\d*)$', equation.replace(" ", ""))

    for match in matches:
        coeff, term = match
        if coeff in ['', '+', '-']:
            coeff = coeff + '1' if coeff else '1'
        
        try:
            coeff = eval(coeff)
        except Exception as e:
            print(f"Erreur lors de l'évaluation du coefficient {coeff}: {e}")
            continue

        if term == 'x^2':
            coeffs['a'] += coeff
        elif term == 'y^2':
            coeffs['b'] += coeff
        elif term == 'z^2':
            coeffs['c'] += coeff
        elif term in ['xz', 'zx']:
            coeffs['d'] += coeff
        elif term in ['xy', 'yx']:
            coeffs['e'] += coeff
        elif term in ['zy', 'yz']:
            coeffs['f'] += coeff
        elif term == 'x':
            coeffs['g'] += coeff
        elif term == 'y':
            coeffs['h'] += coeff
        elif term == 'z':
            coeffs['i'] += coeff

    if constant_term:
        try:
            coeffs['j'] += eval(constant_term[0])
        except Exception as e:
            print(f"Erreur lors de l'évaluation du terme constant {constant_term[0]}: {e}")
    
    return coeffs

# Lire l'équation depuis le fichier data.txt et récupérer les coefficients
equation = read_equation_from_file('data.txt')
coefficients = get_equation_coefficients(equation)
print(coefficients)
