import re
import csv

formula = "C0"
atom = r'([A-Z][a-z]?)(\d*)'
atoms = re.findall(atom, formula)
atom_dict = {}
for (element, subscript) in atoms:
    if subscript != '':
        subscript = int(subscript)
    else:
        subscript = 1
    atom_dict[element] = atom_dict.get(element, 0) + subscript
print(atom_dict)

equation = "2C2H6+7O2->4CO2+6H2O"
left, right = equation.split('->')
reactants = left.split('+')
products = right.split('+')

react_parsed = []
for molecule in reactants:
    match = re.match(r'(\d*)([A-Za-z0-9]+)', molecule)
    # group(1) = coefs
    if match.group(1) != '':
        coef = int(match.group(1))
    else:
        coef = 1
    # group(2) = chem formula
    formula = match.group(2)
    react_parsed.append((coef, formula))

prod_parsed = []
for molecule in products:
    match = re.match(r'(\d*)([A-Za-z0-9]+)', molecule)
    # group(1) = coefs
    if match.group(1) != '':
        coef = int(match.group(1))
    else:
        coef = 1
    # group(2) = chem formula
    formula = match.group(2)
    prod_parsed.append((coef, formula))

# check if balanced

number_of_left_atoms = {}
number_of_right_atoms = {}

for coef, formula in react_parsed:
    atoms = re.findall(atom, formula)
    for (element, subscript) in atoms:
        if subscript != '':
            subscript = int(subscript)
        else:
            subscript = 1
        number_of_left_atoms[element] = number_of_left_atoms.get(element, 0) + coef * subscript

for coef, formula in prod_parsed:
    atoms = re.findall(atom, formula)
    for (element, subscript) in atoms:
        if subscript != '':
            subscript = int(subscript)
        else:
            subscript = 1
        number_of_right_atoms[element] = number_of_right_atoms.get(element, 0) + coef * subscript

print(number_of_left_atoms)
print(number_of_right_atoms)
print(number_of_left_atoms == number_of_right_atoms)


