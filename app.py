import base64
import datetime
import io
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import pandas as pd
import plotly.express as px
from new_def import *
# import dash_design_kit as ddk
import os
import gunicorn
data_Y = pd.read_csv("data/Участники anonimized.csv")
data = pd.read_csv("data/Anonimized/Аддитивные технологии.csv")
com_competihon = ['Геодезия.csv', 'Мехатроника.csv', 'Управление качеством.csv', 'Технологии композитов.csv', 'Строительный контроль.csv', 'Инженерное проектирование.csv', 'Информационная безопасность.csv', 'Управление жизненным циклом.csv', 'Бетонные строительные работы.csv', 'Инженерное мышление. Каракури.csv', 'Промышленная механика и монтаж.csv', 'Программные решения для бизнеса.csv', 'Сетевое и системное администрирование.csv', 'Цифровое ПСР-Предприятие (Lean Smart Plant).csv', 'Вывод из эксплуатации объектов использования атомной энергии.csv', 'Корпоративная защита от внутренних угроз информационной безопасности.csv']


app = Dash(__name__)
server=app.server
l=os.listdir('data/Anonimized')

app.layout = html.Div([
    html.H1(children='Кейс от Росатома', style={"text-align": "center"}),
    dcc.Tabs([
        dcc.Tab(label='Кластеризация', children=[
            "Выбор номинации",
            dcc.Dropdown(
                ['Корпоративная защита от внутренних угроз информационной безопасности', 'Инженер-технолог машиностроения',
                 'Работы на токарных универсальных станках', 'Водитель спецавтомобиля',
                 'Обслуживание и ремонт оборудования релейной защиты и автоматики', 'Машинное обучение и большие данные',
                 'Аддитивные технологии', 'Цифровое ПСР-Предприятие (Lean Smart Plant)', 'Анатилический контроль',
                 'Сетевое и системное администрирование', 'Изготовление прототипов', 'Промышленная автоматика',
                 'Программные решения для бизнеса', 'Бетонные строительные работы', 'Неразрущающий контроль',
                 'Информационная безопасность', 'Управление качеством', 'Строительный контроль',
                 'Токарные работы на станках с ЧПУ',
                 'Квантовые технологии', 'Фрезерные работы на станках с ЧПУ', 'Технологии композитов',
                 'Технологические системы энергетических объектов', 'Инженерное мышление', 'Геодезия', 'Сварочные технологии',
                 'Мехатроника', 'Сметное дело', 'Электромонтаж', 'Промышленная механика и монтаж',
                 'Работы на фрезерных универсальных станках', 'Управление жизненным циклом', 'Радиационный контроль',
                 'Охрана труда', 'Охрана окружающей среды', 'Вывод из эксплуатации объектов использования атомной энергии',
                 'Электроника', 'Инженерное проектирование', 'Инженер-конструктор'],
                 'Корпоративная защита от внутренних угроз информационной безопасности',
                 id='clientside-graph-indicator'),
            "Тип кластеризации",
            dcc.Dropdown(["BPO", "BDO"], "BPO",id='graf'),
            html.H2(style={"text-align": "center"}, children="Пояснение"),
            html.H4( children="1. BPO-Классификация по баллам, Полу, образованию"),
            html.H4( children="1. BDO-Классификация по баллам, Должности, образованию"),
            html.Table(
                children=[
                html.Td([
                dcc.Graph(
                    figure={},
                    id='1-graph',
                    style={'display': 'inline-block'}),
                ]),
                html.Td([
                dcc.Graph(
                    figure={},
                    id='2-graph',
                    style={'display': 'inline-block'})
                ]),
            ]),
        ]),
        dcc.Tab(label="Графики", children=[
        "Выбор номинации",
            dcc.Dropdown(
                ['Корпоративная защита от внутренних угроз информационной безопасности', 'Инженер-технолог машиностроения',
                 'Работы на токарных универсальных станках', 'Водитель спецавтомобиля',
                 'Обслуживание и ремонт оборудования релейной защиты и автоматики', 'Машинное обучение и большие данные',
                 'Аддитивные технологии', 'Цифровое ПСР-Предприятие (Lean Smart Plant)', 'Анатилический контроль',
                 'Сетевое и системное администрирование', 'Изготовление прототипов', 'Промышленная автоматика',
                 'Программные решения для бизнеса', 'Бетонные строительные работы', 'Неразрущающий контроль',
                 'Информационная безопасность', 'Управление качеством', 'Строительный контроль',
                 'Токарные работы на станках с ЧПУ',
                 'Квантовые технологии', 'Фрезерные работы на станках с ЧПУ', 'Технологии композитов',
                 'Технологические системы энергетических объектов', 'Инженерное мышление', 'Геодезия', 'Сварочные технологии',
                 'Мехатроника', 'Сметное дело', 'Электромонтаж', 'Промышленная механика и монтаж',
                 'Работы на фрезерных универсальных станках', 'Управление жизненным циклом', 'Радиационный контроль',
                 'Охрана труда', 'Охрана окружающей среды', 'Вывод из эксплуатации объектов использования атомной энергии',
                 'Электроника', 'Инженерное проектирование', 'Инженер-конструктор'],
                 'Корпоративная защита от внутренних угроз информационной безопасности',
                 id='clientside-graph-indicator2'),
            "Значение по x",
            dcc.Dropdown(["Баллы, %","Баллы, ед.", "Должностьint","BPO", "BDO"], "Должностьint", id="x" ),
            "Значение по y",
            dcc.Dropdown(["Баллы, %","Баллы, ед.", "Должностьint","BPO", "BDO"], "Баллы, %",id="y"),
            "Цвет",
            dcc.Dropdown(["Пол", "BPO","BDO"], "Пол", id="color"),
            html.Table(
                children=[
                    html.Td([
                    dcc.Graph(
                        figure={},
                        id='3-graph',
                        style={'display': 'inline-block'}),
                    ]),
                    html.Td([
                    dcc.Graph(
                        figure={},
                        id='4-graph',
                        style={'display': 'inline-block'}),

                        ]),
                    ]),
                ]),


        dcc.Tab(label="Загрузка файлов", children=[
            dcc.Upload(
                id='upload-data',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
                # Allow multiple files to be uploaded
                multiple=True),
                dcc.Dropdown(
                    options=['Корпоративная защита от внутренних угроз информационной безопасности', 'Инженер-технолог машиностроения',
                 'Работы на токарных универсальных станках', 'Водитель спецавтомобиля',
                 'Обслуживание и ремонт оборудования релейной защиты и автоматики', 'Машинное обучение и большие данные',
                 'Аддитивные технологии', 'Цифровое ПСР-Предприятие (Lean Smart Plant)', 'Анатилический контроль',
                 'Сетевое и системное администрирование', 'Изготовление прототипов', 'Промышленная автоматика',
                 'Программные решения для бизнеса', 'Бетонные строительные работы', 'Неразрущающий контроль',
                 'Информационная безопасность', 'Управление качеством', 'Строительный контроль',
                 'Токарные работы на станках с ЧПУ',
                 'Квантовые технологии', 'Фрезерные работы на станках с ЧПУ', 'Технологии композитов',
                 'Технологические системы энергетических объектов', 'Инженерное мышление', 'Геодезия', 'Сварочные технологии',
                 'Мехатроника', 'Сметное дело', 'Электромонтаж', 'Промышленная механика и монтаж',
                 'Работы на фрезерных универсальных станках', 'Управление жизненным циклом', 'Радиационный контроль',
                 'Охрана труда', 'Охрана окружающей среды', 'Вывод из эксплуатации объектов использования атомной энергии',
                 'Электроника', 'Инженерное проектирование', 'Инженер-конструктор'],
                    value="Аддитивные технологии",
                    id='4'),
                    "Тип кластеризации",
                    dcc.Dropdown(["BPO", "BDO"], "BPO",id='graf2'),
                    html.Table(children=[
                        html.Td([
                            dcc.Graph(
                                    figure={},
                                    id='5-graph',
                                    style={'display': 'inline-block'}),
                            ]),
                            html.Td([
                                dcc.Graph(
                                    figure={},
                                    id='6-graph',
                                    style={'display': 'inline-block'}),

                            ]),
                        html.Div(children={}, id="5")
                    ]),
                ]),
            dcc.Tab(label="Скачка данных", children=[
                "Скачать изначальный датасет",
                dcc.Dropdown(options=['Корпоративная защита от внутренних угроз информационной безопасности', 'Инженер-технолог машиностроения',
                 'Работы на токарных универсальных станках', 'Водитель спецавтомобиля',
                 'Обслуживание и ремонт оборудования релейной защиты и автоматики', 'Машинное обучение и большие данные',
                 'Аддитивные технологии', 'Цифровое ПСР-Предприятие (Lean Smart Plant)', 'Анатилический контроль',
                 'Сетевое и системное администрирование', 'Изготовление прототипов', 'Промышленная автоматика',
                 'Программные решения для бизнеса', 'Бетонные строительные работы', 'Неразрущающий контроль',
                 'Информационная безопасность', 'Управление качеством', 'Строительный контроль',
                 'Токарные работы на станках с ЧПУ',
                 'Квантовые технологии', 'Фрезерные работы на станках с ЧПУ', 'Технологии композитов',
                 'Технологические системы энергетических объектов', 'Инженерное мышление', 'Геодезия', 'Сварочные технологии',
                 'Мехатроника', 'Сметное дело', 'Электромонтаж', 'Промышленная механика и монтаж',
                 'Работы на фрезерных универсальных станках', 'Управление жизненным циклом', 'Радиационный контроль',
                 'Охрана труда', 'Охрана окружающей среды', 'Вывод из эксплуатации объектов использования атомной энергии',
                 'Электроника', 'Инженерное проектирование', 'Инженер-конструктор'],
                    value="Аддитивные технологии.csv",
                    id='6'),
                html.Button("Скачать ", id="btn-download-txt"),
                dcc.Download(id="download-text"),
"Скачать обученный датасет",
                dcc.Dropdown(options=['Корпоративная защита от внутренних угроз информационной безопасности', 'Инженер-технолог машиностроения',
                 'Работы на токарных универсальных станках', 'Водитель спецавтомобиля',
                 'Обслуживание и ремонт оборудования релейной защиты и автоматики', 'Машинное обучение и большие данные',
                 'Аддитивные технологии', 'Цифровое ПСР-Предприятие (Lean Smart Plant)', 'Анатилический контроль',
                 'Сетевое и системное администрирование', 'Изготовление прототипов', 'Промышленная автоматика',
                 'Программные решения для бизнеса', 'Бетонные строительные работы', 'Неразрущающий контроль',
                 'Информационная безопасность', 'Управление качеством', 'Строительный контроль',
                 'Токарные работы на станках с ЧПУ',
                 'Квантовые технологии', 'Фрезерные работы на станках с ЧПУ', 'Технологии композитов',
                 'Технологические системы энергетических объектов', 'Инженерное мышление', 'Геодезия', 'Сварочные технологии',
                 'Мехатроника', 'Сметное дело', 'Электромонтаж', 'Промышленная механика и монтаж',
                 'Работы на фрезерных универсальных станках', 'Управление жизненным циклом', 'Радиационный контроль',
                 'Охрана труда', 'Охрана окружающей среды', 'Вывод из эксплуатации объектов использования атомной энергии',
                 'Электроника', 'Инженерное проектирование', 'Инженер-конструктор'],
                    value="Аддитивные технологии.csv",
                    id='7'),
                html.Button("Скачать ", id="btn-download-txt2"),
                dcc.Download(id="download-text2")
            ])

        ]),
    ])


