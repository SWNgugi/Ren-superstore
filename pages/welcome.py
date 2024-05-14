import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/", title='Welcome', name='Project')

superstore = pd.read_csv('data/Sample - Superstore.csv', encoding='latin1')

# Layout
layout = html.Div(
   children=[
      dbc.Row(
            children = [
                dbc.Col(
                    "Project about"
                )
            ]
        )
    ],
)