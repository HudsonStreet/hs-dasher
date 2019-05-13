import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
from datetime import datetime as dt
import plotly.graph_objs as graob

##Load vix data
headers = ['date_time', 'vix_value']
dtypes = {'date_time':'str', 'vix_value': 'str'}
parse_dates = ['date_time']
df = pd.read_csv("../VIX_Calculator/vix_w_datetime.csv", header=None, names=headers, dtype=dtypes, parse_dates=parse_dates)
df = df.dropna()
df['date_time'] = pd.to_datetime(df.date_time, infer_datetime_format=True)
df['Month'] = df['date_time'].dt.month
df['Day'] = df['date_time'].dt.day
#df['TimeOfDate'] = df['date_time'].dt.time()
df['Hour'] = df['date_time'].dt.hour
df['Minute'] = df['date_time'].dt.minute

print(df['date_time'])
print(df['vix_value'])
print(df['Hour'])
print(df['Minute'])
#print(df['TimeOfDate'])

app = dash.Dash(__name__)

app.layout = html.Div([
   html.Div([
        html.H1("HS Options VIX"),
    ], style={
        'textAlign': "center"}),

    dcc.Graph(id='options_vix_graph'),
    # dcc.Interval(id='refresh', Interval=100)

    # html.Div([
    #     dcc.Slider(
    #     id='time_slider',
    #     min=0,
    #     max=5,
    #     marks={
    #         0: '1 day', 
    #         1: '5 days',
    #         2: '1 month',
    #         3: '3 months',
    #         4: '6 months',
    #         5: 'YTD'
    #     },
    #     value=1,
    # )
    # ])    
], className="container")

@app.callback(
    Output('options_vix_graph', 'figure')
    #events=[Event('refresh', 'interval')]
    # [Input('time_slider','value')] 
)
def update_graph():
    trace = []

    trace.append(graob.Scatter(
        x = df["Month"],
        y = df["vix_value"],
        mode='lines',
        opacity=0.7,
        name=f'VIX',
        textposition='bottom center',
    ))

    # traces = [trace1]
    # data = [val for sublist in traces for val in sublist]
    
    return {
        'data': trace,
        'layout': graob.Layout(
            colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
            height=600,
            title=f"Options vix",
            xaxis={"title":"Date",
            #     'rangeselector': {'buttons': list([
            #     {'count': 1, 'label': '1M', 'step': 'month', 'stepmode': 'backward'},
            #     {'count': 6, 'label': '6M', 'step': 'month', 'stepmode': 'backward'},
            #     {'step': 'all'}
            # ])}, 'rangeslider': {'visible': True}, 'type': 'date'},
            },
            yaxis={
                "title":"VIX",
            }
        )
    }

# app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server(debug=True)
    
    #For testing
    # headers = ['date_time', 'vix_value']
    # dtypes = {'date_time':'str', 'vix_value': 'str'}
    # parse_dates = ['date_time']
    # VIX_DATA_FORM = pd.read_csv("../VIX_Calculator/vix_w_datetime.csv", header=None, names=headers, dtype=dtypes, parse_dates=parse_dates)

    # print(VIX_DATA_FORM)
