import plotly.graph_objs as go
import numpy as np


def plot_histogram(values, title=None, xaxis_title=None):
    """
    Plots histogram of values putting the probability density on the y axis.
    """
    trace = go.Histogram(
        x=values,
        histnorm="probability density"
    )

    layout = go.Layout(
        title=go.layout.Title(
            text=title,
            x=0.5
        ),
        xaxis=dict(
            title=xaxis_title
        ),
        yaxis=dict(
            title="Probability density"
        )
    )

    return go.Figure(data=[trace], layout=layout)


def plot_scatter(x_data, y_data):
    """
    Plots 2d datapoints with coordinates in x_data and y_data.
    """
    trace = go.Scatter(
      x=x_data,
      y=y_data,
      mode="markers"
    )

    layout = go.Layout(
        xaxis=dict(
          title="x"
        ),
        yaxis=dict(
          title="y"
        )
    )

    fig = go.Figure(data=[trace], layout=layout)

    return fig


def plot_regression(x_data, y_data, regressor):
    """
    Plots 2d datapoints with coordinates in x_data and y_data and overlays
    predictions given by regressor in the same interval of x values where the
    data lives.
    """
    x_plot = np.linspace(
        x_data.min(),
        x_data.max(),
        1000
    )

    y_plot = regressor.coef_[0] * x_plot + regressor.intercept_

    trace_data = go.Scatter(
        x=x_data[:, 0],
        y=y_data,
        mode="markers",
        name="data"
    )

    trace_fit = go.Scatter(
        x=x_plot,
        y=y_plot,
        name="regression line"
    )

    layout = go.Layout(
        xaxis=dict(
          title="x"
        ),
        yaxis=dict(
          title="y"
        )
    )

    fig = go.Figure(data=[trace_data, trace_fit], layout=layout)

    return fig


def plot_distr(values, distr, title=None, xaxis_title=None):
    """
    Plots the histogram of some data and a (hopefully fitted) probability
    distribution.
    """
    trace_hist = go.Histogram(
        x=values,
        histnorm="probability density"
    )

    x_domain = np.linspace(values.min(), values.max(), 1000)

    trace_distr = go.Scatter(
        x=x_domain,
        y=distr.pdf(x_domain)
    )

    layout = go.Layout(
        title=go.layout.Title(
            text=title,
            x=0.5
        ),
        xaxis=dict(
            title=xaxis_title
        ),
        yaxis=dict(
            title="Probability density"
        )
    )

    return go.Figure(data=[trace_hist, trace_distr], layout=layout)
