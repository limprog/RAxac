from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
# import dash_design_kit as ddk
import os
data_Y = pd.read_csv("data/Участники anonimized.csv")
data = pd.DataFrame()


