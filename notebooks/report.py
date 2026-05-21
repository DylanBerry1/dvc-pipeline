import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    import pandas as pd
    from matplotlib import pyplot as plt

    df = pd.read_csv('data/features/events.csv')

    df['duration_minutes'].plot(kind='hist')
    return


if __name__ == "__main__":
    app.run()
