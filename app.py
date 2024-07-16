# https://dash.plotly.com/layout
# https://digitrain.ru/articles/272309/
# https://nuffing.coutinho.net/2020/12/python-dash-how-to-build-a-beautiful-dashboard-in-3-steps/

# !!!!!!
# https://question-it.com/questions/6597478/dash-datepickerrange-s-grafikom

# template in ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]:
# https://github.com/plotly/plotly.py/blob/master/doc/python/bar-charts.md

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import dash_split_pane
import plotly.graph_objects as go
from datetime import date
import datetime

# import numpy as np
# import dash_daq as daq
# from numpy import radians, cos, sin

app = Dash(__name__)

# app.config.suppress_callback_exceptions = True
df = pd.read_csv('db/Статистика.csv', delimiter=';')

app.layout = html.Div(
    children=[

        html.Div(children=[

            html.H1('Настройка параметров', style={"margin": "10px",
                                                   "color": "white",
                                                   'font-family': "system-ui",
                                                   'font-weight': 'normal'}),
            html.Br(),
            html.H2('Идентификатор оборудования', style={"margin": "10px",
                                                   "color": "#00edca",
                                                   'font-family': "system-ui",
                                                   'font-weight': 'normal'}),
            dcc.Dropdown(id='dropdown1',
                         options=[{'label': x, 'value': x} for x in
                                  range(df['id_stanok'].min(), df['id_stanok'].max() + 1)],
                         value=df['id_stanok'][0],
                         style={
                             "margin": "10px",
                             "font-size": "20px",
                             "width": "70%"
                             # "border-color": "#4c5866",
                         }),
            html.Br(),
            html.Br(),
            html.Br(),

            html.H2('Анализируемый период', style={"margin": "10px",
                                                   "color": "#00edca",
                                                   'font-family': "system-ui",
                                                   'font-weight': 'normal'}),

            html.Div([
                html.Label('Min:    ',
                           style={"margin": "6px", "color": "red", "font-size": "20px",
                                  "font-weight": "bold",
                                  'font-family': "system-ui"}),

                dcc.DatePickerSingle(
                    id=('date_picker1'),
                    date=date(2022, 12, 1),
                    display_format='DD.M.Y',
                    style={"margin": "10px", 'font-family': "system-ui"}),
            ]),
            html.Br(),
            html.Div([
                html.Label('Max:',
                           style={"margin": "12px", "color": "#00edca", "font-size": "20px",
                                  "font-weight": "bold",
                                  'font-family': "system-ui"}),
                dcc.DatePickerSingle(
                    id=('date_picker2'),
                    date=date(2022, 12, 3),
                    display_format='DD.M.Y',
                    style={'font-family': "system-ui"}),
            ]),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H2('Исследуемый интервал потребляемой мощности, кВТ', style={"margin": "10px",
                                                                              "color": "#00edca",
                                                                              'font-family': "system-ui",
                                                                              'font-weight': 'normal'}),
            html.Div([
                html.Label('Min:',
                           style={"margin": "10px", "color": "red", "font-size": "20px",
                                  "font-weight": "bold",
                                  'font-family': "system-ui"}),

                dcc.Input(id='min', value=0, type="number",
                          style={
                              "height": "30px",
                              "margin": "14px",
                              "font-size": "20px",
                              "border-color": "white",
                              "border-radius": "3px",
                              "width": "32%",
                              'color': '#444444',
                          })
            ]),
            html.Div([
                html.Label('Max:',
                           style={"margin": "10px", "color": "#00edca", "font-size": "20px",
                                  "font-weight": "bold",
                                  'font-family': "system-ui"}),

                dcc.Input(id='max', value=3, type="number",
                          style={
                              "height": "30px",
                              "margin": "10px",
                              "font-size": "20px",
                              "border-color": "white",
                              "border-radius": "3px",
                              "width": "32%",
                              'color': '#444444',
                          })
            ]),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
        ], style={'background-color': '#004149', 'height': '100%', 'width': '20%'}),

        html.Div(children=[

            dcc.Tabs(
                id="tabs-with-classes",
                value='tab-1',
                parent_className='custom-tabs',
                className='custom-tabs-container',
                children=[
                    dcc.Tab(
                        label='Анализ загрузки оборудования в разрезе потребляемой мощности',
                        value='tab-1',
                        className='custom-tab',
                        selected_className='custom-tab--selected'
                    ),
                    dcc.Tab(
                        label='Анализ загрузки оборудования в разрезе технологических цепочек',
                        value='tab-2',
                        className='custom-tab',
                        selected_className='custom-tab--selected'
                    ),

                ]),
            html.Div(id='tabs-content-classes', style={'width': '100%'})
        ], style={'height': '100%', 'width': '80%'})
    ], style={'display': 'flex'}
    # style={'display': 'inline-block'}
    # split="vertical",
    # size=400,

)


