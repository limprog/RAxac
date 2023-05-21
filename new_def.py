import os

import pandas as pd
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.mixture import GaussianMixture
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
    if 'ФИО1' in data.columns:
        if 'ФИО3' in data.columns:
            f = pd.Series(data['ФИО1'].values, index=data['Название команды'].values)
            a = pd.Series(data['ФИО2'].values, index=data['Название команды'].values)
            d = pd.Series(data['ФИО3'].values, index=data['Название команды'].values)
            data = data.drop(["ФИО1", "ФИО2","ФИО3"], axis=1)
            b = pd.concat([f, a, d], axis=0)
        elif 'ФИО2' in data.columns:
            f = pd.Series(data['ФИО1'].values, index=data['Название команды'].values)
            a = pd.Series(data['ФИО2'].values, index=data['Название команды'].values)
            b = pd.concat([f, a], axis=0)
            data = data.drop(["ФИО1", "ФИО2"], axis=1)
        if 'ФИО4' in data.columns:
            e = pd.Series(data['ФИО4'].values, index=data['Название команды'].values)
            b = pd.concat([f, a, d, e], axis=0)
            data = data.drop(["ФИО4"], axis=1)
        if 'ФИО5' in data.columns:
            t = pd.Series(data['ФИО5'].values, index=data['Название команды'].values)
            b = pd.concat([f, a, d, e, t], axis=0)
            data = data.drop(["ФИО5"], axis=1)
        if 'ФИО6' in data.columns:
            y = pd.Series(data['ФИО6'].values, index=data['Название команды'].values)
            data = data.drop(['ФИО6'], axis=1)
            b = pd.concat([f, a, d, e, t, y], axis=0)
        if 'ФИО7' in data.columns:
            o = pd.Series(data['ФИО7'].values, index=data['Название команды'].values)
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
    if 'Unnamed: 0' in data1.columns:
        data1 = data1.drop(["Unnamed: 0"], axis=1)
    return data1

# def ob_to_dt(data):'Unnamed: 0' in data.columns
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


def ob_to_float(data):
    comma_cols = [col for col in data.columns if data[col].dtype == 'object' and data[col].str.contains(',').any()]
    for j in comma_cols:
        if j !='Место работы':
            data[j] = data[j].str.replace(',', '.')
            try:
                data[j] = data[j].astype(float)
            except ValueError:
                pass
    return data


def ob_to_string(data):
    data = data.drop(['Начало трудового стажа', 'Дата рождения', "Начало трудовой деятельности в РОСАТОМ", "Год оканчания","Профессия","Место образования","Специальность","Категория"], axis=1)
    object_rows = data.select_dtypes(include=['object']).columns
    for i in object_rows:

        if  "Команда" !=i !="ФИО" and "Список компетенций" != "Роль в мероприятии":
            data[i] = data[i].astype('category')
            data[i+"int"] = data[i].cat.codes

    if 'Unnamed: 0' in data.columns:
        data = data.drop(["Unnamed: 0"], axis=1)
    print(data)
    return data


def fit_2(data, k1, k2, name, n_components=3):
    scaler = StandardScaler()
    dataset_temp = data[[k1, k2]]
    X_std = scaler.fit_transform(dataset_temp)
    X = normalize(X_std, norm='l2')

    gmm = GaussianMixture(n_components=n_components, covariance_type='spherical', max_iter=2000, random_state=5).fit(X)
    labels = gmm.predict(X)
    dataset_temp[name] = labels
    data = data.merge(dataset_temp[name], left_index=True, right_index=True)
    if set(["Unnamed: 0"]).issubset(data.columns):
        data = data.drop(["Unnamed: 0"], axis=1)
    return data


def fit_3(data, k1, k2, k3, name, n_components=3):
    scaler = StandardScaler()
    dataset_temp = data[[k1, k2, k3]]
    X_std = scaler.fit_transform(dataset_temp)
    X = normalize(X_std, norm='l2')
    if 'Unnamed: 0' in data.columns:
        data = data.drop(["Unnamed: 0"], axis=1)
    gmm = GaussianMixture(n_components=n_components, covariance_type='spherical', max_iter=2000, random_state=5).fit(X)
    labels = gmm.predict(X)
    dataset_temp[name] = labels
    data = data.merge(dataset_temp[name], left_index=True, right_index=True)
    return data


def data_cotanizm():
    test = []
    data2 = pd.read_csv("new_data/Anonimized/Участники anonimized.csv")
    for i in os.listdir("new_data/Anonimized"):
        if i != "Участники anonimized.csv":
            path = "new_data/Anonimized/" + i

            data = pd.read_csv(path)

            data = fio_meng(data)
            data = sort_n(data)
            data = merg(data, data2)
            print(dict(data))
            data = ob_to_float(data)
            data = ob_to_string(data)

            try:
                data = fit_3(data, "Баллы, %", "Пол", "Образованиеint", "BPO")
                data = fit_3(data, "Баллы, %", "Должностьint", "Образованиеint", "BDO")
            except KeyError as e:
                if "KeyError: \"['Образованиеint'] not in index\"" == e:
                    data["Образованиеint"] = 0
                    data = fit_3(data, "Баллы, %", "Пол", "Образованиеint", "BPO")
                    data = fit_3(data, "Баллы, %", "Должностьint", "Образованиеint", "BDO")
                if "KeyError: \"['Должностьint'] not in index\"" == e:
                    data["Должностьint"] = 0
                    data = fit_3(data, "Баллы, %", "Пол", "Образованиеint", "BPO")
                    data = fit_3(data, "Баллы, %", "Должностьint", "Образованиеint", "BDO")
                if "KeyError: \"['Баллы, %'] not in index\"" == e:
                    data['Баллы, %'] = 0
                    data = fit_3(data, "Баллы, %", "Пол", "Образованиеint", "BPO")
                    data = fit_3(data, "Баллы, %", "Должностьint", "Образованиеint", "BDO")
            except ValueError:
                data['Баллы, %'] = 0
                data = fit_3(data, "Баллы, %", "Пол", "Образованиеint", "BPO")
                data = fit_3(data, "Баллы, %", "Должностьint", "Образованиеint", "BDO")


            data.to_csv("new_data/Anonimized/" + i)






    # for i in os.listdir("data/Anonimized"):
    #     data = pd.read_csv("data/Anonimized/" + i)
    #     comma_cols = [col for col in data.columns if data[col].dtype == 'object' and data[col].str.contains(',').any()]
    #     for j in comma_cols:
    #         if j != 'Место работы':
    #             data[j] = data[j].str.replace(',', '.')
    #             try:
    #                 data[j] = data[j].astype(float)
    #             except ValueError:
    #                 pass
    #     data.to_csv("data2/Anonimized/" + i)
