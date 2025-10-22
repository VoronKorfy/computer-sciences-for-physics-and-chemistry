import numpy as np
import matplotlib.pyplot as plt

kf, kr = 0.05, 0.005
A, B, AB = 800, 400, 100
t_max = 1
t = 0

times = [0]
A_vals = [A]
B_vals = [B]
AB_vals = [AB]

while t < t_max:
    rate_forward = kf * A * B
    rate_reverse = kr * AB
    total_rate = rate_forward + rate_reverse
    if total_rate == 0:
        break

    t += np.random.exponential(1 / total_rate)
    if np.random.rand() < rate_forward / total_rate:
        A -= 1
        B -= 1
        AB += 1
    else:
        A += 1
        B += 1
        AB -= 1

    times.append(t)
    A_vals.append(A)
    B_vals.append(B)
    AB_vals.append(AB)

plt.plot(times, A_vals, label='A')
plt.plot(times, B_vals, label='B')
plt.plot(times, AB_vals, label='AB')
plt.legend()
plt.show()
