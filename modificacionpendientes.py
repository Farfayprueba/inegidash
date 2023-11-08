import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import pandas as pd
import numpy as np
import pathlib
import dash_auth
from flask import request
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("./data").resolve()
users = [
    ['hello', 'world'],['hello1', 'world'],['hello1', 'world']
]
data = pd.read_csv(DATA_PATH.joinpath('financial_data.csv'))

data['pct_accounts_receivable'] = (data['accounts receivable'].pct_change()) * 100
data['pct_accounts_receivable'] = data['pct_accounts_receivable'].fillna(0)

data['pct_accounts_payable'] = (data['accounts payable'].pct_change()) * 100
data['pct_accounts_payable'] = data['pct_accounts_payable'].fillna(0)

data['pct_income'] = (data['income'].pct_change()) * 100
data['pct_income'] = data['pct_income'].fillna(0)

data['expenses'] = data['cost of goods sold'] + data['total operating expenses']
data['pct_expenses'] = (data['expenses'].pct_change()) * 100
data['pct_expenses'] = data['pct_expenses'].fillna(0)

data['gross profit'] = data['income'] - data['cost of goods sold']
data['pct_gross_profit'] = (data['gross profit'].pct_change()) * 100
data['pct_gross_profit'] = data['pct_gross_profit'].fillna(0)

data['pct_total_operating_expenses'] = (data['total operating expenses'].pct_change()) * 100
data['pct_total_operating_expenses'] = data['pct_total_operating_expenses'].fillna(0)

data['operating profit (EBIT)'] = data['gross profit'] - data['total operating expenses']
data['pct_operating_profit_(EBIT)'] = (data['operating profit (EBIT)'].pct_change()) * 100
data['pct_operating_profit_(EBIT)'] = data['pct_operating_profit_(EBIT)'].fillna(0)

data['pct_taxes'] = (data['Taxes'].pct_change()) * 100
data['pct_taxes'] = data['pct_taxes'].fillna(0)

data['pct_quick_ratio'] = (data['quick ratio'].pct_change()) * 100
data['pct_quick_ratio'] = data['pct_quick_ratio'].fillna(0)

data['pct_current_ratio'] = (data['current ratio'].pct_change()) * 100
data['pct_current_ratio'] = data['pct_current_ratio'].fillna(0)

data['pct_cash_at_eom'] = (data['cash at eom'].pct_change()) * 100
data['pct_cash_at_eom'] = data['pct_cash_at_eom'].fillna(0)

data['net profit'] = data['operating profit (EBIT)'] - data['Taxes']
data['pct_net_profit'] = (data['net profit'].pct_change()) * 100
data['pct_net_profit'] = data['pct_net_profit'].fillna(0)

data['net profit margin %'] = (data['net profit'] / data['income']) * 100
data['pct_net_profit_margin_%'] = (data['net profit margin %'].pct_change()) * 100
data['pct_net_profit_margin_%'] = data['pct_net_profit_margin_%'].fillna(0)

data['income budget %'] = (data['income'] / data['income budget']) * 100
data['pct_income_budget_%'] = (data['income budget %'].pct_change()) * 100
data['pct_income_budget_%'] = data['pct_income_budget_%'].fillna(0)

data['expense budget %'] = (data['expenses'] / data['expense budget']) * 100
data['pct_expense_budget_%'] = (data['expense budget %'].pct_change()) * 100
data['pct_expense_budget_%'] = data['pct_expense_budget_%'].fillna(0)

data['pct_cost_of_goods_sold'] = (data['cost of goods sold'].pct_change()) * 100
data['pct_cost_of_goods_sold'] = data['pct_cost_of_goods_sold'].fillna(0)


font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]
inegi = pd.read_csv('inegi.csv')
inegi.replace("*", 0, inplace=True)
inegi = inegi.apply(pd.to_numeric, errors='ignore')
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

auth = dash_auth.BasicAuth(
    app,
    users
    
)
def get_username():
    return request.authorization['username'] if request.authorization else None

