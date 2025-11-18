# make the minimal dash app
import dash
from dash import Dash, html, dcc

dash.register_page(__name__, path='/', name='1')

layout = html.Div([
    html.H1(children='Hello World', style={'textAlign':'center'}),
])

if __name__ == '__main__':
    app.run(debug=True)

