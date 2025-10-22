import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import  cumulative_trapezoid

t = np.linspace(0, 20, 1000)
x = 50 * np.sin(0.1 * np.pi * t)
y = 50 * np.sin(0.2 * np.pi * t)

x_noisy = x+np.random.normal(loc=5, scale=0.001, size=t.shape)
y_noisy = y+np.random.normal(loc=5, scale=0.001, size=t.shape)


ax =-0.5*np.pi**2*np.sin(0.1*np.pi*t)
ay =-2*np.pi**2*np.sin(0.2*np.pi*t)

ax_noisy = np.gradient(np.gradient(x_noisy, t), t)
ay_noisy = np.gradient(np.gradient(y_noisy, t), t)

ax_noisy_madeup = ax + np.random.normal(loc=0.1, scale=1.0, size=t.shape)
ay_noisy_madeup = ay + np.random.normal(loc=0.1, scale=1.0, size=t.shape)

x_noisy_integrated = cumulative_trapezoid(cumulative_trapezoid(ax_noisy_madeup, t, initial=0), t, initial=0)
y_noisy_integrated = cumulative_trapezoid(cumulative_trapezoid(ay_noisy_madeup, t, initial=0), t, initial=0)

plt.plot(x_noisy_integrated, y_noisy_integrated, label='Made up')
plt.plot(x_noisy, y_noisy, label='Noisy')

plt.legend()
plt.show()
