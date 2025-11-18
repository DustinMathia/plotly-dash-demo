# add multipage support and a navigation bar
# make a /pages folder and put all your apps you want to be pages in it, add "dash.register_page(__name__, path='/', name='1')" in those apps
# and remove app = Dash()
# add some args in the dash constructor
# make a seperate "home" app that is only the navbar
# https://dash.plotly.com/urls

import dash #! import all of dash
from dash import Dash, html, dcc 
from dash import callback, Output, Input
import plotly.express as px


import dash_bootstrap_components as dbc


dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"


app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.MORPH, dbc.icons.FONT_AWESOME, dbc_css]) #! add use_pages=True

#! make navbar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("1", active="exact", href="/")),
        dbc.NavItem(dbc.NavLink("2", active="exact", href="/2")),
        dbc.NavItem(dbc.NavLink("3", active="exact", href="/3")),
        dbc.NavItem(dbc.NavLink("4", active="exact", href="/4")),
        dbc.NavItem(dbc.NavLink("5", active="exact", href="/5")),
    ],
)

app.layout = html.Div(
    [
        navbar,
        # This component is required! It renders the content of the current page.
        dbc.Container(dash.page_container, fluid=True) 
    ]
)

if __name__ == '__main__':
    app.run(debug=True)

