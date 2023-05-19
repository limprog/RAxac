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