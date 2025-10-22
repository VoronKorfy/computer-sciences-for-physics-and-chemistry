import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

k1, k_minus1, k2 = 1, 0.01, 5
E, S, P, ES = 10, 200, 0, 0
t_max = 5
t = 0

times = [0]
E_vals = [E]
S_vals = [S]
P_vals = [P]
ES_vals = [ES]

while t < t_max:
    rate_bind = k1 * E * S
    rate_unbind = k_minus1 * ES
    rate_product = k2 * ES
    total_rate = rate_bind + rate_unbind + rate_product
    if total_rate == 0:
        break

    t += np.random.exponential(1 / total_rate)
    r = np.random.rand()
    if r < rate_bind / total_rate:
        E -= 1
        S -= 1
        ES += 1
    elif r < (rate_bind + rate_unbind) / total_rate:
        E += 1
        S += 1
        ES -= 1
    else:
        ES -= 1
        E += 1
        P += 1

    times.append(t)
    E_vals.append(E)
    S_vals.append(S)
    P_vals.append(P)
    ES_vals.append(ES)

def enzymatic_ode(y, t):
    E, S, P, ES = y
    dE = -k1*E*S + (k_minus1 + k2)*ES
    dS = -k1*E*S + k_minus1*ES
    dP = k2*ES
    dES = k1*E*S - (k_minus1 + k2)*ES
    return [dE, dS, dP, dES]

t_span = np.linspace(0, t_max, 200)
det_solution = odeint(enzymatic_ode, [10, 200, 0, 0], t_span)

plt.plot(times, P_vals, 'r.', alpha=0.4, label='Stochastic')
plt.plot(t_span, det_solution[:,2], 'k', label='Deterministic')
plt.legend()
plt.show()
