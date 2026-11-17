import matplotlib.pyplot as plt
import numpy as np

from phased.models import Antenna, AntennaArray, Receiver, Environment

frequency = 3e8
spacing = 0.5  # meters
num_antennas = 8

antennas = AntennaArray()
for i in range(num_antennas):
    antennas.add(Antenna(x=i * spacing, y=0.0, frequency=frequency))


receiver = Receiver(6.0, 8.0)
antennas.focus_at(receiver.position)

environment = Environment(x=(-10, 10), y=(-2, 12))
x_matrix, y_matrix = environment.create_grid()
total_wave = antennas.electric_field_grid(x_matrix, y_matrix)


# PLOTTING
fig, ax = plt.subplots(figsize=(7, 6))

img = ax.imshow(
    total_wave,
    extent=(*environment.x_bounds, *environment.y_bounds),
    origin="lower",
    cmap="RdBu_r",
    vmin=-max(num_antennas, 1),
    vmax=max(num_antennas, 1),
)

ax.scatter(
    [float(a.position.x) for a in antennas],
    [float(a.position.y) for a in antennas],
    color="black",
    s=80,
    label="Antennas",
)
ax.scatter(
    receiver.position.x,
    receiver.position.y,
    color="green",
    marker="^",
    s=150,
    label="Receiver",
    zorder=5,
)

fig.colorbar(img, ax=ax, label="Combined Wave Amplitude")

ax.set_title(
    f"{num_antennas}-Antenna Beamforming Focused on Receiver at "
    f"({float(receiver.position.x):g}, {float(receiver.position.y):g})"
)
ax.set_xlabel("X Position (meters)")
ax.set_ylabel("Y Position (meters)")
ax.legend()

plt.show()
