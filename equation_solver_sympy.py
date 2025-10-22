import sympy as sp

VA, VB, VC, VD, VCC, R1, R2, R3, R4 = sp.symbols('VA VB VC VD VCC R1 R2 R3 R4')

equation_1 = sp.Eq(VA, (VCC/R1 + VC/R3 + VB/R3 + VD/R4) / (1/R1 + 2/R3 + 1/R4))
equation_2 = sp.Eq(VB, (VCC/R2 + VD/R3 + VA/R3) / (1/R2 + 2/R3))
equation_3 = sp.Eq(VC, (VA/R3 + VD/R3) / (1/R2 + 2/R3))
equation_4 = sp.Eq(VD, (VB/R3 + VC/R3 + VA/R4) / (1/R1 + 2/R3 + 1/R4))

solutions = sp.solve((equation_1, equation_2, equation_3, equation_4), (VA, VB, VC, VD))

numerical_values = {
    VCC: 15,
    R1: 1000,
    R2: 2000,
    R3: 10000,
    R4: 500
}

VA = solutions[VA].subs(numerical_values).evalf()
VB = solutions[VB].subs(numerical_values).evalf()
VC = solutions[VC].subs(numerical_values).evalf()
VD = solutions[VD].subs(numerical_values).evalf()

print("VA =", VA)
print("VB =", VB)
print("VC =", VC)
print("VD =", VD)
