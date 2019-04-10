import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go
from textblob import TextBlob
from datetime import datetime as dt

from apptest import app

pd.options.mode.chained_assignment = None

def sentiment_graph_twitter(dff):
    dff = dff[dff.tweet_reply_to_user_id.notnull()]
    
    score_sentiment = dff.apply(lambda row : TextBlob(row["tweet_text"]).sentiment.polarity, axis = 1) 
    if score_sentiment.empty:
        score_sentiment = []
    
    dff['score_sentiment'] = pd.Series(score_sentiment)
    dff['tweet_date_creation'] = pd.to_datetime(dff['tweet_date_creation'])
    dff['day'] = dff['tweet_date_creation'].dt.strftime('%Y-%m-%d')
    dff = dff.groupby(['day'], group_keys=False).apply(lambda x : pd.Series({
        'Nb_tweets' : x['tweet_id'].count(),
        'Nb_positif' : (x['score_sentiment']>0).sum(),
        'Nb_negatif': (x['score_sentiment']<0).sum(),
        'Nb_neutre': (x['score_sentiment']==0).sum()}))
    dff = dff.reset_index()
    
    x = []
    traces = [[],[],[]]
    
    for i in range(len(dff)):
        l = dff.iloc[i].tolist()
        x.append(l[0])
        total = l[1]
        traces[0].append(l[3]/total)
        traces[1].append(l[4]/total)
        traces[2].append(l[2]/total)
    
    trace0 = go.Bar(
        x=x,
        y=traces[0],
        text=[str(round(i*100))+'%' for i in traces[0]],
        textposition='auto',
        name='Negative Tweets',
        marker=dict(color='rgba(219, 64, 82, 0.7)',
                    line=dict(color='rgba(219, 64, 82, 1.0)',
                              width=2)))
    trace1 = go.Bar(
        x=x,
        y=traces[1],
        text=[str(round(i*100))+'%' for i in traces[1]],
        textposition='auto',
        name='Neutral Tweets',
        marker=dict(color='rgba(55, 128, 191, 0.7)',
                    line=dict(color='rgba(55, 128, 191, 1.0)',
                              width=2)))
    trace2 = go.Bar(
        x=x,
        y=traces[2],
        text=[str(round(i*100))+'%' for i in traces[2]],
        textposition='auto',
        name='Positive Tweets',
        marker=dict(color='rgba(50, 171, 96, 0.7)',
                    line=dict(color='rgba(50, 171, 96, 1.0)',
                              width=2)))
    data = [trace0, trace1, trace2]
    layout = {
      'xaxis': {'title': 'Date', 'tickangle': '-45'},
      'yaxis': {'title': 'Positive/Neutral/Negative comments', 'tickformat': '%'},
      'barmode': 'relative'
    }
    return {'data': data, 'layout': layout}

def temporal_graph_twitter(dff):
    dff['tweet_date_creation'] = pd.to_datetime(dff['tweet_date_creation'])
    dff['day'] = dff['tweet_date_creation'].dt.strftime('%Y-%m-%d')
    dff = dff.groupby(['day'], group_keys=False).apply(lambda x : pd.Series({
        'Nb_tweets' : (~x.tweet_reply_to_user_id.notnull()).sum(),
        'Nb_comments': (x.tweet_reply_to_user_id.notnull()).sum()}))
    dff = dff.reset_index()
    
    x = []
    trac1 = []
    trac2 = []
    
    for i in range(len(dff)):
        l = dff.iloc[i].tolist()
        x.append(l[0])
        trac1.append(l[1])
        trac2.append(l[2])
    
    trace1 = go.Bar(
        x=x,
        y=trac1,
        text=trac1,
        textposition='auto',
        name='Tweets',
        marker=dict(color='rgba(92, 214, 92, 0.7)',
                    line=dict(color='rgba(92, 214, 92, 1.0)',
                              width=2)))
    trace2 = go.Bar(
        x=x,
        y=trac2,
        text=trac2,
        textposition='auto',
        name='Comments',
        marker=dict(color='rgba(140, 140, 140, 0.7)',
                    line=dict(color='rgba(140, 140, 140, 1.0)',
                              width=2)))
    
    data = [trace1, trace2]
    layout = {
      'xaxis': {'title': 'Date', 'tickangle': '-45'},
      'yaxis': {'title': 'Number of tweets/comments'},
      'barmode': 'relative'
    }
    return {'data': data, 'layout': layout}

df = pd.read_csv("C:/Users/Raph/Desktop/Dashtest/data/Twitter_Renault.csv")

