import pandas as pd

def fio_meng(data):
    if set(['ФИО участников']).issubset(data.columns):
        data_temp = data['ФИО участников'].str.split(";", expand=True)
        data_temp.columns = ['ФИО{}'.format(x + 1) for x in data_temp.columns]
        # data_temp = data_temp.drop(['ФИО участников'], axis=1)
        data = data.join(data_temp)
        return data


def com(path):
    data = pd.read_csv(path)
    if set(['ФИО участников']).issubset(data.columns):
        name = path.split("/")[-1]
        return name
    else:
        pass

def sort_n(data):
    if set(['ФИО3']).issubset(data.columns):
        f = pd.Series(data['ФИО1'].values, index=data['Название команды'].values)
        a = pd.Series(data['ФИО2'].values, index=data['Название команды'].values)
        d = pd.Series(data['ФИО3'].values, index=data['Название команды'].values)
        data = data.drop(["ФИО1", "ФИО2","ФИО3"], axis=1)
        b = pd.concat([f, a, d], axis=0)
    else:
        f = pd.Series(data['ФИО1'].values, index=data['Название команды'].values)
        a = pd.Series(data['ФИО2'].values, index=data['Название команды'].values)
        b = pd.concat([f, a], axis=0)
        data = data.drop(["ФИО1", "ФИО2"], axis=1)
    if set(['ФИО4']).issubset(data.columns):
        e = pd.Series(data['ФИО4'].values, index=data['Название команды'].values)
        b = pd.concat([f, a, d, e], axis=0)
        data = data.drop(["ФИО4"], axis=1)
    if set(['ФИО5']).issubset(data.columns):
        t = pd.Series(data['ФИО5'].values, index=data['Название команды'].values)
        b = pd.concat([f, a, d, e, t], axis=0)
        data = data.drop(["ФИО5"], axis=1)
    if set(['ФИО6']).issubset(data.columns):
        y = pd.Series(data['ФИО6'].values, index=data['Название команды'].values)
        data = data.drop(['ФИО6'], axis=1)
        b = pd.concat([f, a, d, e, t, y], axis=0)
    if set(['ФИО7']).issubset(data.columns):
        o = pd.Series(data['ФИО7'].values, index=data['Название команды'].values)
        data = data.drop(["ФИО7"], axis=1)
        b = pd.concat([f, a, d, e, t, y, o ], axis=0)
    data = data.set_index('Название команды')
    s = b
    data = data.merge(s.rename('new'), left_index=True, right_index=True)
    return data


