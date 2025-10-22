import numpy as np

VCC = 15
R1, R2, R3, R4 = 1000, 2000, 10000, 500

A = np.array([
    [1/R1 + 2/R3 + 1/R4, -1/R3, -1/R3, -1/R4], # VA*A[0][0]−VB*A[0][1]−VC*A[0][1]−VD*A[0][1] = B[0]
    [-1/R3, 1/R2 + 2/R3, 0, -1/R3],
    [-1/R3, 0, 1/R2 + 2/R3, -1/R3],
    [-1/R4, -1/R3, -1/R3, 1/R1 + 2/R3 + 1/R4]
])

B = np.array([VCC/R1, VCC/R2, 0, 0]) # VCC/R1, etc

VA, VB, VC, VD = np.linalg.solve(A, B)

print("VA =", VA)
print("VB =", VB)
print("VC =", VC)
print("VD =", VD)
