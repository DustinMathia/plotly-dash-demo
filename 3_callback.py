# add callbacks to make components interact with each other

from dash import Dash, html, dcc 
from dash import callback, Output, Input #!
import plotly.express as px

app = Dash()

df = px.data.wind()

app.layout = [
    html.H1(children='My wind app', style={'textAlign':'center'}),
    dcc.Dropdown(['direction', 'strength'], 'direction', id='dropdown'),
    dcc.Graph(id='graph-fig')
]

@callback( 
    Output('graph-fig', 'figure'),
    Input('dropdown', 'value'),
)
def update_graph(value): #!
    return px.scatter(df, x=value, y='frequency')



if __name__ == '__main__':
    app.run(debug=True)

