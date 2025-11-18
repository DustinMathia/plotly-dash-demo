# add callbacks to make components interact with each other
import dash
from dash import Dash, html, dcc 
from dash import callback, Output, Input #!
import plotly.express as px

dash.register_page(__name__, path='/3', name='3')

df = px.data.wind()

layout = html.Div([
    html.H1(children='My wind app', style={'textAlign':'center'}),
    dcc.Dropdown(['direction', 'strength'], 'direction', id='dropdown_3'),
    dcc.Graph(id='graph-fig_3')
])

@callback( #!
    Output('graph-fig_3', 'figure'),
    Input('dropdown_3', 'value')
)
def update_graph_3(value): #!
    return px.scatter(df, x=value, y='frequency')



if __name__ == '__main__':
    app.run(debug=True)