@app.callback(Output('tabs-content-classes', 'children'),
              Input('tabs-with-classes', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.Div([
                dcc.Graph(id='graph1', config={'displaylogo': False}, className="w60"),
                dcc.Graph(id='graph3', config={'displaylogo': False}, className="w20"),
                dcc.Graph(id='graph4', config={'displaylogo': False}, className="w20"),
            ], style={'display': 'flex',
                      'flex-direction': 'row',
                      'justify-content': 'center',
                      }),

            html.Div([
                dcc.Graph(id='graph2', config={'displaylogo': False}, className="w30"),
                dcc.Graph(id='graph21', config={'displaylogo': False}, className="w30"),
                dcc.Graph(id='graph22', config={'displaylogo': False}, className="w30"),
            ], style={'display': 'flex',
                      'flex-direction': 'row',
                      'justify-content': 'center',
                      }),

            # html.Div([
            #     dcc.Graph(id='graph3', config={'displaylogo': False}),
            #     dcc.Graph(id='graph4', config={'displaylogo': False}),
            # ], style={'display': 'flex',
            #           'flex-direction': 'row',
            #           'justify-content': 'center'})

        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Система показателей в разработке')], style={'text-align': 'center'})


@app.callback(Output('graph1', 'figure'),
              Output('graph2', 'figure'),
              Output('graph21', 'figure'),
              Output('graph22', 'figure'),
              Output('graph3', 'figure'),
              Output('graph4', 'figure'),
              Input('dropdown1', 'value'),
              Input('min', 'value'),
              Input('max', 'value'),
              Input('date_picker1', 'date'),
              Input('date_picker2', 'date'),
              )
def update_output_div(dropdown1, min, max, date_picker1, date_picker2):
    df['dateDay'] = pd.to_datetime(df['date']).dt.date

    start_date = datetime.datetime.strptime(date_picker1, '%Y-%d-%m').date()
    end_date = datetime.datetime.strptime(date_picker2, '%Y-%d-%m').date()

    query_filter_stanok = df[
        (df['id_stanok'] == dropdown1) & (df['dateDay'] >= start_date) & (df['dateDay'] <= end_date)]

    query_filter_power = len(df[(df['id_stanok'] == dropdown1) & (df['value'] >= min) & (df['value'] <= max) & (
            df['dateDay'] >= start_date) & (df['dateDay'] <= end_date) & (df['dateDay'] >= start_date) & (
                                        df['dateDay'] <= end_date)]) / 12
    query_filter_prostoi = len(df[(df['id_stanok'] == dropdown1) & (df['value'] <= 0) & (
            df['dateDay'] >= start_date) & (df['dateDay'] <= end_date)]) / 12
    query_filter_any_power = len(df[(df['id_stanok'] == dropdown1) & (df['value'] > 0) & (
            df['dateDay'] >= start_date) & (df['dateDay'] <= end_date)]) / 12
    count_element = len(
        df[(df['id_stanok'] == dropdown1) & (df['dateDay'] >= start_date) & (df['dateDay'] <= end_date)]) / 12
    query_filter_max_power = \
    df[(df['id_stanok'] == dropdown1) & (df['dateDay'] >= start_date) & (df['dateDay'] <= end_date)]['value'].max()
    query_filter_mean_power = \
    df[(df['id_stanok'] == dropdown1) & (df['dateDay'] >= start_date) & (df['dateDay'] <= end_date)]['value'].mean()

    fig1 = px.bar(query_filter_stanok, x="date", y="value",
                  title=f'Потрябляемая мощность оборудования ID: {str(dropdown1)} ',
                  template="plotly_white")
    fig1.update_traces(marker_color='#025669')
    fig1.update_xaxes(title_text='Время')
    fig1.update_yaxes(title_text='Мощность, Ватт')

    fig2 = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        delta={'reference': count_element},
        value=query_filter_prostoi,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [None, count_element], 'tickwidth': 1, 'tickcolor': "gray"},
            'bar': {'color': "red"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            # 'steps': [
            #     {'range': [0, max//3], 'color': 'red'},
            #     {'range': [max//3, (max//3)*2], 'color': 'yellow'},
            #     {'range': [(max//3)*2, max], 'color': 'green'}],
        },
        title={"text": "Суммарное t простоя оборудования <br><span style='font-size:0.8em;color:gray'>мин</span><br> "}))

    fig21 = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        delta={'reference': count_element},
        value=query_filter_power,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [None, count_element], 'tickwidth': 1, 'tickcolor': "gray"},
            'bar': {'color': "#025669"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            # 'steps': [
            #     {'range': [0, max//3], 'color': 'red'},
            #     {'range': [max//3, (max//3)*2], 'color': 'yellow'},
            #     {'range': [(max//3)*2, max], 'color': 'green'}],
        },
        title={
            "text": "Суммарное t работы оборудования <br><span style='font-size:0.8em;color:gray'>в интервалах потребляемой мощности, мин</span><br> "}))
    fig22 = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        delta={'reference': count_element},
        value=query_filter_any_power,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [None, count_element], 'tickwidth': 1, 'tickcolor': "gray"},
            'bar': {'color': "green"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            # 'steps': [
            #     {'range': [0, max//3], 'color': 'red'},
            #     {'range': [max//3, (max//3)*2], 'color': 'yellow'},
            #     {'range': [(max//3)*2, max], 'color': 'green'}],
        },
        title={
            "text": "Суммарное t работы оборудования <br><span style='font-size:0.8em; color:gray'>при любой мощности, мин</span><br> "}))

    fig3 = go.Figure(go.Indicator(
        mode="number",
        number={'font': {'color': 'red', 'size': 87}},
        value=query_filter_max_power,
        title={
            "text": "МАКСИМАЛЬНАЯ<br><span style='font-size:0.8em;color:gray'>потребляемая мощность, кВт</span>"},
        domain={'row': 0, 'column': 0}))

    fig4 = go.Figure(go.Indicator(
        mode="number",
        number={'font': {'color': 'green', 'size': 87}},
        value=query_filter_mean_power,
        title={
            "text": "СРЕДНЯЯ<br><span style='font-size:0.8em;color:gray'>потребляемая мощность, кВт</span>"},
        domain={'row': 0, 'column': 0}))

    return fig1, fig2, fig21, fig22, fig4, fig3


if __name__ == '__main__':
    app.run_server(debug=False)
