import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

resistance = 1000
capacitor = 10**(-9)
voltage_in = 5
time = (0, 10**(-5))
time_array = np.linspace(time[0], time[1], 1000)

def derivative_function(t, capacitor_voltage):
    return 1/(capacitor*resistance)*(voltage_in-capacitor_voltage)

capacitor_voltage_integrated = solve_ivp(
    derivative_function,
    time,
    [0],
    t_eval=np.linspace(0, 10**(-5), 1000)
)

capacitor_voltage_analytical = voltage_in * (1 - np.exp(-time_array / (resistance * capacitor)))

plt.plot(time_array, capacitor_voltage_integrated.y[0], label='capacitor voltage')
plt.show()
plt.plot(capacitor_voltage_analytical, capacitor_voltage_integrated.y[0]-capacitor_voltage_analytical, label='relative difference')
plt.legend()
plt.show()

