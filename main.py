# import dash
# from dash.dependencies import Input, Output
# import dash_core_components as dcc
# import dash_html_components as html

import pandas as pd
# from datetime import datetime as dt
# import plotly.graph_objs as graob

##Load vix data
# headers = ['date_time', 'vix_value']
# dtypes = {'date_time':'str', 'vix_value': 'float'}
# parse_dates = ['date_time']
# VIX_DATA_FORM = pd.read_csv("../hs-vix-calculator/vix_w_datetime.csv", header=None, names=headers, dtype=dtypes, parse_dates=parse_dates)

# app = dash.Dash(__name__)

# app.layout = html.Div([
#    html.Div([
#         html.H1("HS Options VIX"),
#     ], style={
#         'textAlign': "center"}),

#     dcc.Graph(id='options_vix_graph'),

#     html.Div([
#         dcc.Slider(
#         id='time_slider',
#         min=0,
#         max=5,
#         marks={
#             0: '1 day', 
#             1: '5 days',
#             2: '1 month',
#             3: '3 months',
#             4: '6 months',
#             5: 'YTD'
#         },
#         value=1,
#     )
#     ])
    
# ], className="container")

# @app.callback(
#     Output('options_vix_graph', 'figure'), 
#     [Input('time_slider','value')] 
# )
# def update_graph(selected_slider_value):
#     trace = []

#     return {
#         'data': [{
#             'x': df.index,
#             'y': df.Close
#         }],
#         'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
#     }

# app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    # app.run_server()
    headers = ['date_time', 'vix_value']
    dtypes = {'date_time':'str', 'vix_value': 'str'}
    parse_dates = ['date_time']
    VIX_DATA_FORM = pd.read_csv("../hs-vix-calculator/vix_w_datetime.csv", header=None, names=headers, dtype=dtypes, parse_dates=parse_dates)

    print(VIX_DATA_FORM)
