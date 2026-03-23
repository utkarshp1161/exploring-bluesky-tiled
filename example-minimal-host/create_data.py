import os
import h5py
import numpy as np

os.makedirs("data", exist_ok=True)

with h5py.File("data/scan_a.h5", "w") as f:
    f["image"] = np.random.rand(64, 64)
    f["spectrum"] = np.random.rand(100)

with h5py.File("data/scan_b.h5", "w") as f:
    g = f.create_group("measurement")
    g["x"] = np.linspace(0, 10, 50)
    g["y"] = np.sin(g["x"][:])