import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import pandas as pd
import numpy as np
import pathlib
import dash_auth
from flask import Flask, request, Response

users = [
    ['a', 'a'],
    ['edodemexico', 'J$@9m#Px&Zq2s5L'],
    ['veracruz', '8#vY@p4KwU!tN7D'],
    ['yucatan', 'x6F@W%3RzPv*G2Q'],
    ['aguascalientes', 'A@B3cD4eF5gH6iJ7'],
    ['bajacalifornia', 'Z9@Y8xW7vU6tS5r'],
    ['bajacaliforniasur', 'L#M3qKpN7oR6nG5'],
    ['campeche', '2P#Q6O$T8V!X7U%'],
    ['chiapas', 'H$I1S@M9F&G5T3J'],
    ['chihuahua', 'V2#R8wX$Z1sK@L9'],
    ['cohauila', 'Y!P&K2oC7A#E4qD'],
    ['colima', 'T5#Z%W3P@U1M7N8'],
    ['durango', '6L@KpT3GvHwS9f#'],
    ['ciudaddemexico', '7b#Xm$V5Z@K2jG'],
    ['guanajuato', 'L4#PvQ6YtS$Zx8'],
    ['guerrero', 'S3#R5KvL6M$HwI'],
    ['hidalgo', '9N@U7O1P#YmTj5 '],
    ['jalisco', 'X6#QwS2P@LdKm3'],
    ['michoacan', 'W@7X6T8#YzPq1R'],
    ['morelos', '4J@KvG5DwZxT3M'],
    ['nayarit', 'I6#QyVzE1P@F2h'],
    ['nuevoleon', 'G5#BtX3UwP$Rz8'],
    ['oaxaca', '7#WmYqKp@S9vD2'],
    ['puebla', '1F@KdR5vG2X#M9'],
    ['queretaro', 'U2#SjZ5Rm7PvX8'],
    ['quintanaroo', 'K6#L@H3P7MvYz1']
]
server = Flask(__name__)
app = Dash(__name__, use_pages=True, server=server)

auth = dash_auth.BasicAuth(app, users)

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=5000)
