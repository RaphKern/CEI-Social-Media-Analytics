# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:57:52 2019

@author: Raph
"""

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

from apps import overview, competitors, recommendations, settings, alerts
from apptest import app

navbar = dbc.NavbarSimple([
            dbc.Nav([
                dbc.NavItem(dbc.NavLink('Overview', href="/")),
                dbc.NavItem(dbc.NavLink('Competitors', href="/competitors")),
                dbc.NavItem(dbc.NavLink('Recommendations', href="/recommendations")),
                dbc.NavItem(dbc.NavLink('Settings', href="/settings")),
                dbc.NavItem(dbc.NavLink('', href="/settings"), className='border-right border-dark'),
                dbc.NavItem(dbc.NavLink('', href="/alerts")),
                dbc.NavItem(dbc.NavLink('Alerts', href="/alerts")),
                dbc.NavItem(dbc.Badge("17", id="nb_alerts", color="success", pill=True)),
                dbc.NavItem(dbc.NavLink('')),
                dbc.NavItem(dbc.NavLink('')),
                dbc.NavItem(dbc.NavLink('')),
                dbc.NavItem(dbc.NavLink('')),
                dbc.NavItem(dbc.NavLink('')),
                dbc.NavItem(dbc.NavLink('')),
                dbc.NavItem(html.A(html.Img(src="/static/TNP.png", width="60", height="28", alt=""), 
                                        href="https://www.tnpconsultants.com", target="_blank"))
            ], pills=True, justified=True, navbar=True)
        ],
        brand="Social Media Analytics",
        color='#D0E49F',
        sticky="top")

app.layout = html.Div([
    html.Meta(name="viewport", content="width=device-width, initial-scale=1, shrink-to-fit=no"),
    dcc.Location(id='url', pathname=None, refresh=False),
    navbar,
    html.Div(id='body')
])

@app.callback(Output('body', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)
    if pathname is None or pathname == '/':
        return overview.body
    if pathname.rstrip('/') == '/competitors':
        return competitors.body
    elif pathname.rstrip('/') == '/recommendations':
        return recommendations.body
    elif pathname.rstrip('/') == '/settings':
        return settings.body
    elif pathname.rstrip('/') == '/alerts':
        return alerts.body
    else:
        return '404'

if __name__ == "__main__":
    app.run_server(debug=False)





