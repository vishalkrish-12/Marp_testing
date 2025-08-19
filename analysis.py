# Cell 1: Author and Imports
# Author: 23ds2000044@ds.study.iitm.ac.in
# This cell imports required libraries and sets up the dataset.
import numpy as np
import matplotlib.pyplot as plt
import marimo as mo

# Generate synthetic data
x = np.linspace(0, 10, 100)
y = 2 * x + np.random.normal(0, 2, size=100)

# Cell 2: Interactive Slider and Plot
# This cell creates a slider to adjust the slope and updates the plot accordingly.
slope = mo.ui.slider(label="Slope", min=0, max=5, step=0.1, value=2)

# Recalculate y based on slider
y_dynamic = slope.value * x + np.random.normal(0, 2, size=100)

fig, ax = plt.subplots()
ax.scatter(x, y_dynamic, alpha=0.6)
ax.plot(x, slope.value * x, color='red', label=f"Slope: {slope.value}")
ax.legend()
plt.close(fig)

mo.display(fig)

# Cell 3: Dynamic Markdown Output
# This cell displays dynamic markdown based on the slider's value.
mo.md(f"### Current slope value: **{slope.value}**\n\nThe plot above shows the relationship between x and y with the selected slope.")
