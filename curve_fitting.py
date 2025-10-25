import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import struct

TAUS = np.array([200.9, 5.8, 38.6, 516.2, 57.8, 8.9])
FILES = ["Data1.txt", "Data2.txt", "Data3.txt", "Data4.dat", "Data5.txt", "Data6.txt"]


def fluorescence_model(t, A1, A2, A3, A4, A5, A6):
    return (A1 * np.exp(-t / TAUS[0]) +
            A2 * np.exp(-t / TAUS[1]) +
            A3 * np.exp(-t / TAUS[2]) +
            A4 * np.exp(-t / TAUS[3]) +
            A5 * np.exp(-t / TAUS[4]) +
            A6 * np.exp(-t / TAUS[5]))

#read the files
for filename in FILES:
    if filename.endswith(".txt"):
        data = np.loadtxt(filename)
    elif filename.endswith(".dat"):
        with open(filename, "rb") as f:
            binary_file = f.read()
        values = struct.unpack(f"{len(binary_file)//2}H", binary_file)

    #time axis from 0 to (N-1)*0.2 ns
    # t = np.arange(0, len(data) * 0.2, 0.2)
    t = np.linspace(0, 1000, len(data))
    # t = np.linspace(0, (len(data)-1)*0.05, len(data))

    par_initial = np.ones(6) # array filled with 1s
    par_optimal, par_covariance = curve_fit(fluorescence_model, t, data, par_initial, bounds=(0, np.inf))

    fitted = fluorescence_model(t, *par_optimal)

    for i in range(6):
        print(f"A{i + 1} (tau={TAUS[i]}): {par_optimal[i]:f}")

    plt.plot(t, data, label="Measured")
    plt.plot(t, fitted, label="Fitted")
    plt.legend()
    plt.show()
