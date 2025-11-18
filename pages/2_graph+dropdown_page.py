# add interactive dash core components
# dcc.graph, dcc.Dropdown, import df and make px.scatter
import dash
from dash import Dash, html, dcc
import plotly.express as px #!
dash.register_page(__name__, path='/2', name='2')

df = px.data.wind() #!
fig = px.scatter(df, x='direction', y='frequency') #!

layout = html.Div([
    html.H1(children='My wind app', style={'textAlign':'center'}),
    dcc.Dropdown(['direction', 'strength'], 'direction', id='dropdown_2'), #!
    dcc.Graph(figure = fig, id='graph-fig_2') #!
])

if __name__ == '__main__':
    app.run(debug=True)

