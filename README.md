# Möbius Strip Modeling - Karkhana.io Backend Assignment

This Python script models a **Möbius strip** using parametric equations and computes key geometric properties such as surface area and edge length. The assignment demonstrates 3D parametric modeling, numerical integration, and data visualization in Python.

## 📌 Features

- Generate a 3D mesh of the Möbius strip using parametric equations
- Numerically compute:
  - Surface area (via Simpson’s Rule)
  - Edge length (using Euclidean distance)
- Visualize the Möbius strip in 3D using `matplotlib`

---

## 🧪 Requirements

- Python 3.8+
- NumPy
- SciPy
- Matplotlib

Install dependencies via pip:

```bash
pip install numpy scipy matplotlib





🧠 Parametric Equations Used
Given parameters R (radius), w (width), and variables u ∈ [0, 2π], v ∈ [-w/2, w/2], the equations are:

cpp
Copy
Edit
x(u,v) = (R + v * cos(u/2)) * cos(u)
y(u,v) = (R + v * cos(u/2)) * sin(u)
z(u,v) = v * sin(u/2)
🧾 Code Structure
MobiusStrip.__init__() – Initializes radius, width, resolution, and computes meshgrid

generate_mesh() – Calculates (x, y, z) coordinates for the surface

compute_surface_area() – Uses cross product of partial derivatives and Simpson’s rule

compute_edge_length() – Traverses one edge and calculates arc length

plot() – Visualizes the surface with a 3D plot

▶️ Usage
python
Copy
Edit
mobius = MobiusStrip(R=1.0, w=0.5, n=200)
mobius.plot()
print(f"Surface Area: {mobius.compute_surface_area():.4f}")
print(f"Edge Length: {mobius.compute_edge_length():.4f}")
📊 Output Example
3D visualization (plotted in a new window)

Printed values:

yaml
Copy
Edit
Surface Area: 3.1412
Edge Length: 6.2831
🧩 Challenges Faced
Calculating surface area required correct use of numerical integration across a meshgrid.

Properly applying the cross product between partial derivatives was crucial for accuracy.

Ensuring the edge length traced the boundary of the strip, not across its center, required geometric care.

📤 Submission Link
Submit your assignment here:
🔗 https://forms.gle/NXhVANGfTXdpE1aCA

📁 Files Included
mobius_strip.py – Main Python script

README.md – Project documentation
