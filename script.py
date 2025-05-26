import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import simpson

class MobiusStrip:
    """
    A class to model and analyze a Mobius strip.
    
    Parameters:
        R (float): Radius from center to the strip (default: 1)
        w (float): Width of the strip (default: 0.5)
        n (int): Number of points in the mesh (default: 100)
    """
    
    def __init__(self, R=1, w=0.5, n=100):
        self.R = R
        self.w = w
        self.n = n
        
        # Generate parameter space
        self.u = np.linspace(0, 2*np.pi, n)  # Angle around the strip
        self.v = np.linspace(-w/2, w/2, n)   # Width parameter
        
        # Create mesh grid
        self.U, self.V = np.meshgrid(self.u, self.v)
        
        # Compute 3D coordinates
        self.x, self.y, self.z = self._parametric_equations(self.U, self.V)
        
    def _parametric_equations(self, u, v):
        """Compute the parametric equations for the Mobius strip."""
        x = (self.R + v * np.cos(u/2)) * np.cos(u)
        y = (self.R + v * np.cos(u/2)) * np.sin(u)
        z = v * np.sin(u/2)
        return x, y, z
    
    def compute_surface_area(self):
        """Numerically compute the surface area of the Mobius strip."""
        # Compute partial derivatives for surface area calculation
        du = 2*np.pi / self.n
        dv = self.w / self.n
        
        # For surface area, we need to compute the magnitude of the cross product
        # of the partial derivatives (∂x/∂u × ∂x/∂v)
        
        # Compute numerical derivatives
        dx_du = np.gradient(self.x, du, axis=1)
        dy_du = np.gradient(self.y, du, axis=1)
        dz_du = np.gradient(self.z, du, axis=1)
        
        dx_dv = np.gradient(self.x, dv, axis=0)
        dy_dv = np.gradient(self.y, dv, axis=0)
        dz_dv = np.gradient(self.z, dv, axis=0)
        
        # Compute cross product components
        cross_x = dy_du * dz_dv - dz_du * dy_dv
        cross_y = dz_du * dx_dv - dx_du * dz_dv
        cross_z = dx_du * dy_dv - dy_du * dx_dv
        
        # Magnitude of the cross product
        cross_mag = np.sqrt(cross_x**2 + cross_y**2 + cross_z**2)
        
        # Integrate over the surface
        area = simpson(simpson(cross_mag, dx=du, axis=1), dx=dv, axis=0)
        
        return area
    
    def compute_edge_length(self):
        """Numerically compute the length of the edge of the Mobius strip."""
        # The edge is when v = ±w/2
        u_edge = np.linspace(0, 2*np.pi, self.n)
        v_edge = self.w/2  # Using one edge (both edges have same length)
        
        # Compute edge coordinates
        x, y, z = self._parametric_equations(u_edge, v_edge)
        
        # Compute derivatives along the edge
        dx = np.gradient(x, u_edge)
        dy = np.gradient(y, u_edge)
        dz = np.gradient(z, u_edge)
        
        # Compute differential length
        dl = np.sqrt(dx**2 + dy**2 + dz**2)
        
        # Integrate to get total length
        length = simpson(dl, u_edge)
        
        return length * 2  # Both edges have the same length
    
    def plot(self):
        """Create a 3D plot of the Mobius strip."""
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Plot the surface
        ax.plot_surface(self.x, self.y, self.z, color='b', alpha=0.7)
        
        # Plot the edges
        v_edge = self.w/2
        x_edge, y_edge, z_edge = self._parametric_equations(self.u, v_edge)
        ax.plot(x_edge, y_edge, z_edge, color='r', linewidth=2)
        x_edge, y_edge, z_edge = self._parametric_equations(self.u, -v_edge)
        ax.plot(x_edge, y_edge, z_edge, color='r', linewidth=2)
        
        # Set labels and title
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'Mobius Strip (R={self.R}, w={self.w})')
        
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Create a Mobius strip with default parameters
    mobius = MobiusStrip(R=2, w=0.8, n=200)
    
    # Compute properties
    area = mobius.compute_surface_area()
    edge_length = mobius.compute_edge_length()
    
    print(f"Surface Area: {area:.4f}")
    print(f"Edge Length: {edge_length:.4f}")
    
    # Visualize
    mobius.plot()
