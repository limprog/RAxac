from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
from new_def import *
# import dash_design_kit as ddk
import os
data_Y = pd.read_csv("data/Участники anonimized.csv")
data = pd.DataFrame()
com_competihon = ['Геодезия.csv', 'Мехатроника.csv', 'Управление качеством.csv', 'Технологии композитов.csv', 'Строительный контроль.csv', 'Инженерное проектирование.csv', 'Информационная безопасность.csv', 'Управление жизненным циклом.csv', 'Бетонные строительные работы.csv', 'Инженерное мышление. Каракури.csv', 'Промышленная механика и монтаж.csv', 'Программные решения для бизнеса.csv', 'Сетевое и системное администрирование.csv', 'Цифровое ПСР-Предприятие (Lean Smart Plant).csv', 'Вывод из эксплуатации объектов использования атомной энергии.csv', 'Корпоративная защита от внутренних угроз информационной безопасности.csv']



for i in com_competihon:
    data = sort_n(pd.read_csv("data/Anonimized/"+i))
    data.to_csv("data2/Anonimized/"+i)




