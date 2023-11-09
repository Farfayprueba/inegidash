import dash
from dash import dcc
from dash import html,callback
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import pandas as pd
import numpy as np
import pathlib
import dash_auth
from flask import request

font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]
inegi = pd.read_csv('inegi.csv')
seguridad = pd.read_csv('seguridad.csv')
inegi.replace("*", 0, inplace=True)
inegi = inegi.apply(pd.to_numeric, errors='ignore')
dash.register_page(__name__, external_stylesheets = external_stylesheets, path='/')

def get_username():
    return request.authorization['username'] if request.authorization else None

@callback(
    [Output('select_est', 'options'),
     Output('select_est', 'value')],
    Input('select_est', 'value')
)
def update_dropdown_options(selected_value):
    username = get_username()
    if username == "a":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'] == "Yucatán", 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "yucatan":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'] == "Yucatán", 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "edodemexico":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'] == "México", 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "veracruz":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'] == "Veracruz de Ignacio de la Llave", 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "aguascalientes":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'] == "Aguascalientes", 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "bajacalifornia":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'] == "Baja California", 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "bajacaliforniasur":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Baja California Sur"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "campeche":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Campeche"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "chiapas":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Chiapas"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "chihuahua":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Chihuahua"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "cohauila":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Coahuila de Zaragoza"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "colima":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Colima"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "durango":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Durango"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "ciudaddemexico":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Ciudad de México"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "guanajuato":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Guanajuato"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "guerrero":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Guerrero"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "hidalgo":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Hidalgo"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "jalisco":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Jalisco"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "michoacan":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Michoacán de Ocampo"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "morelos":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Morelos"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "nayarit":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Nayarit"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "nuevoleon":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Nuevo León"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "oaxaca":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Oaxaca"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "puebla":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Puebla"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "queretaro":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Querétaro"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "quintanaroo":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Quintana Roo"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "nacional":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc['NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    else:
        return [], None
    
layout = html.Div([
    html.Div([
        html.Div([
            html.Img(
                src='/assets/statistics.png',
                style={'height': '30px'},
                className='title_image'
            ),
            html.H6('Factores sociodemograficos',
                    style = {'color': '#D35940'},
                    className = 'title'
                    ),
        ], className = 'logo_title'),

        html.Div([
            html.P('Seleccionar filtro',
                   style = {'color': '#D35940'},
                   className = 'drop_down_list_title'
                   ),
            dcc.Dropdown(
                id='select_est',
                value=None,
                multi=False,
                clearable=True,
                disabled=False,
                placeholder='Seleccionar estado',
                className='drop_down_list'
            ),
            dcc.Dropdown(
                id='select_mun',
                multi=False,
                clearable=True,
                disabled=True,  # Inicialmente deshabilitado
                placeholder='Seleccionar municipio',
                className='drop_down_list'
            ),
            dcc.Dropdown(id = 'select_year',
                         multi = False,
                         clearable = True,
                         disabled = False,
                         style = {'display': True},
                         value = 2023,
                         placeholder = 'Seleccionar municipio',
                         options = [{'label': c, 'value': c}
                                    for c in seguridad['Año'].unique()],
                         className = 'drop_down_list'),
        ], className = 'title_drop_down_list'),
    ], className = 'title_and_drop_down_list'),

    html.Div([
        html.Div([
            html.Div([
                #amarillo es un
                html.Div([
                    html.Div([
                        html.P('Poblacion Femenina',
                               className = 'format_text')
                    ], className = 'accounts_receivable1'),
                    html.Div([
                        html.Div(id = 'accounts_receivable_value',
                                 className = 'numeric_value')
                    ], className = 'accounts_receivable2')
                ], className = 'accounts_receivable_column'),
                
                html.Div([
                    html.Div([
                        html.P('Poblacion mayor',
                               className = 'format_text')
                    ], className = 'accounts_payable1'),
                    
                    html.Div([
                        html.Div(id = 'accounts_payable_value',
                                 className = 'numeric_value')
                    ], className = 'accounts_payable2')
                ], className = 'accounts_payable_column'),
                
            ], className = 'receivable_payable_column'),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Poblacion Masculina',
                               className = 'format_text')
                    ], className = 'income1'),
                    html.Div([
                        html.Div(id = 'income_value',
                                 className = 'numeric_value')
                    ], className = 'income2')
                ], className = 'income_column'),
                html.Div([
                    html.Div([
                        html.P('Poblacion total',
                               className = 'format_text')
                    ], className = 'expenses1'),
                    html.Div([
                        html.Div(id = 'poblacion_total',
                                 className = 'numeric_value')
                    ], className = 'expenses2')
                ], className = 'expenses_column'),
                
                
            ], className = 'income_expenses_column'),
        ], className = 'first_row'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                    ], className = 'first_left_circle'),
                    html.Div([
                        html.Div(id = 'primercirculo'),
                    ], className = 'second_left_circle'),
                ], className = 'first_second_left_column'),
            ], className = 'left_circle_row'),
            dcc.Graph(id = 'chart1',
                      config = {'displayModeBar': False},
                      className = 'donut_chart_size'),
        ], className = 'text_and_chart'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                    ], className = 'first_right_circle'),
                    html.Div([
                        html.Div(id = 'segundocirculo'),
                    ], className = 'second_right_circle'),
                ], className = 'first_second_right_column'),
            ], className = 'right_circle_row'),
            dcc.Graph(id = 'chart2',
                      config = {'displayModeBar': False},
                      className = 'donut_chart_size'),

            html.Div([
                html.Div([
                    html.Div([
                        html.P('Instituciones de Seguro Medico',
                               className = 'format_text')
                    ], className = 'income_statement'),
                    html.Div([
                        html.Div([
                            html.Div([
                                dcc.Graph(id = 'instituciones',
                                    config = {'displayModeBar': False},
                                    className = 'bar_chart_size2')
                            ], className = 'income_statement_indicator_row1'),
                        ], className = 'in_state_column')
                    ], className = 'income_statement_multiple_values'),
                ], className = 'income_statement_column1'),
                
            ], className = 'net_profit1'),
        ], className = 'income_statement_row')
    ], className = 'f_row'),
    
    ############################
    
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Poblacion con discapacidades',
                               className = 'format_text')
                    ], className = 'accounts_receivable1'),
                    html.Div([
                        html.Div(id = 'discapacitada',
                                 className = 'numeric_value')
                    ], className = 'accounts_receivable2')
                ], className = 'accounts_receivable_column'),
                
            ], className = 'receivable_payable_column2'),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Poblacion con discapacidades',
                               className = 'format_text')
                    ], className = 'accounts_receivable1'),
                    html.Div([
                        html.Div(id = 'mentalillness',
                                 className = 'numeric_value')
                    ], className = 'accounts_receivable2')
                ], className = 'accounts_receivable_column'),
                
            ], className = 'receivable_payable_column2'),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Discapacidad auditiva',
                               className = 'format_text')
                    ], className = 'expenses1'),
                    html.Div([
                        html.Div(id = 'discapacidad_auditiva',
                                 className = 'numeric_value')
                    ], className = 'expenses2')
                ], className = 'expenses_column'),
            ], className = 'receivable_payable_column2'),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Discapacidad motora',
                               className = 'format_text')
                    ], className = 'expenses1'),
                    html.Div([
                        html.Div(id = 'discapacidad_motora',
                                 className = 'numeric_value')
                    ], className = 'expenses2')
                ], className = 'expenses_column'),
            ], className = 'receivable_payable_column2'),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Discapacidad visual',
                               className = 'format_text')
                    ], className = 'expenses1'),
                    html.Div([
                        html.Div(id = 'discapacidad_visual',
                                 className = 'numeric_value')
                    ], className = 'expenses2')
                ], className = 'expenses_column'),
            ], className = 'receivable_payable_column2'),
        ], className = 'first_row2'),
        
        
    ], className = 'f_row'),
