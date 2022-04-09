import plotly
import plotly.graph_objs as go

plotly.offline.plot({
    "data": [go.Scatter(x=['A', 'B', 'C', 'D'], y=[1, 2, 3, 4])],
        "layout": go.Layout(title="line chart")
	}, auto_open=True)