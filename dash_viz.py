from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv("pink_morsels_processed_data.csv")

fig_all = px.line(df, x="date", y="sales", color="region")


app.layout = html.Div(children=[
    html.H1(children='Pink Morsel sales'),

    html.Div(children='''
            Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?
    '''),

    dcc.Graph(
        id='line-graph',
        figure=fig_all
    )
])

if __name__ == '__main__':
    app.run(debug=True)
