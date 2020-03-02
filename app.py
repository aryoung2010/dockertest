#!/usr/bin/env python
import pandas as pd
import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

hurricanes = pd.read_csv('./county_measures_no_outcomes.csv')
col_options = [dict(label=x, value=x) for x in hurricanes.columns]
dimensions = ["DV"]

app = dash.Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)

app.layout = html.Div(
    [
        html.H1("Hurricane Measures"),
        html.Div(
            [
                html.P([d + ":", dcc.Dropdown(id=d, options=col_options)])
                for d in dimensions
            ],
            style={"width": "25%", "float": "left"},
        ),
        dcc.Graph(id="graph", style={"width": "75%", "display": "inline-block"}),
    ]
)


@app.callback(Output("graph", "figure"), [Input(d, "value") for d in dimensions])
def make_figure(x, y):
    
    return px.bar(hurricanes, 
                   x=x, 
                   y=y, 
                   color="Storm",
                   height=700)

app.run_server(debug=False)

