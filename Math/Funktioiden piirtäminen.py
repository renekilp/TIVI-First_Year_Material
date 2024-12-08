import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------

x = np.linspace(-5, 5, 100)
y = -1.5 * x ** 2 - 3 * x + 7
z = x ** 2 - 4 * x + 3

ax = plt.subplot()

ax.spines['vasen'].set_position(('data', 0))
ax.spines['ala'].set_position(('data', 0))
ax.spines['oikea'].set_color('none')
ax.spines['ylä'].set_color('none')

# mittasuhteet
ax.set_aspect('equal')

# x-akselin säätöä
ax.set_xticks(np.arange(-5, 5, 1))


# Y:lle rajat, että kuvaajat näkyvät fiksummin
plt.ylim([-10, 10])

# label tarvitsee tuon legend():n

# ----------------------------------------------------------

plt.plot(x, y, label=r"$y = -1 \ frac {1} {2} x^2 - 3x + 7$")
plt.plot(x, z, label=r"$y = x^2 - 4x + 3$")
plt.legend()
plt.show()

# ----------------------------------------------------------

plt.plot(x, y, label=r"$y = x^2$")
plt.plot(x, z, label=r"$y = 3x - 5$")
plt.legend()
plt.show()