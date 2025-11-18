# add a dcc.store to store maximum frequency value, and a slider to draw a horizontal line
# 2 more callbacks, one dcc.store, add_hline in update_graph
import dash
from dash import Dash, html, dcc 
from dash import callback, Output, Input
import plotly.express as px

dash.register_page(__name__, path='/4', name='4')

df = px.data.wind()

layout = html.Div([
    dcc.Store(id='store-freq-max_4'), #!
    html.H1(children='My wind app', style={'textAlign':'center'}),
    
    dcc.Dropdown(['direction', 'strength'], 'direction', id='dropdown_4'),
    dcc.Graph(id='graph-fig_4'),
    dcc.Slider(0, 5, id='slider_4', updatemode='drag',), #!
])


######## callbacks #######


# stores max value in dcc.store
@callback( #!
    Output('store-freq-max_4', 'data'),
    Input('store-freq-max_4', 'id'), #! this is a dummy input that triggers when app starts
)
def store_max_frequency_4(id_value): #!
    #get max value from frequency column from df
    max_freq = df['frequency'].max()
    # store int in dcc.store
    return max_freq


#set slider max to store-freq-max value
@callback(
    Output('slider_4', 'max'),
    Input('store-freq-max_4', 'data'),
)
def set_slider_max_4(freq_max):
    if freq_max is not None:
        return freq_max
    return 100 # Default if data hasn't loaded


# draws graph
@callback(
    Output('graph-fig_4', 'figure'),
    Input('dropdown_4', 'value'),
    Input('slider_4', 'value'),
)
def update_graph_4(value, slider_value):
    fig = px.scatter(df, x=value, y='frequency')

    #! if slider has a value, add_hline at value
    if slider_value is not None:
        fig.add_hline(
            y=slider_value, 
            line_dash="dash",
            line_color='orange',
        )

    return fig


if __name__ == '__main__':
    app.run(debug=True)

