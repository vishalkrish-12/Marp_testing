# 23ds2000044@ds.study.iitm.ac.in
import marimo as mo
import pandas as pd
import plotly.express as px
from sklearn.datasets import load_iris

# Initialize the Marimo app
app = mo.App()


@app.cell
def load_data(mo):
    """
    Cell 1: Load and prepare the dataset.
    This cell has no dependencies and provides the initial DataFrame `iris_df`.
    Other cells will depend on `iris_df`.
    """
    mo.md(
        """
        # Interactive Analysis of the Iris Dataset

        This notebook demonstrates the relationship between sepal and petal
        measurements in the Iris dataset. We will use interactive widgets to
        filter and explore the data dynamically.
        """
    )
    # Load the classic Iris dataset
    iris = load_iris(as_frame=True)
    iris_df = iris.frame
    # The target column is numeric, so we map it to species names
    iris_df['species'] = iris_df['target'].map(
        {i: name for i, name in enumerate(iris.target_names)}
    )
    # Rename columns for clarity (remove ' (cm)')
    iris_df.columns = [
        'sepal_length', 'sepal_width', 'petal_length', 'petal_width',
        'target', 'species'
    ]
    return iris, iris_df, mo


@app.cell
def create_slider(iris_df, mo):
    """
    Cell 2: Create an interactive slider widget.
    This cell depends on `iris_df` from Cell 1 to determine the slider's range.
    The slider's state will be used by other cells.
    """
    mo.md(
        """
        ### Filter by Petal Length

        Use the slider below to set a minimum petal length. The plot and the
        summary statistics will update automatically.
        """
    )
    # Create a slider for filtering by petal length.
    # The min and max values are derived from the loaded data.
    petal_length_slider = mo.ui.slider(
        start=iris_df['petal_length'].min(),
        stop=iris_df['petal_length'].max(),
        step=0.1,
        value=iris_df['petal_length'].min(),
        label="Minimum Petal Length ($cm$):"
    )
    return petal_length_slider,


@app.cell
def dynamic_markdown(petal_length_slider, mo):
    """
    Cell 3: Display dynamic markdown output.
    This cell depends on `petal_length_slider` from Cell 2.
    Its output changes whenever the slider's value changes.
    """
    # Get the current value from the slider widget
    min_length = petal_length_slider.value

    # Display a markdown cell that updates dynamically
    dynamic_output = mo.md(
        f"""
        The analysis is currently filtered for flowers with a petal length of
        **{min_length:.1f} cm** or greater.
        """
    )
    return dynamic_output, min_length


@app.cell
def filter_data(iris_df, min_length):
    """
    Cell 4: Filter the data based on the slider.
    This cell has two dependencies:
    1. `iris_df` from Cell 1
    2. `min_length` from Cell 3 (which itself depends on the slider in Cell 2)
    It provides the `filtered_df` to the plotting cell.
    """
    # Filter the DataFrame based on the value from the dynamic markdown cell
    filtered_df = iris_df[iris_df['petal_length'] >= min_length]
    return filtered_df,


@app.cell
def plot_data(filtered_df, px):
    """
    Cell 5: Generate the plot.
    This cell depends on `filtered_df` from Cell 4.
    When `filtered_df` is updated, this cell re-runs to redraw the plot.
    """
    # Create an interactive scatter plot with Plotly Express
    fig = px.scatter(
        filtered_df,
        x="sepal_length",
        y="sepal_width",
        color="species",
        size='petal_length',
        hover_data=['petal_width'],
        title="Sepal Width vs. Sepal Length (Filtered)",
        labels={
            "sepal_length": "Sepal Length ($cm$)",
            "sepal_width": "Sepal Width ($cm$)"
        }
    )
    return fig,


if __name__ == "__main__":
    app.run()
