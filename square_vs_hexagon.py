import numpy as np
import matplotlib.pyplot as plt


R = 36  # radius from axle to square corner (cm)

# the side length
s = R * np.sqrt(2)

# the radius from axle to mid-side
r = s / 2

# Build one inverted catenary arch
x_single = np.linspace(-s/2, s/2, 400)

# Standard catenary
y_catenary = r * np.cosh(x_single / r)

# Height at endpoints
y_end = r * np.cosh((s/2) / r)

# Inverted arch so endpoints touch y=0
y_inverted = y_end - y_catenary

# Repeat arches periodically
num_periods = 4
x_full = []
y_full = []

for k in range(0, num_periods + 1):
    x_shifted = x_single + k * s
    x_full.append(x_shifted)
    y_full.append(y_inverted)

x_full = np.concatenate(x_full)
y_full = np.concatenate(y_full)

R = 36  # radius from axle to vertex (cm)
n = 6   # hexagon

# Side length of regular hexagon
s = 2 * R * np.sin(np.pi / n)

# Catenary parameter
a = s / 2

# Build one inverted catenary arch
x_single = np.linspace(-s/2, s/2, 400)

# Standard catenary
y_catenary = a * np.cosh(x_single / a)

# Height at endpoints
y_end = a * np.cosh((s/2) / a)

# Inverted arch so endpoints touch y=0
y_inverted = y_end - y_catenary

# Repeat arches periodically
num_periods = 4
x_full_hex = []
y_full_hex = []

for k in range(0, num_periods + 1):
    x_shifted = x_single + k * s
    x_full_hex.append(x_shifted)
    y_full_hex.append(y_inverted)

x_full_hex = np.concatenate(x_full_hex)
y_full_hex = np.concatenate(y_full_hex)

plt.figure(figsize=(10, 4))
plt.plot(x_full, y_full, label='Square')
plt.plot(x_full_hex, y_full_hex, label='Hexagon')
plt.xlabel("Horizontal distance (cm)", fontsize=14)
plt.ylabel("Height (cm)", fontsize=14)
plt.gca().set_aspect('equal', adjustable='box')
plt.margins(y=0.4)
plt.grid(True)
plt.legend(fontsize=12)
plt.savefig('square_vs_hexagon.pdf')
plt.show()