@app.callback(
    [Output('select_est', 'options'),
     Output('select_est', 'value')],
    Input('select_est', 'value')
)
def update_dropdown_options(selected_value):
    username = get_username()
    if username == "hello":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Yucatán"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    if username == "hello1":
        opciones_filtradas = [{'label': c, 'value': c} for c in inegi.loc[inegi['NOM_ENT'].str.contains("Quintana"), 'NOM_ENT'].unique()]
        value = opciones_filtradas[0]["value"]
        return opciones_filtradas,value
    else:
        return [], None


app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src = app.get_asset_url('statistics.png'),
                     style = {'height': '30px'},
                     className = 'title_image'
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
            dcc.Dropdown(id = 'select_month',
                         multi = False,
                         clearable = True,
                         disabled = False,
                         style = {'display': True},
                         value = 'Mar',
                         placeholder = 'Seleccionar municipio',
                         options = [{'label': c, 'value': c}
                                    for c in data['months'].unique()],
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
                html.Div([
                    
                ], className = 'income_statement_column1'),
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
                          className = 'bar_chart_size'),
            ], className = 'net_profit2'),
        ], className = 'income_statement_row')
    ], className = 'f_row'),

    html.Div([
        dcc.Graph(id = 'line_chart',
                  config = {'displayModeBar': False},
                  className = 'line_chart_size'),
        dcc.Graph(id = 'combination_chart',
                  config = {'displayModeBar': False},
                  className = 'combination_chart_size'),
    ], className = 'last_row')
])

############################3


#############################
@app.callback(
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


@app.callback(Output('poblacion_total', 'children'),
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
                    html.Img(src = app.get_asset_url('organizacion.png'),
                     style = {'height': '40px'},
                     className = 'title_image'
                     ),
                ], className = 'indicator_column'),
            ]

@app.callback(Output('discapacitada', 'children'),
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
                    html.Img(src = app.get_asset_url('discapacidad.png'),
                     style = {'height': '45px'},
                     className = 'title_image'
                     ),
                ], className = 'indicator_column'),
            ]

@app.callback(Output('mentalillness', 'children'),
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
                    html.Img(src = app.get_asset_url('frasco-de-pastillas.png'),
                     style = {'height': '45px'},
                     className = 'title_image'
                     ),
                ], className = 'indicator_column'),
            ]

@app.callback(Output('discapacidad_motora', 'children'),
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
                    html.Img(src = app.get_asset_url('discapacidad_motora.png'),
                     style = {'height': '45px'},
                     className = 'title_image'
                     ),
                ], className = 'indicator_column'),
            ]
            
@app.callback(Output('discapacidad_visual', 'children'),
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
                    html.Img(src = app.get_asset_url('discapacidad-visual.png'),
                     style = {'height': '45px'},
                     className = 'title_image'
                     ),
                ], className = 'indicator_column'),
            ]
        else:
            raise PreventUpdate
        
            
@app.callback(Output('discapacidad_auditiva', 'children'),
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
                    html.Img(src = app.get_asset_url('la-discapacidad-auditiva.png'),
                     style = {'height': '45px'},
                     className = 'title_image'
                     ),
                ], className = 'indicator_column'),
            ]
        else:
            raise PreventUpdate
        
############################


