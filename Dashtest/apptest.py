# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:24:27 2019

@author: Raph
"""

from dash import Dash
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Social Media Analytics'
app.config.suppress_callback_exceptions = True
