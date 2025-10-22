import numpy as np
from scipy.optimize import minimize

VCC, R1, R2, R3, R4 = 15, 1000, 2000, 10000, 500

def cost(arr):
    VA, VB, VC, VD = arr[0], arr[1], arr[2], arr[3]

    error1 = VA - (VCC/R1 + VC/R3 + VB/R3 + VD/R4) / (1/R1 + 2/R3 + 1/R4)
    error2 = VB - (VCC/R2 + VD/R3 + VA/R3) / (1/R2 + 2/R3)
    error3 = VC - (VA/R3 + VD/R3) / (1/R2 + 2/R3)
    error4 = VD - (VB/R3 + VC/R3 + VA/R4) / (1/R1 + 2/R3 + 1/R4)

    return error1**2 + error2**2 + error3**2 + error4**2

arr = [1, 1, 1, 1]

result = minimize(cost, arr)

VA, VB, VC, VD = result.arr

print("VA =", VA)
print("VB =", VB)
print("VC =", VC)
print("VD =", VD)
