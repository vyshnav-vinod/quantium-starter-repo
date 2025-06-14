from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv("pink_morsels_processed_data.csv")

app.layout = html.Div(
    style={
        'backgroundColor': '#f9f9f9',
        'fontFamily': 'Arial, sans-serif',
        'padding': '40px'
    },
    children=[
        html.H1(
            children='Pink Morsel Sales',
            style={
                'textAlign': 'center',
                'color': '#d63384',
                'marginBottom': '30px'
            }
        ),

        html.Div(
            children='''Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?''',
            style={
                'textAlign': 'center',
                'fontSize': '18px',
                'marginBottom': '30px'
            }
        ),

        dcc.Graph(
            id='line-graph',
            style={
                'margin': '0 auto',
                'maxWidth': '800px'
            }
        ),

        html.Div(
            children=dcc.RadioItems(
                ["North", "South", "East", "West", "All"],
                id="radio-region",
                inline=True,
                value="All",
                style={
                    'display': 'inline-block',
                    'padding': '10px',
                    'fontSize': '16px'
                }
            ),
            style={
                'textAlign': 'center',
                'marginTop': '20px'
            }
        )
    ]
)

@callback(
    Output('line-graph', 'figure'),
    Input('radio-region', 'value')
)
def select_region_and_update_graph(selected_value):
    df_val = df[df["region"] == selected_value.lower()] if selected_value != "All" else df
    fig = px.line(df_val, x="date", y="sales", title=f"Sales in {selected_value} Region" if selected_value != "All" else "Sales in All Regions")
    fig.update_layout(
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#333')
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)