body = dbc.Container([
        dbc.Row([
            dbc.Col(dbc.CardGroup([
                dbc.Card([
                    dbc.CardHeader("Twitter", style={'text-align': 'center'}),
                    dbc.CardImg(src="/static/twitter.png", top=True),
                    dbc.CardFooter([
                        daq.BooleanSwitch(on=True, color="#D0E49F")
                    ])
                ]),
                dbc.Card([
                    dbc.CardHeader("Facebook", style={'text-align': 'center'}),
                    dbc.CardImg(src="/static/facebook.png", top=True),
                    dbc.CardFooter([
                        daq.BooleanSwitch(on=False, color="#D0E49F")
                    ])
                ]),
                dbc.Card([
                    dbc.CardHeader("YouTube", style={'text-align': 'center'}),
                    dbc.CardImg(src="/static/youtube.png", top=True),
                    dbc.CardFooter([
                        daq.BooleanSwitch(on=True, color="#D0E49F")
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
            dbc.CardGroup([
                dbc.Card([
                    dbc.CardHeader("Number of Tweets", style={'text-align': 'center'}),
                    dbc.CardBody([
                        dbc.CardTitle(id="nb_posts", children="0", style={'text-align': 'center'}),
                    ]),
                ], color="dark", outline=True),
                dbc.Card([
                    dbc.CardHeader("Number of comments", style={'text-align': 'center'}),
                    dbc.CardBody([
                        dbc.CardTitle(id="nb_comments", children="0", style={'text-align': 'center'}),
                    ]),
                ], color="dark", outline=True),
                dbc.Card([
                    dbc.CardHeader("Number of Retweets", style={'text-align': 'center'}),
                    dbc.CardBody([
                        dbc.CardTitle(id="nb_retweets", children="0", style={'text-align': 'center'}),
                    ]),
                ], color="dark", outline=True),
                dbc.Card([
                    dbc.CardHeader("Number of followers", style={'text-align': 'center'}),
                    dbc.CardBody([
                        dbc.CardTitle("130k", style={'text-align': 'center'}),
                    ]),
                ], color="dark", outline=True),
                dbc.Card([
                    dbc.CardHeader("Twitter score", style={'text-align': 'center'}),
                    dbc.CardBody([
                        dbc.CardTitle("7/10", style={'text-align': 'center'}),
                    ]),
                ], color="dark", outline=True),
            ])
        ], justify="center", className="mb-4"),
        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardHeader(html.H3("Temporal Evolution"), style={'text-align': 'center'}),
                dcc.Graph(id='temporal_evolution')
            ]), width=6),
            dbc.Col(dbc.Card([
                dbc.CardHeader(html.H3("Sentiment Analysis"), style={'text-align': 'center'}),
                dcc.Graph(id='sentiment_analysis')
            ]), width=6)
        ], className="mb-3"),
        dbc.Row([html.H2("Wordclouds")], justify="center"),
        dbc.Row([
            dbc.CardGroup([
                dbc.Card([
                    dbc.CardHeader(html.H3("Posts"), style={'text-align': 'center'}),
                    dbc.CardImg(src="/static/wordcloudposts.png", bottom=True)
                ]),
                dbc.Card([
                    dbc.CardHeader(html.H3("Comments"), style={'text-align': 'center'}),
                    dbc.CardImg(src="/static/wordcloudcomments.png", bottom=True)
                ])
            ])
        ], className="mb-4"),
        html.Div(id='data_Twitter', style={'display': 'none'})
    ],
    className="mt-4",
)

@app.callback(
    Output('data_Twitter', 'children'),
    [Input('period', 'start_date'),
     Input('period', 'end_date')])
def update_cache(start_date, end_date):
    start = dt.strptime(start_date, '%Y-%m-%d').strftime('%Y-%m-%d') + ' 00:00:00'
    end = dt.strptime(end_date, '%Y-%m-%d').strftime('%Y-%m-%d') + ' 23:59:59'
    
    dff = df[(df['tweet_lang']=='en') &
             (df['tweet_date_creation']>=start) &
             (df['tweet_date_creation']<=end)]
    
    return dff.to_json()

@app.callback(
    Output('sentiment_analysis', 'figure'),
    [Input('data_Twitter', 'children')])
def graph_sentiment(cached_data):
    dff = pd.read_json(cached_data)
    fig = sentiment_graph_twitter(dff)
    return fig

@app.callback(
    Output('temporal_evolution', 'figure'),
    [Input('data_Twitter', 'children')])
def graph_temporal(cached_data):
    dff = pd.read_json(cached_data)
    fig = temporal_graph_twitter(dff)
    return fig

@app.callback(
    Output('nb_posts', 'children'),
    [Input('data_Twitter', 'children')])
def nb_posts_twitter(cached_data):
    dff = pd.read_json(cached_data)
    dff = dff[~dff.tweet_reply_to_user_id.notnull()]
    return str(dff.drop_duplicates().count()[0])

@app.callback(
    Output('nb_comments', 'children'),
    [Input('data_Twitter', 'children')])
def nb_comments_twitter(cached_data):
    dff = pd.read_json(cached_data)
    dff = dff[dff.tweet_reply_to_user_id.notnull()]
    return str(dff.drop_duplicates().count()[0])

@app.callback(
    Output('nb_retweets', 'children'),
    [Input('data_Twitter', 'children')])
def nb_retweets(cached_data):
    dff = pd.read_json(cached_data)
    dff = dff[dff['tweet_text'].str.startswith("RT ")]
    return str(dff.drop_duplicates().count()[0])