##############################################################
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Sin electricidad',
                               className = 'format_text')
                    ], className = 'accounts_receivable1'),
                    html.Div([
                        html.Div(id = 'sinelectricidad',
                                 className = 'numeric_value')
                    ], className = 'accounts_receivable2')
                ], className = 'accounts_receivable_column'),
                html.Div([
                    html.Div([
                        html.P('Sin agua entubada',
                               className = 'format_text')
                    ], className = 'accounts_payable1'),
                    html.Div([
                        html.Div(id = 'current_ratio_value',
                                 className = 'numeric_value')
                    ], className = 'accounts_payable2')
                ], className = 'accounts_payable_column'),
            ], className = 'receivable_payable_column'),

            html.Div([
                html.Div([
                    html.Div([
                        html.P('Sin drenaje',
                               className = 'format_text')
                    ], className = 'income1'),
                    html.Div([
                        html.Div(id = 'net_profit_value',
                                 className = 'numeric_value')
                    ], className = 'income2')
                ], className = 'income_column'),
                html.Div([
                    html.Div([
                        html.P('Sin TICs',
                               className = 'format_text')
                    ], className = 'expenses1'),
                    html.Div([
                        html.Div(id = 'cash_at_eom_value',
                                 className = 'numeric_value')
                    ], className = 'expenses2')
                ], className = 'expenses_column'),
            ], className = 'income_expenses_column'),
        ], className = 'first_row3'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                    ], className = 'first_left_circle'),
                    html.Div([
                        html.Div(id = 'third_left_circle'),
                    ], className = 'second_left_circle'),
                ], className = 'first_second_left_column'),
            ], className = 'left_circle_row'),
            dcc.Graph(id = 'chart3',
                      config = {'displayModeBar': False},
                      className = 'donut_chart_size'),
        ], className = 'text_and_chart2'),

        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                    ], className = 'first_right_circle'),
                    html.Div([
                        html.Div(id = 'fourth_right_circle'),
                    ], className = 'second_right_circle'),
                ], className = 'first_second_right_column'),
            ], className = 'right_circle_row2'),
            dcc.Graph(id = 'chart4',
                      config = {'displayModeBar': False},
                      className = 'donut_chart_size2'),
            html.Div([
                dcc.Graph(id = 'bar_chart',
                          config = {'displayModeBar': False},
                          className = 'bar_chart_size3'),
            ], className = 'net_profit2'),
        ], className = 'income_statement_row')
    ], className = 'f_row'),

])

############################3


#############################
@callback(
    Output('select_mun', 'disabled'),
     [Output('select_mun', 'options'),
     Output('select_mun', 'value')],
    Input('select_est', 'value')
)
def update_municipios(selected_estado):
    if selected_estado is None:
        # Si no se ha seleccionado un estado, el segundo menú está deshabilitado
        return True, []
    else:
        # Habilita el segundo menú y filtra las opciones según el estado seleccionado
        municipios = inegi[inegi['NOM_ENT'] == selected_estado]['NOM_MUN'].unique()
        opciones_mun = [{'label': c, 'value': c} for c in municipios]
        value = opciones_mun[0]["value"]
        return False, opciones_mun,value


