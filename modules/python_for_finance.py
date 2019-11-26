import plotly.graph_objs as go


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