@app.callback(Output('accounts_receivable_value', 'children'),
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
                html.Img(src = app.get_asset_url('mujeres.png'),
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
                html.Img(src = app.get_asset_url('mujeres.png'),
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

@app.callback(Output('accounts_payable_value', 'children'),
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
                 html.Img(src = app.get_asset_url('adultos_mayores.png'),
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
        
@app.callback(Output('income_value', 'children'),
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
                html.Img(src = app.get_asset_url('hombre.png'),
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
                html.Img(src = app.get_asset_url('hombre.png'),
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


@app.callback(Output('primercirculo', 'children'),
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
       
           

@app.callback(Output('chart1', 'figure'),
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


@app.callback(Output('segundocirculo', 'children'),
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
@app.callback(Output('chart2', 'figure'),
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


@app.callback(Output('instituciones', 'figure'),
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

@app.callback(Output('sinelectricidad', 'children'),
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
                 html.Img(src = app.get_asset_url('sin-enchufe.png'),
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


@app.callback(Output('current_ratio_value', 'children'),
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
                 html.Img(src = app.get_asset_url('no-hay-agua.png'),
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



@app.callback(Output('net_profit_value', 'children'),
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
                 html.Img(src = app.get_asset_url('sin-contaminacion.png'),
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


@app.callback(Output('cash_at_eom_value', 'children'),
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
                 html.Img(src = app.get_asset_url('sin-telefono.png'),
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



@app.callback(Output('third_left_circle', 'children'),
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



@app.callback(Output('chart3', 'figure'),
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


@app.callback(Output('fourth_right_circle', 'children'),
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


@app.callback(Output('chart4', 'figure'),
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



@app.callback(Output('bar_chart', 'figure'),
              [Input('select_month', 'value')])
def update_graph(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        filter_month = data[data['months'] == select_month]
        income = filter_month['income'].iloc[0]
        cost_of_goods_sold = filter_month['cost of goods sold'].iloc[0]
        gross_profit = filter_month['gross profit'].iloc[0]
        total_operating_expenses = filter_month['total operating expenses'].iloc[0]
        operating_profit_EBIT = filter_month['operating profit (EBIT)'].iloc[0]
        taxes = filter_month['Taxes'].iloc[0]
        net_profit = filter_month['net profit'].iloc[0]
        object_data = [['income', income], ['cost of goods sold', cost_of_goods_sold],
                       ['gross profit', gross_profit], ['total operating expenses', total_operating_expenses],
                       ['operating profit ebit', operating_profit_EBIT], ['taxes', taxes],
                       ['net profit', net_profit]]
        df = pd.DataFrame(object_data, columns = ['Text', 'Value'])
        bar_color = np.where(df['Value'] > 0, '#B258D3', '#FF3399')
        # bar_color1 = np.where(df['Value'] > 0, '#B258D3', '#FF3399')

        return {
            'data': [go.Bar(x = df['Text'],
                            y = df['Value'],
                            marker = dict(color = bar_color),
                            width = 0.5,
                            orientation = 'v',
                            hoverinfo = 'text',
                            hovertext =
                            '' + df['Text'].astype(str) + '<br>' +
                            '$' + [f'{x:,.0f}' for x in df['Value']] + '<br>'
                            )],

            'layout': go.Layout(
                plot_bgcolor = 'rgba(0,0,0,0)',
                paper_bgcolor = 'rgba(0,0,0,0)',
                title = {'text': 'Income Statement',
                         'y': 0.97,
                         'x': 0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'},
                titlefont = {'color': '#404040',
                             'size': 16,
                             'family': 'Calibri', },
                margin = dict(r = 20, t = 20, b = 20, l = 70),
                xaxis = dict(title = '<b></b>',
                             visible = True,
                             color = 'white',
                             showline = False,
                             showgrid = False,
                             showticklabels = False,
                             linecolor = 'white',
                             linewidth = 0,
                             ticks = 'outside',
                             tickfont = dict(
                                 family = 'Arial',
                                 size = 12,
                                 color = 'white')
                             ),

                yaxis = dict(title = '<b></b>',
                             tickprefix = '$',
                             tickformat = ',.0f',
                             visible = True,
                             color = 'white',
                             showline = False,
                             showgrid = False,
                             showticklabels = True,
                             linecolor = 'white',
                             linewidth = 1,
                             ticks = 'outside',
                             tickfont = dict(
                                 family = 'Calibri',
                                 size = 15,
                                 color = '#404040')
                             ),
            )
        }


@app.callback(Output('line_chart', 'figure'),
              [Input('select_month', 'value')])
def update_graph(select_month):
    net_profit = data['net profit']
    months = data['months']
    text_color = np.where(net_profit > 0, 'black', '#FF3399')

    return {
        'data': [
            go.Scatter(
                x = months,
                y = net_profit,
                text = net_profit,
                texttemplate = '$' + '%{text:,.0f}',
                textposition = 'top center',
                textfont = dict(
                    family = "Calibri",
                    size = 14,
                    color = text_color,
                ),
                mode = 'markers+lines+text',
                line = dict(shape = "spline", smoothing = 1.3, width = 3, color = '#B258D3'),
                marker = dict(size = 10, symbol = 'circle', color = '#FFFFFF',
                              line = dict(color = '#00B0F0', width = 2)
                              ),

                hoverinfo = 'text',
                hovertext =
                '<b>Month</b>: ' + months.astype(str) + '<br>' +
                '<b>Net Profit</b>: $' + [f'{x:,.0f}' for x in net_profit] + '<br>'
            )],

        'layout': go.Layout(
            plot_bgcolor = 'rgba(0,0,0,0)',
            paper_bgcolor = 'rgba(0,0,0,0)',
            title = {'text': 'Net Profit',
                     'y': 0.97,
                     'x': 0.5,
                     'xanchor': 'center',
                     'yanchor': 'top'},
            titlefont = {'color': '#404040',
                         'size': 16,
                         'family': 'Calibri', },
            margin = dict(r = 20, t = 20, b = 30, l = 70),
            xaxis = dict(title = '<b></b>',
                         visible = True,
                         color = 'white',
                         showline = False,
                         showgrid = False,
                         showticklabels = True,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = '#404040')
                         ),

            yaxis = dict(title = '<b></b>',
                         tickprefix = '$',
                         tickformat = ',.0f',
                         visible = True,
                         color = 'white',
                         showline = False,
                         showgrid = False,
                         showticklabels = True,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Calibri',
                             size = 15,
                             color = '#404040')
                         ),
        )
    }


@app.callback(Output('combination_chart', 'figure'),
              [Input('select_month', 'value')])
def update_graph(select_month):
    income = data['income']
    expenses = data['expenses']
    months = data['months']

    return {
        'data': [
            go.Scatter(
                x = months,
                y = income,
                mode = 'lines',
                line = dict(shape = "spline", smoothing = 1.3, width = 3, color = '#D35940'),
                hoverinfo = 'text',
                hovertext =
                '<b>Month</b>: ' + months.astype(str) + '<br>' +
                '<b>Income</b>: $' + [f'{x:,.0f}' for x in income] + '<br>'
            ),
            go.Bar(
                x = months,
                y = expenses,
                marker = dict(color = '#63A0CC'),
                width = 0.5,
                hoverinfo = 'text',
                hovertext =
                '<b>Month</b>: ' + months.astype(str) + '<br>' +
                '<b>Expenses</b>: $' + [f'{x:,.0f}' for x in expenses] + '<br>'
            )
        ],

        'layout': go.Layout(
            showlegend = False,
            plot_bgcolor = 'rgba(0,0,0,0)',
            paper_bgcolor = 'rgba(0,0,0,0)',
            title = {'text': 'Income and Expenses',
                     'y': 0.97,
                     'x': 0.5,
                     'xanchor': 'center',
                     'yanchor': 'top'},
            titlefont = {'color': '#404040',
                         'size': 16,
                         'family': 'Calibri', },
            margin = dict(r = 20, t = 20, b = 30, l = 70),
            xaxis = dict(title = '<b></b>',
                         visible = True,
                         color = 'white',
                         showline = False,
                         showgrid = False,
                         showticklabels = True,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = '#404040')
                         ),

            yaxis = dict(title = '<b></b>',
                         tickprefix = '$',
                         tickformat = ',.0f',
                         visible = True,
                         color = 'white',
                         showline = False,
                         showgrid = False,
                         showticklabels = True,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Calibri',
                             size = 15,
                             color = '#404040')
                         ),
        )
    }


if __name__ == "__main__":
    app.run_server(debug = True)