#############################


@callback(Output('poblacion_total', 'children'),
            [Input('select_mun', 'value')],
              [Input('select_est', 'value')],
              )
def update_text(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        if not filter_mun.empty:  # Verifica que el DataFrame no esté vacío
            pobtot = filter_mun['POBTOT'].values
        else:
            raise PreventUpdate
        if pobtot > 0:
            return [
                html.Div([
                    html.P('{0:,.0f}'.format(pobtot[0]),
                           ),
                    html.Img(
                        src='/assets/organizacion.png',
                        style={'height': '30px'},
                        className='title_image'
                    ),
                ], className = 'indicator_column'),
            ]

@callback(Output('discapacitada', 'children'),
            [Input('select_mun', 'value')],
              [Input('select_est', 'value')],
              )
def update_text(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        if not filter_mun.empty:  # Verifica que el DataFrame no esté vacío
            pobtot = filter_mun['POBTOT'].values
            pcon_disc = filter_mun['PCON_DISC'].values
        else:
            raise PreventUpdate
        if pcon_disc > 0:
            return [
                
                html.Div([
                    html.P('{0:,.0f}'.format(pcon_disc[0]),
                           ),
                    html.Img(
                        src='/assets/discapacidad.png',
                        style={'height': '30px'},
                        className='title_image'
                    ),
                ], className = 'indicator_column'),
            ]

@callback(Output('mentalillness', 'children'),
            [Input('select_mun', 'value')],
              [Input('select_est', 'value')],
              )
def update_text(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        if not filter_mun.empty:  # Verifica que el DataFrame no esté vacío
            pobtot = filter_mun['POBTOT'].values
            pcon_disc = filter_mun['PCDISC_MEN'].values
        else:
            raise PreventUpdate
        if pcon_disc > 0:
            return [
                
                html.Div([
                    html.P('{0:,.0f}'.format(pcon_disc[0]),
                           ),
                    html.Img(src='/assets/frasco-de-pastillas.png',
                     style = {'height': '45px'},
                     className = 'title_image'
                     ),
                ], className = 'indicator_column'),
            ]

@callback(Output('discapacidad_motora', 'children'),
            [Input('select_mun', 'value')],
              [Input('select_est', 'value')],
              )
def update_text(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        if not filter_mun.empty:  # Verifica que el DataFrame no esté vacío
            pobtot = filter_mun['POBTOT'].values
            pcon_disc = filter_mun['PCDISC_MOT'].values
        else:
            raise PreventUpdate
        if pcon_disc[0] > 0:
            return [
                html.Div([
                    html.P('{0:,.0f}'.format(pcon_disc[0]),
                           ),
                    html.Img(src='/assets/discapacidad_motora.png',
                     style = {'height': '45px'},
                     className = 'title_image'
                     ),
                ], className = 'indicator_column'),
            ]
            
@callback(Output('discapacidad_visual', 'children'),
            [Input('select_mun', 'value')],
              [Input('select_est', 'value')],
              )
def update_text(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        if not filter_mun.empty:  # Verifica que el DataFrame no esté vacío
            pobtot = filter_mun['POBTOT'].values
            pcon_disc = filter_mun['PCDISC_VIS'].values
            return [
                html.Div([
                    html.P('{0:,.0f}'.format(pcon_disc[0]),
                           ),
                    html.Img(src='/assets/discapacidad-visual.png',
                     style = {'height': '45px'},
                     className = 'title_image'
                     ),
                ], className = 'indicator_column'),
            ]
        else:
            raise PreventUpdate
        
            
@callback(Output('discapacidad_auditiva', 'children'),
            [Input('select_mun', 'value')],
              [Input('select_est', 'value')],
              )
def update_text(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        if not filter_mun.empty:  # Verifica que el DataFrame no esté vacío
            pobtot = filter_mun['POBTOT'].values
            pcon_disc = filter_mun['PCDISC_AUD'].values
            return [
                html.Div([
                    html.P('{0:,.0f}'.format(pcon_disc[0]),
                           ),
                    html.Img(src='/assets/la-discapacidad-auditiva.png',
                     style = {'height': '45px'},
                     className = 'title_image'
                     ),
                ], className = 'indicator_column'),
            ]
        else:
            raise PreventUpdate
        
############################


@callback(Output('accounts_receivable_value', 'children'),
              [Input('select_mun', 'value')],
              [Input('select_est', 'value')],
              )
def update_text(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        if not filter_mun.empty:  # Verifica que el DataFrame no esté vacío
            pob_tot = filter_mun['POBTOT'].values
            pob_fem = filter_mun['POBFEM'].values
            pob_mas = filter_mun['POBMAS'].values
        else:
            raise PreventUpdate
        if float(pob_fem[0]/pob_tot[0]) > 0.5:
            return [
                html.Img(src='/assets/mujeres.png',
                     style = {'height': '40px'},
                     className = 'title_image'
                     ),
                html.Div([
                    html.P('{0:,.0f}'.format(pob_fem[0]),
                           ),
                    html.Div([
                        html.Div([
                            html.P(f'{pob_fem[0] / pob_tot[0] * 100:.1f}% de pob total', className='indicator1'),
                            html.Div([
                                html.I(className = "fas fa-caret-up",
                                       style = {"font-size": "25px",
                                                'color': '#00B050'},
                                       ),
                            ], className = 'value_indicator'),
                        ], className = 'value_indicator_row'),
                    ], className = 'vs_p_m_column')
                ], className = 'indicator_column'),
            ]
        elif float(pob_fem[0]/pob_tot[0]) < 0.5:
            return [
                html.Img(src='/assets/mujeres.png',
                     style = {'height': '40px'},
                     className = 'title_image'
                     ),
                html.Div([
                    html.P('{0:,.0f}'.format(pob_fem[0]),
                           ),
                    html.Div([
                        html.Div([
                            html.P(f'{pob_fem[0] / pob_tot[0] * 100:.1f}% de pob total', className='indicator2'),
                            html.Div([
                                html.I(className = "fas fa-caret-down",
                                       style = {"font-size": "25px",
                                                'color': '#FF3399'},
                                       ),
                            ], className = 'value_indicator'),
                        ], className = 'value_indicator_row'),
                    ], className = 'vs_p_m_column')
                ], className = 'indicator_column'),
            ]
        elif pob_fem == 0:
            return [
                html.Div([
                    html.P('{0:,.3f}% de pob total'.format(pob_fem[0]),
                           ),
                    html.Div([
                        html.Div([
                            html.P('{0:,.1f}%'.format(pob_fem[0]/pob_tot[0]),
                                   className = 'indicator2'),
                        ], className = 'value_indicator_row'),
                    ], className = 'vs_p_m_column')
                ], className = 'indicator_column'),
            ]

@callback(Output('accounts_payable_value', 'children'),
            [Input('select_mun', 'value')],
              [Input('select_est', 'value')],
              )
def update_text(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        if not filter_mun.empty:  # Verifica que el DataFrame no esté vacío
            pobtot = filter_mun['POBTOT'].values
            pob65mas = filter_mun['POB65_MAS'].values #adultos mayores
        else:
            raise PreventUpdate
        if pob65mas > 0:
            return [
                 html.Img(src='/assets/adultos_mayores.png',
                     style = {'height': '40px'},
                     className = 'title_image'
                     ),
                html.Div([
                    html.P('{0:,.0f}'.format(pob65mas[0]),
                           ),
                    html.Div([
                        html.Div([
                            html.P(f'{pob65mas[0] / pobtot[0] * 100:.1f}% de pob total',className = "indicator3"),
                        ], className = 'value_indicator_row'),
                    ], className = 'vs_p_m_column')
                ], className = 'indicator_column'),
            ]
        
@callback(Output('income_value', 'children'),
              [Input('select_mun', 'value')],
              [Input('select_est', 'value')],
              )
def update_text(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        if not filter_mun.empty:  # Verifica que el DataFrame no esté vacío
            pob_tot = filter_mun['POBTOT'].values
            pob_fem = filter_mun['POBFEM'].values
            pob_mas = filter_mun['POBMAS'].values
        else:
            raise PreventUpdate
        if float(pob_mas[0]/pob_tot[0]) > 0.5:
            return [
                html.Img(src='/assets/hombre.png',
                     style = {'height': '40px'},
                     className = 'title_image'
                     ),
                html.Div([
                    
                    html.P('{0:,.0f}'.format(pob_mas[0]),
                           ),
                    html.Div([
                        html.Div([
                            html.P(f'{pob_mas[0] / pob_tot[0] * 100:.1f}% de pob total', className='indicator1'),
                            html.Div([
                                html.I(className = "fas fa-caret-up",
                                       style = {"font-size": "25px",
                                                'color': '#00B050'},
                                       ),
                            ], className = 'value_indicator'),
                        ], className = 'value_indicator_row'),
                    ], className = 'vs_p_m_column')
                ], className = 'indicator_column'),
            ]
        elif float(pob_mas[0]/pob_tot[0]) < 0.5:
            return [
                html.Img(src='/assets/hombre.png',
                     style = {'height': '40px'},
                     className = 'title_image'
                     ),
                html.Div([
                    html.P('{0:,.0f}'.format(pob_mas[0]),
                           ),
                    html.Div([
                        html.Div([
                           html.P(f'{pob_mas[0] / pob_tot[0] * 100:.1f}% de pob total', className='indicator2'),
                            html.Div([
                                html.I(className = "fas fa-caret-down",
                                       style = {"font-size": "25px",
                                                'color': '#FF3399'},
                                       ),
                            ], className = 'value_indicator'),
                        ], className = 'value_indicator_row'),
                    ], className = 'vs_p_m_column')
                ], className = 'indicator_column'),
            ]
        elif pob_mas == 0:
            return [
                html.Div([
                    html.P('${0:,.0f}'.format(pob_mas[0]),
                           ),
                    html.Div([
                        html.Div([
                            html.P('{0:,.1f}%'.format(pob_mas[0]),
                                   className = 'indicator2'),
                        ], className = 'value_indicator_row'),
                    ], className = 'vs_p_m_column')
                ], className = 'indicator_column'),
            ]


@callback(Output('primercirculo', 'children'),
              [Input('select_mun', 'value')],
              [Input('select_est', 'value')],
              )
def update_text(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        if not filter_mun.empty:  # Verifica que el DataFrame no esté vacío
            pobtot = int(filter_mun['POBTOT'].values[0])
            pobmas = int(filter_mun['POBMAS'].values[0])
            pobfem = int(filter_mun['POBFEM'].values[0])
            pobmas60 = int(filter_mun['P_60YMAS_M'].values[0])
            pobfem60 = int(filter_mun['P_60YMAS_F'].values[0])
            pobmas = pobmas - pobmas60
            pobfem = pobfem - pobfem60
            pob60 = pobmas60 + pobfem60
            return [
                html.Div([
                    html.Div([
                        html.P('Poblacion',
                               className = 'donut_chart_title'
                               ),
                        html.P('Masculina', className='titulo1'),
                        html.P('Femenina', className='titulo2'),
                        html.P('Adulta Mayor', className='titulo3'),
                    ], className = 'title_and_percentage'),
                    html.Div([
                        html.Div([
                            
                            html.Div([
                            ], className = 'value_indicator'),
                        ], className = 'value_indicator_row'),
                        html.P('tipos de poblacion',
                               className = 'vs_previous_month')
                    ], className = 'vs_p_m_column')
                ], className = 'inside_donut_chart_column'),
            ]

        else:
            raise PreventUpdate
       
           

@callback(Output('chart1', 'figure'),
              [Input('select_mun', 'value')],
              [Input('select_est', 'value')],
              )
def update_graph(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        pobmas = int(filter_mun['POBMAS'].values[0])
        pobfem = int(filter_mun['POBFEM'].values[0])
        pobmas60 = int(filter_mun['P_60YMAS_M'].values[0])
        pobfem60 = int(filter_mun['P_60YMAS_F'].values[0])
        pobmas = pobmas - pobmas60
        pobfem = pobfem - pobfem60
        pob60 = pobmas60 + pobfem60
        colors = ['#rgb(55, 0, 255)', '#f700ff',"163c1f"]

    return {
        'data': [go.Pie(labels = ['', '',''],
                        values = [pobmas, pobfem,pob60],
                        marker = dict(colors = colors,
                                      # line=dict(color='#DEB340', width=2)
                                      ),
                        hoverinfo = 'percent',  # Esto muestra etiqueta, porcentaje y valor en hover
                        textinfo = 'text',
                        hole = .7,
                        rotation = 90
                        )],

        'layout': go.Layout(
            plot_bgcolor = 'rgba(0,0,0,0)',
            paper_bgcolor = 'rgba(0,0,0,0)',
            margin = dict(t = 35, b = 0, r = 0, l = 0),
            showlegend = False,
            title = {'text': '',
                     'y': 0.95,
                     'x': 0.5,
                     'xanchor': 'center',
                     'yanchor': 'top'},
            titlefont = {'color': 'white',
                         'size': 15},
        ),

    }


@callback(Output('segundocirculo', 'children'),
            [Input('select_mun', 'value')],
            [Input('select_est', 'value')],
              )
def update_text(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        psinder = int(filter_mun['PSINDER'].values[0])
        pder_ss = int(filter_mun['PDER_SS'].values[0])
        pobtot = int(filter_mun['POBTOT'].values[0])
        colors = ["#f25872",'#400e28']
        if not filter_mun.empty:  # Verifica que el DataFrame no esté vacío
            return [
                html.Div([
                    html.Div([
                        html.P('Seguro Medico',
                               className = 'donut_chart_title'
                               ),
                        
                        html.P(f'{(pder_ss/pobtot) * 100:.1f}% con seguro', className='titulo11'),
                        html.P('medico', className='titulo11'),
                        html.P(f'{(psinder/pobtot) * 100:.1f}% sin seguro', className='titulo22'),
                        html.P('medico', className='titulo22')
                    ], className = 'title_and_percentage'),
                    html.Div([
                        html.Div([
                            
                            html.Div([
                            
                            ], className = 'value_indicator'),
                        ], className = 'value_indicator_row'),
                        html.P('               .',
                               className = 'vs_previous_month')
                    ], className = 'vs_p_m_column')
                ], className = 'inside_donut_chart_column'),
            ]
        else:
            raise PreventUpdate
@callback(Output('chart2', 'figure'),
            [Input('select_mun', 'value')],
            [Input('select_est', 'value')],
              )
def update_graph(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        psinder = int(filter_mun['PSINDER'].values[0])
        pder_ss = int(filter_mun['PDER_SS'].values[0])
        colors = ["#f25872",'#400e28']

    return {
        'data': [go.Pie(labels = ['', ''],
                        values = [psinder, pder_ss],
                        marker = dict(colors = colors,
                                      ),
                        hoverinfo = 'percent',
                        textinfo = 'text',
                        hole = .7,
                        rotation = 360
                        )],

        'layout': go.Layout(
            plot_bgcolor = 'rgba(0,0,0,0)',
            paper_bgcolor = 'rgba(0,0,0,0)',
            autosize = True,
            margin = dict(t = 35, b = 0, r = 0, l = 0),
            showlegend = False,
            title = {'text': '',
                     'y': 0.95,
                     'x': 0.5,
                     'xanchor': 'center',
                     'yanchor': 'top'},
            titlefont = {'color': 'white',
                         'size': 15},
        ),

    }


@callback(Output('instituciones', 'figure'),
              [Input('select_mun', 'value')],
              [Input('select_est', 'value')])
def update_text(select_mun, select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        issste_est = int(filter_mun["PDER_ISTEE"].values[0])
        issste = int(filter_mun["PDER_ISTE"].values[0])
        imss = int(filter_mun["PDER_IMSS"].values[0])
        pemsen = int(filter_mun["PAFIL_PDOM"].values[0])
        seguropopular = int(filter_mun["PDER_SEGP"].values[0])
        imssbienestar = int(filter_mun["PDER_IMSSB"].values[0])
        privada = int(filter_mun["PAFIL_IPRIV"].values[0])
        otra_inst = int(filter_mun["PAFIL_OTRAI"].values[0])
        pder_ss = int(filter_mun['PDER_SS'].values[0])

        porcentaje_issste_est = min(issste_est / pder_ss * 100, 100)
        porcentaje_issste = min(issste / pder_ss * 100, 100)
        porcentaje_imss = min(imss / pder_ss * 100, 100)
        porcentaje_pemsen = min(pemsen / pder_ss * 100, 100)
        porcentaje_seguropopular = min(seguropopular / pder_ss * 100, 100)
        porcentaje_imssbienestar = min(imssbienestar / pder_ss * 100, 100)
        porcentaje_privada = min(privada / pder_ss * 100, 100)
        porcentaje_otra_inst = min(otra_inst / pder_ss * 100, 100)

        data = [
            go.Bar(
                y=['Issste estatal', 'Issste', 'Imss', 'Pemex, Ejército',
                   'Seguro popular', 'Imss Bienestar', 'Institucion privada', 'Otra institucion'],
                x=[porcentaje_issste_est, porcentaje_issste, porcentaje_imss, porcentaje_pemsen,
                   porcentaje_seguropopular, porcentaje_imssbienestar,
                   porcentaje_privada, porcentaje_otra_inst],
                marker=dict(color='#000000'),
                orientation='h',
            )
        ]

        # Ordena las etiquetas y los valores de menor a mayor
        sorted_data = sorted(zip(data[0]['y'], data[0]['x']), key=lambda x: x[1], reverse=True)
        sorted_labels, sorted_values = zip(*sorted_data)
        return {
            'data': [
                go.Bar(
                    y=sorted_labels,
                    x=sorted_values,
                    text=[f'{val:.2f}%' for val in sorted_values],
                    marker=dict(color='#400e28'),
                    orientation='h',
                )
            ],
            'layout': go.Layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                autosize=True,
                margin=dict(t=10, b=0, r=0, l=120),
                showlegend=False,
                title={'text': '',
                       'y': 1,
                       'x': 0,
                       'xanchor': 'center',
                       'yanchor': 'top'},
                titlefont={'color': 'white',
                           'size': 15},
            ),
        }

@callback(Output('sinelectricidad', 'children'),
              [Input('select_mun', 'value')],
              [Input('select_est', 'value')])
def update_text(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        if not filter_mun.empty:  # Verifica que el DataFrame no esté vacío
            tvivpar = int(filter_mun['TVIVPAR'].values[0]) 
            sin_elec = int(filter_mun['VPH_S_ELEC'].values[0]) #adultos mayores
        else:
            raise PreventUpdate
        if sin_elec:
            return [
                 html.Img(src='/assets/sin-enchufe.png',
                     style = {'height': '60px'},
                     className = 'title_image'
                     ),
                html.Div([
                    html.P('{0:,.0f}'.format(sin_elec),
                           ),
                    html.Div([
                        html.Div([
                            html.P(f'{sin_elec / tvivpar * 100:.1f}% de viviendas',className = "indicator3"),
                        ], className = 'value_indicator_row'),
                        html.Div([
                            html.P('totales sin electricidad',className = "indicator32"),
                        ], className = 'value_indicator_row'),
                    ], className = 'vs_p_m_column')
                ], className = 'indicator_column'),
            ]


@callback(Output('current_ratio_value', 'children'),
            [Input('select_mun', 'value')],
            [Input('select_est', 'value')])
def update_text(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        if not filter_mun.empty:  # Verifica que el DataFrame no esté vacío
            tvivpar = int(filter_mun['TVIVPAR'].values[0]) 
            sin_agua = int(filter_mun['VPH_AGUAFV'].values[0])  #adultos mayores
        else:
            raise PreventUpdate
        if sin_agua:
            return [
                 html.Img(src='/assets/no-hay-agua.png',
                     style = {'height': '60px'},
                     className = 'title_image'
                     ),
                html.Div([
                    html.P('{0:,.0f}'.format(sin_agua),
                           ),
                    html.Div([
                        html.Div([
                            html.P(f'{sin_agua / tvivpar * 100:.1f}% de viviendas',className = "indicator3"),
                        ], className = 'value_indicator_row'),
                        html.Div([
                            html.P('totales sin agua',className = "indicator32"),
                        ], className = 'value_indicator_row'),
                    ], className = 'vs_p_m_column')
                ], className = 'indicator_column'),
            ]



@callback(Output('net_profit_value', 'children'),
            [Input('select_mun', 'value')],
            [Input('select_est', 'value')])
def update_text(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        if not filter_mun.empty:  # Verifica que el DataFrame no esté vacío
            tvivpar = int(filter_mun['TVIVPAR'].values[0])
            sin_dren =  int(filter_mun['VPH_NODREN'].values[0]) #adultos mayores
        else:
            raise PreventUpdate
        if sin_dren:
            return [
                 html.Img(src='/assets/sin-contaminacion.png',
                     style = {'height': '60px'},
                     className = 'title_image'
                     ),
                html.Div([
                    html.P('{0:,.0f}'.format(sin_dren),
                           ),
                    html.Div([
                        html.Div([
                            html.P(f'{sin_dren / tvivpar * 100:.1f}% de viviendas',className = "indicator3")
                            ], className = 'value_indicator_row'),
                            html.Div([
                            html.P('totales sin drenaje',className = "indicator32"),
                            ], className = 'value_indicator_row'),
                    ], className = 'vs_p_m_column')
                ], className = 'indicator_column'),
            ]


@callback(Output('cash_at_eom_value', 'children'),
            [Input('select_mun', 'value')],
            [Input('select_est', 'value')])
def update_text(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        if not filter_mun.empty:  # Verifica que el DataFrame no esté vacío
            tvivpar = int(filter_mun['TVIVPAR'].values[0])
            sin_tic = int(filter_mun['VPH_SINTIC'].values[0]) #adultos mayores
        else:
            raise PreventUpdate
        if sin_tic:
            return [
                 html.Img(src='/assets/sin-telefono.png',
                     style = {'margin-left':'10px','height': '60px'},
                     className = 'title_image'
                     ),
                html.Div([
                    html.P('{0:,.0f}'.format(sin_tic),
                           ),
                    html.Div([
                        html.Div([
                            html.P(f'{sin_tic / tvivpar * 100:.1f}% de viviendas',className = "indicator3"),
                        ], className = 'value_indicator_row'),
                        html.Div([
                            html.P('sin tecnologias de la comunicacion',className = "indicator32"),
                        ], className = 'value_indicator_row'),
                    ], className = 'vs_p_m_column')
                ], className = 'indicator_column'),
            ]



@callback(Output('third_left_circle', 'children'),
            [Input('select_mun', 'value')],
            [Input('select_est', 'value')])
def update_text(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        if not filter_mun.empty:  # Verifica que el DataFrame no esté vacío
            return [
                html.Div([
                    html.Div([
                        html.P('Vulnerabilidades',
                               className = 'donut_chart_title5'
                               ),
                    ], className = 'title_and_percentage'),
                    html.Div([
                        html.Div([
                            html.Div([
                            html.P('Indicadores', className='titulo1chart3'),
                             ], className = 'value_indicator_row'),
                        ], className = 'value_indicator_row'),
                        html.Div([
                            html.Div([
                            html.P('de viviendas', className='titulo1chart3'),
                             ], className = 'value_indicator_row'),
                        ], className = 'value_indicator_row'),
                         html.Div([
                            html.Div([
                            html.P('vulnerables', className='titulo1chart3'),
                             ], className = 'value_indicator_row'),
                        ], className = 'value_indicator_row'),
                    ], className = '    vs_p_m_column')
                ], className = 'inside_donut_chart_column'),
            ]



@callback(Output('chart3', 'figure'),
            [Input('select_mun', 'value')],
            [Input('select_est', 'value')])
def update_graph(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        if not filter_mun.empty:  # Verifica que el DataFrame no esté vacío
            tvivpar = int(filter_mun['TVIVPAR'].values[0])
            sin_tic = int(filter_mun['VPH_SINTIC'].values[0]) #sin tics
            sin_comp = int(filter_mun['VPH_SINCINT'].values[0]) #sin computadora
            sin_tel = int(filter_mun['VPH_SINLTC'].values[0]) #sin telefonia
            sin_rtv = int(filter_mun['VPH_SINRTV'].values[0]) #sin radio ni television
            sin_agua = int(filter_mun['VPH_AGUAFV'].values[0]) #sin agua entubada
            sin_dren = int(filter_mun['VPH_NODREN'].values[0]) #sin drenaje
            sin_tras_priv = int(filter_mun['VPH_NDACMM'].values[0]) #sin drenaje
            
              
            sin_tic = min(sin_tic / tvivpar * 100, 100)
            sin_comp = min(sin_comp / tvivpar * 100, 100)
            sin_tel = min(sin_tel / tvivpar * 100, 100)
            sin_rtv = min(sin_rtv / tvivpar * 100, 100)
            sin_agua = min(sin_agua / tvivpar * 100, 100)
            sin_dren = min(sin_dren / tvivpar * 100, 100)
            sin_tras_priv = min(sin_tras_priv / tvivpar * 100, 100)
                
            
            colors = ['#D35940', '#82FFFF','#e4e2af',"#ffa590","#e5cbb4","#56413e","#0e002f"]

            return {
                'data': [go.Pie(
                        labels=['Sin tecnologias para comunicacion', 'Sin computadora','Sin telefono','Sin radio y/o television',
                                'Sin acceso a agua entubada','Sin drenaje', 'Sin transporte privado'],
                        values=[sin_tic, sin_comp, sin_tel, sin_rtv, sin_agua, sin_dren, sin_tras_priv],
                        marker=dict(colors=colors),
                        hoverinfo='label',  # Muestra el label y el porcentaje en el hover
                        hole=0.7,
                        rotation=90
                    )],

                'layout': go.Layout(
                    plot_bgcolor = 'rgba(0,0,0,0)',
                    paper_bgcolor = 'rgba(0,0,0,0)',
                    margin = dict(t = 35, b = 0, r = 0, l = 0),
                    showlegend = False,
                    title = {'text': '',
                            'y': 0.95,
                            'x': 0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'},
                    titlefont = {'color': 'white',
                                'size': 15},
                ),

            }


@callback(Output('fourth_right_circle', 'children'),
            [Input('select_mun', 'value')],
            [Input('select_est', 'value')])
def update_text(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        if not filter_mun.empty:  # Verifica que el DataFrame no esté vacío
            tvivpar = int(filter_mun['TVIVPAR'].values[0])
            sin_tic = int(filter_mun['VPH_SINTIC'].values[0]) #sin tics
            sin_comp = int(filter_mun['VPH_SINCINT'].values[0]) #sin computadora
            sin_tel = int(filter_mun['VPH_SINLTC'].values[0]) #sin telefonia
            sin_rtv = int(filter_mun['VPH_SINRTV'].values[0]) #sin radio ni television
            sin_agua = int(filter_mun['VPH_AGUAFV'].values[0]) #sin agua entubada
            sin_dren = int(filter_mun['VPH_NODREN'].values[0]) #sin drenaje
            sin_tras_priv = int(filter_mun['VPH_NDACMM'].values[0]) #sin drenaje
          
            return [
                html.Div([
                    html.Div([
                        html.P('Viviendas', className='titulo1chart4'),
                    ], className = 'title_and_percentage2'),
                    html.Div([
                        html.Div([
                            html.Div([
                            html.P('sin', className='titulo1chart3'),
                             ], className = 'value_indicator_row'),
                        ], className = 'title_and_percentage2'),
                        html.Div([
                            html.Div([
                            html.P('internet', className='titulo1chart3'),
                             ], className = 'value_indicator_row'),
                        ], className = 'title_and_percentage2'),
                    ], className = '    vs_p_m_column')
                ], className = 'inside_donut_chart_column2'),
            ]


@callback(Output('chart4', 'figure'),
            [Input('select_mun', 'value')],
            [Input('select_est', 'value')])
def update_graph(select_mun,select_est):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filter_mun = inegi[(inegi['NOM_MUN'] == select_mun) & (inegi['NOM_ENT'] == select_est)]
        if not filter_mun.empty:  # Verifica que el DataFrame no esté vacío
            tvivpar = int(filter_mun['TVIVPAR'].values[0])
            con_inter = int(filter_mun['VPH_INTER'].values[0]) #con internet
            
              
            con_inter = min(con_inter / tvivpar * 100, 100)
            sin_inter = 100 - con_inter
                
            
            colors = ['#411f2d', '#ac4147']

            return {
                'data': [go.Pie(
                        labels=['Con internet', 'Sin internet'],
                        values=[con_inter, sin_inter],
                        marker=dict(colors=colors),
                        hoverinfo='label',  # Muestra el label y el porcentaje en el hover
                        hole=0.7,
                        rotation=90
                    )],

                'layout': go.Layout(
                    plot_bgcolor = 'rgba(0,0,0,0)',
                    paper_bgcolor = 'rgba(0,0,0,0)',
                    margin = dict(t = 35, b = 0, r = 0, l = 0),
                    showlegend = False,
                    title = {'text': '',
                            'y': 0.95,
                            'x': 0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'},
                    titlefont = {'color': 'white',
                                'size': 15},
                ),

            }
@callback(Output('bar_chart', 'figure'),
            [Input('select_mun', 'value')],
            [Input('select_est', 'value')],
            [Input('select_year', 'value')])
def update_graph(select_mun, select_est, select_year):
    if select_mun is None:
        raise PreventUpdate
    if select_est is None:
        raise PreventUpdate
    else:
        filtro_ano = seguridad[(seguridad["Entidad"] == select_est) & (seguridad["Municipio"] == select_mun) & (seguridad["Año"] == select_year)]
        df_sorted = filtro_ano.sort_values(by='Total_delitos', ascending=False)
        df_sorted = df_sorted.head(10)
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

        return {
    'data': [go.Bar(
        x=df_sorted['Tipo de delito'],
        y=df_sorted['Total_delitos'],
        marker=dict(color=df_sorted['Total_delitos']),
        width=0.8,  # Ancho de las barras ajustado
        orientation='v',
        hoverinfo='text',
        hovertext='' + df_sorted['Tipo de delito'].astype(str) + '<br>' +
                    '' + [f'{x:,.0f}' for x in df_sorted['Total_delitos']] + '<br>'
        )],

    'layout': go.Layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title={'text': 'Incidentes delictivos por municipio',
               'y': 0.97,
               'x': 0.5,
               'xanchor': 'center',
               'yanchor': 'top'},
        titlefont={'color': '#404040',
                   'size': 16,
                   'family': 'Calibri', },
        margin=dict(r=20, t=20, b=20, l=70),
        xaxis=dict(title='<b></b>',
                   visible=True,
                   color='white',
                   showline=False,
                   showgrid=False,
                   showticklabels=False,
                   linecolor='white',
                   linewidth=0,
                   ticks='outside',
                   tickfont=dict(
                       family='Arial',
                       size=12,
                       color='white')
                   ),

        yaxis=dict(title='<b></b>',
                   tickprefix='',
                   tickformat=',.0f',
                   visible=True,
                   color='white',
                   showline=False,
                   showgrid=False,
                   showticklabels=True,
                   linecolor='white',
                   linewidth=1,
                   ticks='outside',
                   tickfont=dict(
                       family='Calibri',
                       size=15,
                       color='#404040')
                   ),
    )
}