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
        o = pd.Series(dataNaN['ФИО7'].values, index=data['Название команды'].values)
        data = data.drop(["ФИО7"], axis=1)
        b = pd.concat([f, a, d, e, t, y, o ], axis=0)
    data = data.set_index('Название команды')
    s = b
    data = data.merge(s.rename('ФИО'), left_index=True, right_index=True)
    try:
        data = data.drop(["Unnamed: 0","№"], axis=1)
    except KeyError:
        print("Непредвиденные обстоятельчтва")
    return data

def merg(data1,data2):
    data1 = data1.set_index('ФИО')
    data2 = data2.set_index('ФИО')
    data1 = data1.merge(data2, left_index=True, right_index=True)
    if set(["Unnamed: 0"]).issubset(data1.columns):
        data1 = data1.drop(["Unnamed: 0"], axis=1)
    return data1

# def ob_to_dt(data):
#     dt = ['Начало трудового стажа', 'Дата рождения', "Начало трудовой деятельности в РОСАТОМ"]
#     for i in dt:
#         try:
#             data[i] = pd.to_datetime(data[i])
#             data["Month_"+i] = data[i].dt.month
#             data["Year_"+i] = data[i].dt.year
#             data["Day_"+i] = data[i].dt.day
#         except:
#             print(i)
#     return data

def ob_to_string(data):
    data = data.drop(['Начало трудового стажа', 'Дата рождения', "Начало трудовой деятельности в РОСАТОМ", "Год оканчания","Профессия","Место образования","Специальность","Категория", "Место работы"], axis=1)
    object_rows = data.select_dtypes(include=['object']).columns
    for i in object_rows:

        if  "Команда" !=i !="ФИО":
            data = pd.concat([data, pd.get_dummies(data[i], prefix=i)], axis=1)

    if set(["Unnamed: 0"]).issubset(data.columns):
        data = data.drop(["Unnamed: 0"], axis=1)
    print(data)
    return data
