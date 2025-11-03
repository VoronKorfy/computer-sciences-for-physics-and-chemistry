import re
import csv

def parse_formula(formula):
    atom_pattern = r'([A-Z][a-z]?)(\d*)'  # [A-Z] big letter, [a-z]? 0 or 1 repetition of small letter, ([0-9]*) 0 or more repetitions of numbers for subscript
    atoms = re.findall(atom_pattern, formula)
    atom_dict = {}
    for element, subscript in atoms:
        if subscript != '':
            subscript = int(subscript)
        else:
            subscript = 1
        atom_dict[element] = atom_dict.get(element, 0) + subscript
    return atom_dict

def parse_side(side_list):
    parsed = []
    for molecule in side_list:
        match = re.match(r'(\d*)([A-Za-z0-9]+)', molecule) # ([0-9]*) multiple numbers for coef, everything else is formula (at least 1 letter)
        # group(1) = ([0-9]*) = coefs
        if match.group(1) != '':
            coef = int(match.group(1))
        else:
            coef = 1
        # group(2) = ([A-Za-z0-9]+) = chem formula
        formula = match.group(2)
        parsed.append((coef, formula))
    return parsed

def parse_equation(equation):
    left, right = equation.split('->')
    reactants = left.split('+')
    products = right.split('+')
    return parse_side(reactants), parse_side(products)

def count_atoms(parsed_side):
    counts = {}
    for coef, formula in parsed_side:
        atoms = parse_formula(formula)
        for element, subscript in atoms.items():
            if element in counts:
                counts[element] += coef * subscript
            else:
                counts[element] = coef * subscript
    return counts

with open('formula.csv', newline='') as equation_csv:
    reader = csv.reader(equation_csv)
    for row in reader:
        formula = row[0]
        counts = parse_formula(formula)
        if counts.get('H') == 5 and counts.get('C') == 2:
            print("Molecule with 5H and 2C:", formula)

with open('balanceequation1.csv', newline='') as equation_csv:
    reader = csv.reader(equation_csv)
    number_of_balanced = 0
    for row in reader:
        equation = row[0]
        reactant, product = parse_equation(equation)
        if count_atoms(reactant) == count_atoms(product):
            number_of_balanced += 1
    print("Number of balanced equations in the first table:", number_of_balanced)


with open('balanceequation2.csv', newline='') as equation_csv:
    reader = csv.reader(equation_csv)
    number_of_balanced = 0
    for row in reader:
        equation = row[0]
        reactant, product = parse_equation(equation)
        if count_atoms(reactant) == count_atoms(product):
            number_of_balanced += 1
    print("Number of balanced equations in the second table:", number_of_balanced)
