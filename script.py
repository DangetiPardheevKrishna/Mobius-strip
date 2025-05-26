import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import simpson
from scipy.spatial.distance import euclidean

class MobiusStrip:
    def __init__(self, R, w, n):
        self.R = R
        self.w = w
        self.n = n
        self.u = np.linspace(0, 2 * np.pi, n)
        self.v = np.linspace(-w/2, w/2, n)
        self.U, self.V = np.meshgrid(self.u, self.v)
        self.x, self.y, self.z = self.generate_mesh()

    def generate_mesh(self):
        U = self.U
        V = self.V
        R = self.R

        X = (R + V * np.cos(U / 2)) * np.cos(U)
        Y = (R + V * np.cos(U / 2)) * np.sin(U)
        Z = V * np.sin(U / 2)
        return X, Y, Z

    def compute_surface_area(self):
        # Compute partial derivatives
        Xu = np.gradient(self.x, axis=1)
        Xv = np.gradient(self.x, axis=0)
        Yu = np.gradient(self.y, axis=1)
        Yv = np.gradient(self.y, axis=0)
        Zu = np.gradient(self.z, axis=1)
        Zv = np.gradient(self.z, axis=0)

        # Cross product of partial derivatives
        cross_prod = np.sqrt(
            (Yu * Zv - Zu * Yv)**2 +
            (Zu * Xv - Xu * Zv)**2 +
            (Xu * Yv - Yu * Xv)**2
        )

        # Numerical double integration using Simpson's rule
        area = simpson([simpson(row, self.u) for row in cross_prod], self.v)
        return area

    def compute_edge_length(self):
        # Trace one edge of the strip (v = w/2)
        edge_x = (self.R + (self.w/2) * np.cos(self.u / 2)) * np.cos(self.u)
        edge_y = (self.R + (self.w/2) * np.cos(self.u / 2)) * np.sin(self.u)
        edge_z = (self.w/2) * np.sin(self.u / 2)

        edge = np.stack((edge_x, edge_y, edge_z), axis=1)
        length = sum(euclidean(edge[i], edge[i+1]) for i in range(len(edge)-1))
        return length

    def plot(self):
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.x, self.y, self.z, cmap='viridis', edgecolor='k', linewidth=0.1)
        ax.set_title("Mobius Strip")
        plt.savefig("mobius_strip_plot.png")  # Save the plot image
        plt.show()

# Accept user input
if __name__ == "__main__":
    try:
        R = float(input("Enter radius (R): "))
        w = float(input("Enter width (w): "))
        n = int(input("Enter resolution (n): "))

        mobius = MobiusStrip(R, w, n)
        mobius.plot()
        print(f"Surface Area: {mobius.compute_surface_area():.4f}")
        print(f"Edge Length: {mobius.compute_edge_length():.4f}")

    except Exception as e:
        print("Error:", e)