@app.callback(
    Output("download-text", "data"),
    Input("btn-download-txt", "n_clicks"),
    Input("6", "value"),
    prevent_initial_call=True,
)
def func(n_clicks, i):
    df = pd.read_csv("data/Anonimized/"+i+".csv")
    return dcc.send_data_frame(df.to_csv, i+".csv")

@app.callback(
    Output("download-text2", "data"),
    Input("btn-download-txt2", "n_clicks"),
    Input("7", "value"),
    prevent_initial_call=True,
)
def func(n_clicks, i):
    df = pd.read_csv("new_data/Anonimized/"+i+".csv")
    return dcc.send_data_frame(df.to_csv, i+".csv")

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            df.to_csv("new_data/Anonimized/"+filename)

        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
@app.callback(Output('5', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        data_cotanizm()
        return None




@callback(Output("3-graph",  component_property='figure'),
          Output("4-graph",  component_property='figure'),
          Input("clientside-graph-indicator2", "value"),
          Input("y", "value"),
          Input("x", "value"),
          Input("color", "value"))
def graf_2(test, x, y, color):
    data = pd.read_csv("data/Anonimized/"+test+ ".csv")
    fig = px.scatter(data, x=x, y=y, color=color, hover_name="ФИО",)
    fig2 = px.bar(data, x=x, y=y, color=color, hover_name="ФИО",)
    return fig,fig2

@callback(Output("1-graph",  component_property='figure'),
          Output("2-graph",  component_property='figure'),
          Input("clientside-graph-indicator", "value"),
          Input("graf", "value"))
def graf_1(X,Y):
    data = pd.read_csv("data/Anonimized/"+X+".csv")
    if Y == "BPO":
        a = "Пол"
    else:
        a = "Должностьint"
    try:
        fig = px.scatter_3d(data, x="Баллы, %", y="Образованиеint", z=a, hover_name="ФИО", color = Y)
        fig2 = px.scatter(data, x="Баллы, %", y="Образованиеint", color=Y)
    except:
        data['Образованиеint'] = 0
        fig = px.scatter_3d(data, x="Баллы, %", y="Образованиеint", z=a, hover_name="ФИО", color=Y)
        fig2 = px.scatter(data, x="Баллы, %", y="Образованиеint", color=Y, hover_name="ФИО")
    return fig, fig2


@callback(Output("5-graph",  component_property='figure'),
          Output("6-graph",  component_property='figure'),
          Input("4", "value"),
          Input("graf2", "value"))
def graf_3(X,Y):
    data = pd.read_csv("new_data/Anonimized/"+X+".csv")
    if Y == "BPO":
        a = "Пол"
    else:
        a = "Должностьint"
    try:
        fig = px.scatter_3d(data, x="Баллы, %", y="Образованиеint", z=a, hover_name="ФИО", color = Y)
        fig2 = px.scatter(data, x="Баллы, %", y="Образованиеint", color=Y, hover_name="ФИО")
    except:
        data['Образованиеint'] = 0
        fig = px.scatter_3d(data, x="Баллы, %", y="Образованиеint", z=a, hover_name="ФИО", color=Y)
        fig2 = px.scatter(data, x="Баллы, %", y="Образованиеint", color=Y, hover_name="ФИО")
    return fig, fig2
if __name__ == '__main__':
    app.run_server(debug=False)
#
style={
                'display': 'inline-block',
                'vertical-align': 'bottom'},