import numpy as np
import matplotlib.pyplot as plt

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int(xmax - xmin) * pixel_density)
    im = np.linspace(ymin, ymax, int(ymax - ymin) * pixel_density)
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

def is_stable(c, num_iterations):
    z = np.zeros_like(c)
    mask = np.full(c.shape, True, dtype= bool)

    for n in range(num_iterations):
        z[mask] = z[mask] **2 + c[mask]
        mask[np.abs(z) > 2] = False

    return mask

def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]

c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density= 100 )
members = get_members(c, num_iterations= 50)

plt.scatter(members.real, members.imag, color = 'black', marker= ',', s = 1)
plt.gca().set_aspect('equal')
plt.axis('off')
plt.tight_layout()
plt.show()