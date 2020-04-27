import plotly.graph_objects as go

def plot():
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y = [3, 2, 1],
        name = "data1"
    ))

    fig.update_layout(
        title="Plot One",
        xaxis_title="Plot One X Axis",
        yaxis_title="Plot One Y Axis"
    )
    print("Plot One")
    fig.show()
###
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        y = [1, 2, 3],
        name = "data2"
    ))
    fig2.update_layout(
        title="Plot Two",
        xaxis_title="Plot Two X Axis",
        yaxis_title="Plot Two Y Axis"
    )
    print("Plot Two")
    fig2.show()
test = plot()
test
