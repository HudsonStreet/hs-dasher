import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from pandas_datareader import data as web
from datetime import datetime as dt

app = dash.Dash('HS Options Vix')

app.layout = html.Div([
    html.H1(children='HS Options Vix'),

    # dcc.Dropdown(
    #     id='my-dropdown',
    #     options=[
    #         {'label': 'NIO', 'value': 'NIO'},
    #         {'label': 'Tesla', 'value': 'TSLA'},
    #         {'label': 'Apple', 'value': 'AAPL'},
    #         {'label': 'Deutsche X-trackers Harvest CSI300 CHN A', 'value': 'ASHR'},
    #         {'label': 'Harvest CSI 500 China-A Shares Small Cap ETF', 'value': 'ASHS'},
    #         {'label': '摩根史坦利中国A股指数基金', 'value': 'CAF'},
    #         {'label': 'ETF-iShares FTSE', 'value': 'FXI'},
    #         {'label': 'Direxion Daily FTSE China Bull 3X ETF', 'value': 'YINN'},
    #         {'label': '中证小盘股做多ETF', 'value': 'CNXT'},
    #         {'label': '沪深300', 'value': 'CHAU'},
    #     ],
    #     value='NIO'
    # ),
    
    dcc.Graph(id='my-graph'),

    html.Div([
        dcc.Slider(
        id='my-slider',
        min=0,
        max=5,
        marks={
            0: '1 day', 
            1: '5 days',
            2: '1 month',
            3: '3 months',
            4: '6 months',
            5: 'YTD'
        },
        value=1,
    )
    ])
    
], style={
        'width': 'auto',
        'borderWidth': '1px',
        'borderStyle': 'dashed',
    })

@app.callback(
    Output('my-graph', 'figure'), 
    [Input('my-dropdown', 'value'),
    Input('my-slider','value')])
def update_graph(selected_dropdown_value, selected_slider_value):
    df = web.DataReader(
        selected_dropdown_value,
        'yahoo',
        dt(2018, 1, 1),
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server()