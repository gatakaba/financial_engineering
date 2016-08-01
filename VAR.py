# coding:utf-8
# calc Value and risk using brown motion

import numpy as np
import matplotlib.pyplot as plt

# set up params
N = 1000
dt = 0.01

mu = 0.1
sigma = 0.2
S0 = 1000
t = np.linspace(0, N * dt, N)

# calc using formula
E = np.exp(mu * t) * S0
V = np.exp(2 * mu * t) * S0 ** 2 * (np.exp(sigma ** 2 * t) - 1)

# simulate brown motion
for j in range(100):
    l = []
    S = S0
    for i in range(N):
        S += mu * S * dt + sigma * S * np.random.normal(0, sigma ** 0.5) * dt ** 0.5
        l.append(S)
    plt.plot(t, l)

# plot
plt.plot(t, E)
plt.plot(t, E + V ** 0.5)
plt.plot(t, E - V ** 0.5)
plt.show()
