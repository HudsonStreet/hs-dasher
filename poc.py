import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from pandas_datareader import data as web
from datetime import datetime as dt

app = dash.Dash('Hello World')

app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'NIO', 'value': 'NIO'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'},
            {'label': 'Deutsche X-trackers Harvest CSI300 CHN A', 'value': 'ASHR'},
            {'label': 'Harvest CSI 500 China-A Shares Small Cap ETF', 'value': 'ASHS'},
            {'label': '摩根史坦利中国A股指数基金', 'value': 'CAF'},
            {'label': 'ETF-iShares FTSE', 'value': 'FXI'},
            {'label': 'Direxion Daily FTSE China Bull 3X ETF', 'value': 'YINN'},
            {'label': '中证小盘股做多ETF', 'value': 'CNXT'},
            {'label': '沪深300', 'value': 'CHAU'},
        ],
        value='NIO'
    ),
    dcc.Graph(id='my-graph')
], style={'width': '500'})

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
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