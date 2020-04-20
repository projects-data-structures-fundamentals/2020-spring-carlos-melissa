import plotly.graph_objects as go

def plot():
    fig = go.Figure(data=go.Bar(y=[2, 3,1]))
    print("I printed this")
    fig.show()
test = plot()
test
