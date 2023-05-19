from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
from new_def import *
# import dash_design_kit as ddk
import os
data_Y = pd.read_csv("data/Участники anonimized.csv")
data = pd.read_csv("data/Anonimized/Аддитивные технологии.csv")
com_competihon = ['Геодезия.csv', 'Мехатроника.csv', 'Управление качеством.csv', 'Технологии композитов.csv', 'Строительный контроль.csv', 'Инженерное проектирование.csv', 'Информационная безопасность.csv', 'Управление жизненным циклом.csv', 'Бетонные строительные работы.csv', 'Инженерное мышление. Каракури.csv', 'Промышленная механика и монтаж.csv', 'Программные решения для бизнеса.csv', 'Сетевое и системное администрирование.csv', 'Цифровое ПСР-Предприятие (Lean Smart Plant).csv', 'Вывод из эксплуатации объектов использования атомной энергии.csv', 'Корпоративная защита от внутренних угроз информационной безопасности.csv']
col = ["Компетенция"]
print(list(data.dtypes))
for i in os.listdir("data/Anonimized"):
    data = pd.read_csv("data/Anonimized/"+i)
    print(data.dtypes)
    comma_cols = [col for col in data.columns if data[col].dtype == 'object' and data[col].str.contains(',').any()]
    print(comma_cols)
    for j in comma_cols:
        data[j] = data[j].str.replace(',', '.')
        try:
            data[j] = data[j].astype(float)

        except ValueError:
            pass
        if set(["Unnamed: 0"]).issubset(data.columns):
            data = data.drop(["Unnamed: 0"], axis=1)
    data.to_csv("data/Anonimized/"+i)




