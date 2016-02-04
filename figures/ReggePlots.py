import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.0001, 1, num=5000, endpoint=False)
a_0 = 0.5
a_1 = 0.5
a_2 = 0.5
z_A = 1
z_B = -1

def r0(x, a_0):
    return (-1.0 + (a_0) * (1.0 / np.sqrt(1.0 - (x ** 2))))

def r1(x, a_1, z_A, z_B):
    return (-1.0 - (z_A * z_B * a_1) * (x / np.sqrt(1.0 - (x ** 2))))

def r2(x, a_2):
    return (-1.0 + (a_2 / 2.0) * ((2.0 * (x ** 2) - 1.0) / np.sqrt(1 - (x ** 2))))

def r(x, a_0):
    return (-1.0 + (a_0) * np.arccos(-1 * x) / np.sqrt(1.0 - (x ** 2)))

R0 = r0(x, a_0)
R1 = r1(x, a_1, z_A, z_B)
R2 = r2(x, a_2)
R = r(x, a_0)

lw = 1.5 # line width

for k in range(4):
    plt.plot(x, np.array([float(k) for n in x]), 'k--')

# plt.plot(x, R0, '#FF7575', label=r'$N = 0$', linewidth=lw)
# plt.plot(x, R1, '#2F74D0', label=r'$N = 1$', linewidth=lw)
# plt.plot(x, R2, '#4AE371', label=r'$N = 2$', linewidth=lw)

plt.plot(x, R0, '#FF7575', label=r'$R_{0}$', linewidth=lw)
plt.plot(x, R, '#9669FE', label=r'$R$', linewidth=lw)

fs = 18 # font size

plt.xlabel(r'$\xi$', fontsize=fs)
plt.ylabel(r'$n$', fontsize=fs)
plt.xlim(-0.04, x.max() * 1.04)
# plt.ylim(-2, 4) # 012.pdf
plt.ylim(-2, 4) # R0R.pdf
plt.legend(loc='upper center', fontsize=fs)
plt.savefig('R0R.pdf')
# plt.savefig('012.pdf')