import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pip
from sklearn.decomposition import PCA
# matplotlib inline
import pandas as pd

X = np.array([[5, 8, 7, 33, 13, 38, 12, 6, 2], [5, 7, 9, 41, 39, 59, 26, 9, 2], [9, 8, 13, 16, 21, 25, 22, 12, 4],
              [18, 10, 11, 12, 15, 15, 21, 10, 3], [14, 11, 14, 10, 14, 18, 11, 14, 6],
              [24, 13, 15, 6, 13, 12, 25, 13, 3], [20, 5, 8, 16, 15, 14, 14, 8, 4], [6, 1, 5, 21, 12, 37, 13, 2, 3],
              [6, 5, 11, 16, 12, 16, 8, 11, 5], [11, 12, 13, 13, 17, 20, 16, 18, 5]])
u, s, vh = np.linalg.svd(X, full_matrices=True)
print(X)
print("//")
print(u)
print("//")
print(s)
print("//")
print(vh)
print("//")
PC1 = []
PC2 = []
PC3 = []
for i in range(10):
    x = np.transpose(vh[:, 1]) * np.transpose(X[i, :])
    y = np.transpose(vh[:, 2]) * np.transpose(X[i, :])
    z = np.transpose(vh[:, 3]) * np.transpose(X[i, :])
    PC1.insert(i, x)
    PC2.insert(i, y)
    PC3.insert(i, z)
    fig = plt.figure(figsize=(16, 9))
    ax = plt.axes(projection="3d")

# Add x, y gridlines
ax.grid(b=True, color='grey', linestyle='-.', linewidth=0.3, alpha=0.2)
# Creating color map
my_cmap = plt.get_cmap('hsv')
# Creating plot
sctt = ax.scatter3D(x, y, z, alpha=0.8, c=(x + y + z), cmap=my_cmap, marker='o')
plt.title("Detecting Human Genome")
ax.set_xlabel('PC1', fontweight='bold')
ax.set_ylabel('PC2', fontweight='bold')
ax.set_zlabel('PC3', fontweight='bold')
fig.colorbar(sctt, ax=ax, shrink=0.5, aspect=5)
plt.show()

ax.scatter3D(PC1, PC2, PC3)

plt.show()
