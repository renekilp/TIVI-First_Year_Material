import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 100)
y = x**2
z = 2*x-4

ax=plt.subplot()

ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# samat mittasuhteet
ax.set_aspect('equal')

# x-akselin säätöä
ax.set_xticks(np.arange(-5, 5, 1))


# Y:lle rajat, että kuvaajat näkyvät fiksummin
plt.ylim([-7, 7])

# label tarvitsee tuon legend():n
plt.plot(x, y, label="$y = x^2$")
plt.plot(x, z, label="$y = 3x - 5$")
plt.legend()

plt.show()




