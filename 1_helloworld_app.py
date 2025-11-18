# make the minimal dash app

from dash import Dash, html, dcc

app = Dash()

app.layout = [
    html.H1(children='Hello World', style={'textAlign':'center'}),
]

if __name__ == '__main__':
    app.run(debug=True)

