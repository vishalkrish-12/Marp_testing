# Marimo Notebook: Interactive Data Analysis

Below is the content of `analysis.py` (a Marimo notebook) hosted on GitHub. It begins with your email, stitches together at least two cells with variable dependencies, provides an interactive slider widget, and renders dynamic markdown based on the widget’s state. Comments document the data flow between cells.

```python
# 23ds2000044@ds.study.iitm.ac.in

# %% [markdown]
"""
# Exploring Variable Relationships with a Slider

This Marimo notebook demonstrates how changing one variable impacts another via an interactive slider.
"""

# %% cell1
import numpy as np
import matplotlib.pyplot as plt

# Generate base data in cell1
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)        # y depends on x
# End of cell1

# %% cell2
from ipywidgets import IntSlider, interact
from IPython.display import Markdown, display

# cell2 depends on x and y defined in cell1
def plot_sine(frequency, amplitude):
    """
    Plot a sine wave with user-controlled frequency and amplitude.
    """
    y2 = amplitude * np.sin(frequency * x)   # y2 depends on x, frequency, amplitude
    plt.figure(figsize=(6, 3))
    plt.plot(x, y2, label=f"{amplitude}·sin({frequency}x)")
    plt.legend()
    plt.title("Interactive Sine Wave")
    plt.tight_layout()
    plt.show()

    # Dynamic markdown output based on current slider state
    display(Markdown(
        f"**Current settings:** Frequency = {frequency}, Amplitude = {amplitude}  \n"
        f"As frequency increases, the wave compresses horizontally.  \n"
        f"As amplitude increases, the wave stretches vertically."
    ))

# %% cell3
# cell3 wires up the interactive sliders to the plot function
freq_slider = IntSlider(min=1, max=10, step=1, value=3, description="Frequency")
amp_slider  = IntSlider(min=1, max=5,  step=1, value=1, description="Amplitude")

# Display the interactive controls and link them to plot_sine
display(Markdown("## Adjust the Sliders Below"))
interact(plot_sine, frequency=freq_slider, amplitude=amp_slider)

# %% cell4
import numpy as np
import matplotlib.pyplot as plt

# Generate base data
x = np.linspace(0, 2 * np.pi, 200)   # x is independent variable
y = np.sin(x)                        # y depends on x

# %% cell5
from ipywidgets import FloatSlider, interact
from IPython.display import Markdown, display

def plot_sine(frequency, amplitude):
    """
    Plots a sine curve based on the slider inputs.
    y2 depends on x, frequency, and amplitude.
    """
    y2 = amplitude * np.sin(frequency * x)   # new data depends on slider values
    plt.figure(figsize=(6,3))
    plt.plot(x, y2, color='teal')
    plt.title(f"Sine Wave — freq: {frequency}, amp: {amplitude}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.tight_layout()
    plt.show()

    # Dynamic markdown feedback
    display(Markdown(
        f"**Current settings:**  \n"
        f"- Frequency = {frequency}  \n"
        f"- Amplitude = {amplitude}  \n\n"
        "↑ Drag the sliders to update the plot and see how the wave changes."
    ))

# %% cell6
# Instantiate interactive sliders
freq_slider = FloatSlider(
    value=1.0,
    min=0.5,
    max=5.0,
    step=0.1,
    description='Frequency'
)

amp_slider = FloatSlider(
    value=1.0,
    min=0.5,
    max=2.0,
    step=0.1,
    description='Amplitude'
)

# Wire widgets to the plotting function
interact(plot_sine, frequency=freq_slider, amplitude=amp_slider)

