import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go
from datetime import datetime as dt

from apptest import app

pd.options.mode.chained_assignment = None

#df_tw_re = pd.read_csv("C:/Users/Raph/Desktop/Dashtest/data/Twitter_Renault.csv")
#df_tw_hy = pd.read_csv("C:/Users/Raph/Desktop/Dashtest/data/Twitter_Hyundai.csv")
#df_tw_ma = pd.read_csv("C:/Users/Raph/Desktop/Dashtest/data/Twitter_Mahindra.csv")
#df_tw_su = pd.read_csv("C:/Users/Raph/Desktop/Dashtest/data/Twitter_Suzuki.csv")
#df_tw_ta = pd.read_csv("C:/Users/Raph/Desktop/Dashtest/data/Twitter_Tatamotors.csv")

def competitors_graph_global():
    x = ['Number of subscribers/followers (k)', 'Number of videos/posts', 'Number of comments', 'Number of videos posted/Retweets']
        
    y_re = [188, 22162+3900, 3139+15494, 13375+1204]
    y_hy = [721+640, 2558+600, 204+15358, 1534+675]
    y_ma = [1270+50, 6558+600, 1161+13665, 4014+264]
    y_su = [69+42, 11957+800, 6537+3122, 5303+276]
    y_ta = [115+150, 3240+50, 2742+17805, 2028+1549]
    
    trace_re = go.Bar(
        x=x,
        y=y_re,
        text=y_re,
        textposition = 'auto',
        name= 'Renault',
        marker=dict(
            color='rgb(0,51,153)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),),
        opacity=0.6)
    
    trace_hy = go.Bar(
        x=x,
        y=y_hy,
        text=y_hy,
        textposition = 'auto',
        name= 'Hyundai',
        marker=dict(
            color='rgb(0,68,204)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),),
        opacity=0.6)
    
    trace_ma = go.Bar(
        x=x,
        y=y_ma,
        text=y_ma,
        textposition = 'auto',
        name= 'Mahindra',
        marker=dict(
            color='rgb(0,85,255)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),),
        opacity=0.6)
    
    trace_su = go.Bar(
        x=x,
        y=y_su,
        text=y_su,
        textposition = 'auto',
        name= 'Suzuki',
        marker=dict(
            color='rgb(51,119,255)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),),
        opacity=0.6)
    
    trace_ta = go.Bar(
        x=x,
        y=y_ta,
        text=y_ta,
        textposition = 'auto',
        name= 'Tatamotors',
        marker=dict(
            color='rgb(102,153,255)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),),
        opacity=0.6)
    
    data = [trace_re, trace_hy, trace_ma, trace_su, trace_ta]
    layout = {
      'xaxis': {'title': 'Metrics'},
      'yaxis': {'title': 'Quantity'},
    }
    return {'data': data, 'layout': layout}

def competitors_graph_youtube():
    x = ['Number of subscribers (k)', 'Number of videos', 'Number of comments', 'Number of videos posted']
    
    y_re = [58, 3900, 15494, 1204]
    y_hy = [640, 600, 15358, 675]
    y_ma = [50, 600, 13665, 264]
    y_su = [42, 800, 3122, 276]
    y_ta = [150, 50, 17805, 1549]
    
#    ys = [y_re, y_hy, y_ma, y_su, y_ta]
#    dffs = [dff_re, dff_hy, dff_ma, dff_su, dff_ta]
#    
#    for i in range(5):
#        dff = dffs[i]
#        y = ys[i]
#        
#        y.append(dff[~dff.tweet_reply_to_user_id.notnull()].drop_duplicates().count()[0])
#        y.append(dff[dff.tweet_reply_to_user_id.notnull()].drop_duplicates().count()[0])
#        y.append(dff[dff['tweet_text'].str.startswith("RT ")].drop_duplicates().count()[0])
    
    trace_re = go.Bar(
        x=x,
        y=y_re,
        text=y_re,
        textposition = 'auto',
        name= 'Renault',
        marker=dict(
            color='rgb(0,51,153)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),),
        opacity=0.6)
    
    trace_hy = go.Bar(
        x=x,
        y=y_hy,
        text=y_hy,
        textposition = 'auto',
        name= 'Hyundai',
        marker=dict(
            color='rgb(0,68,204)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),),
        opacity=0.6)
    
    trace_ma = go.Bar(
        x=x,
        y=y_ma,
        text=y_ma,
        textposition = 'auto',
        name= 'Mahindra',
        marker=dict(
            color='rgb(0,85,255)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),),
        opacity=0.6)
    
    trace_su = go.Bar(
        x=x,
        y=y_su,
        text=y_su,
        textposition = 'auto',
        name= 'Suzuki',
        marker=dict(
            color='rgb(51,119,255)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),),
        opacity=0.6)
    
    trace_ta = go.Bar(
        x=x,
        y=y_ta,
        text=y_ta,
        textposition = 'auto',
        name= 'Tatamotors',
        marker=dict(
            color='rgb(102,153,255)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),),
        opacity=0.6)
    
    data = [trace_re, trace_hy, trace_ma, trace_su, trace_ta]
    layout = {
      'xaxis': {'title': 'Metrics'},
      'yaxis': {'title': 'Quantity'},
    }
    return {'data': data, 'layout': layout}

def competitors_graph_twitter():
    x = ['Number of followers (k)', 'Number of tweets', 'Number of comments', 'Number of Retweets']
    
    y_re = [130, 22162, 3139, 13375]
    y_hy = [721, 2558, 204, 1534]
    y_ma = [1270, 6558, 1161, 4014]
    y_su = [69.5, 11957, 6537, 5303]
    y_ta = [115, 3240, 2742, 2028]
    
#    ys = [y_re, y_hy, y_ma, y_su, y_ta]
#    dffs = [dff_re, dff_hy, dff_ma, dff_su, dff_ta]
#    
#    for i in range(5):
#        dff = dffs[i]
#        y = ys[i]
#        
#        y.append(dff[~dff.tweet_reply_to_user_id.notnull()].drop_duplicates().count()[0])
#        y.append(dff[dff.tweet_reply_to_user_id.notnull()].drop_duplicates().count()[0])
#        y.append(dff[dff['tweet_text'].str.startswith("RT ")].drop_duplicates().count()[0])
    
    trace_re = go.Bar(
        x=x,
        y=y_re,
        text=y_re,
        textposition = 'auto',
        name= 'Renault',
        marker=dict(
            color='rgb(0,51,153)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),),
        opacity=0.6)
    
    trace_hy = go.Bar(
        x=x,
        y=y_hy,
        text=y_hy,
        textposition = 'auto',
        name= 'Hyundai',
        marker=dict(
            color='rgb(0,68,204)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),),
        opacity=0.6)
    
    trace_ma = go.Bar(
        x=x,
        y=y_ma,
        text=y_ma,
        textposition = 'auto',
        name= 'Mahindra',
        marker=dict(
            color='rgb(0,85,255)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),),
        opacity=0.6)
    
    trace_su = go.Bar(
        x=x,
        y=y_su,
        text=y_su,
        textposition = 'auto',
        name= 'Suzuki',
        marker=dict(
            color='rgb(51,119,255)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),),
        opacity=0.6)
    
    trace_ta = go.Bar(
        x=x,
        y=y_ta,
        text=y_ta,
        textposition = 'auto',
        name= 'Tatamotors',
        marker=dict(
            color='rgb(102,153,255)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),),
        opacity=0.6)
    
    data = [trace_re, trace_hy, trace_ma, trace_su, trace_ta]
    layout = {
      'xaxis': {'title': 'Metrics'},
      'yaxis': {'title': 'Quantity'},
    }
    return {'data': data, 'layout': layout}

body = dbc.Container([
        dbc.Row([
            dbc.Col(dbc.CardGroup([
                dbc.Card([
                    dbc.CardHeader("Twitter", style={'text-align': 'center'}),
                    dbc.CardImg(src="/static/twitter.png", top=True),
                    dbc.CardFooter([
                        daq.BooleanSwitch(id='switch_twitter', on=True, color="#D0E49F")
                    ])
                ]),
                dbc.Card([
                    dbc.CardHeader("Facebook", style={'text-align': 'center'}),
                    dbc.CardImg(src="/static/facebook.png", top=True),
                    dbc.CardFooter([
                        daq.BooleanSwitch(id='switch_facebook', on=False, color="#D0E49F")
                    ])
                ]),
                dbc.Card([
                    dbc.CardHeader("YouTube", style={'text-align': 'center'}),
                    dbc.CardImg(src="/static/youtube.png", top=True),
                    dbc.CardFooter([
                        daq.BooleanSwitch(id='switch_youtube', on=True, color="#D0E49F")
                    ])
                ])
            ]), width=4),
            dbc.Col(dbc.Card([
                dbc.CardHeader("Pick a period", style={'text-align': 'center'}),
                html.Div([
                    dcc.DatePickerRange(
                        id='period',
                        min_date_allowed=dt(2018, 1, 1),
                        max_date_allowed=dt(2019, 3, 17),
                        initial_visible_month="2019-01",
                        start_date="2019-01-01",
                        end_date="2019-03-01"
                    )
                    ], style={'text-align': 'center'})
            ]), width=4, align="center")
        ], justify="around", className="mb-3"),
        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardHeader(html.H3("Competitors"), style={'text-align': 'center'}),
                dcc.Graph(id='competitors')
            ]), width=12),
        ], className="mb-3"),
#        html.Div(id='data_twitter_renault', style={'display': 'none'}),
#        html.Div(id='data_twitter_hyundai', style={'display': 'none'}),
#        html.Div(id='data_twitter_mahindra', style={'display': 'none'}),
#        html.Div(id='data_twitter_suzuki', style={'display': 'none'}),
#        html.Div(id='data_twitter_tatamotors', style={'display': 'none'}),
    ],
    className="mt-4",
)

#@app.callback(
#    Output('data_twitter_renault', 'children'),
#    [Input('period', 'start_date'),
#     Input('period', 'end_date')])
#def update_cache_renault(start_date, end_date):
#    start = dt.strptime(start_date, '%Y-%m-%d').strftime('%Y-%m-%d') + ' 00:00:00'
#    end = dt.strptime(end_date, '%Y-%m-%d').strftime('%Y-%m-%d') + ' 23:59:59'    
#    dff = df_tw_re[(df_tw_re['tweet_lang']=='en') &
#                   (df_tw_re['tweet_date_creation']>=start) &
#                   (df_tw_re['tweet_date_creation']<=end)]    
#    return dff.to_json()
#
#@app.callback(
#    Output('data_twitter_hyundai', 'children'),
#    [Input('period', 'start_date'),
#     Input('period', 'end_date')])
#def update_cache_hyundai(start_date, end_date):
#    start = dt.strptime(start_date, '%Y-%m-%d').strftime('%Y-%m-%d') + ' 00:00:00'
#    end = dt.strptime(end_date, '%Y-%m-%d').strftime('%Y-%m-%d') + ' 23:59:59'    
#    dff = df_tw_hy[(df_tw_hy['tweet_lang']=='en') &
#                   (df_tw_hy['tweet_date_creation']>=start) &
#                   (df_tw_hy['tweet_date_creation']<=end)]    
#    return dff.to_json()
#
#@app.callback(
#    Output('data_twitter_mahindra', 'children'),
#    [Input('period', 'start_date'),
#     Input('period', 'end_date')])
#def update_cache_mahindra(start_date, end_date):
#    start = dt.strptime(start_date, '%Y-%m-%d').strftime('%Y-%m-%d') + ' 00:00:00'
#    end = dt.strptime(end_date, '%Y-%m-%d').strftime('%Y-%m-%d') + ' 23:59:59'    
#    dff = df_tw_ma[(df_tw_ma['tweet_lang']=='en') &
#                   (df_tw_ma['tweet_date_creation']>=start) &
#                   (df_tw_ma['tweet_date_creation']<=end)]    
#    return dff.to_json()
#
#@app.callback(
#    Output('data_twitter_suzuki', 'children'),
#    [Input('period', 'start_date'),
#     Input('period', 'end_date')])
#def update_cache_suzuki(start_date, end_date):
#    start = dt.strptime(start_date, '%Y-%m-%d').strftime('%Y-%m-%d') + ' 00:00:00'
#    end = dt.strptime(end_date, '%Y-%m-%d').strftime('%Y-%m-%d') + ' 23:59:59'    
#    dff = df_tw_su[(df_tw_su['tweet_lang']=='en') &
#                   (df_tw_su['tweet_date_creation']>=start) &
#                   (df_tw_su['tweet_date_creation']<=end)]    
#    return dff.to_json()
#
#@app.callback(
#    Output('data_twitter_tatamotors', 'children'),
#    [Input('period', 'start_date'),
#     Input('period', 'end_date')])
#def update_cache_tatamotors(start_date, end_date):
#    start = dt.strptime(start_date, '%Y-%m-%d').strftime('%Y-%m-%d') + ' 00:00:00'
#    end = dt.strptime(end_date, '%Y-%m-%d').strftime('%Y-%m-%d') + ' 23:59:59'    
#    dff = df_tw_ta[(df_tw_ta['tweet_lang']=='en') &
#                   (df_tw_ta['tweet_date_creation']>=start) &
#                   (df_tw_ta['tweet_date_creation']<=end)]    
#    return dff.to_json()

#@app.callback(
#    Output('competitors_twitter', 'figure'),
#    [Input('data_twitter_renault', 'children'),
#     Input('data_twitter_hyundai', 'children'),
#     Input('data_twitter_mahindra', 'children'),
#     Input('data_twitter_suzuki', 'children'),
#     Input('data_twitter_tatamotors', 'children')])
#def update_competitors(ren, hyu, mah, suz, tat):
#    dff_re = pd.read_json(ren)
#    dff_hy = pd.read_json(hyu)
#    dff_ma = pd.read_json(mah)
#    dff_su = pd.read_json(suz)
#    dff_ta = pd.read_json(tat)
#    fig = competitors_graph(dff_re, dff_hy, dff_ma, dff_su, dff_ta)
#    return fig

@app.callback(
    Output('competitors', 'figure'),
    [Input('switch_twitter', 'on'),
     Input('switch_youtube', 'on')])
def update_social_network(twitter, youtube):
    if twitter and youtube :
        return competitors_graph_global()
    elif twitter and not(youtube):
        return competitors_graph_twitter()
    elif not(twitter) and youtube:
        return competitors_graph_youtube()
    else:
        return []