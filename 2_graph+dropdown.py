# add interactive dash core components
# dcc.graph, dcc.Dropdown, import df and make px.scatter

from dash import Dash, html, dcc
import plotly.express as px #!

app = Dash()

df = px.data.wind() #!
fig = px.scatter(df, x='direction', y='frequency') #!

app.layout = [
    html.H1(children='My wind app', style={'textAlign':'center'}),
    dcc.Dropdown(['direction', 'strength'], 'direction', id='dropdown'), #!
    dcc.Graph(figure = fig, id='graph-fig') #!
]

if __name__ == '__main__':
    app.run(debug=True)

