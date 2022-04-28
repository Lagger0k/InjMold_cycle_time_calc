# тут будет логика связанная с БД

import pandas as pd


def read_excel_data(string):
    """returns an object with data"""
    return pd.read_excel(string, sheet_name=0)


def return_material(data):
    """returns a list of unique materials from the database"""
    return sorted(set(data[data.columns[0]]))


def return_thickness(data, material):
    """returns a list of available thicknesses for the chosen material"""
    return sorted(data[data.columns[1]].where(data[data.columns[0]] == material).dropna())


def return_time(data, material, thickness):
    """returns the cycle time for the given conditions"""
    table = dict()
    for tmp in data.values:
        mat, s, t = tmp[0], tmp[1], tmp[2]
        table.setdefault(mat, {s: t})
        table[mat][s] = t
    return table[material][thickness]


b = read_excel_data('Данные ТПА.xlsx')

mat, s = input('введите название материала, затем нажмите enter: ').strip(), \
         float(input('введите толщину детали, затем нажмите enter: '))


print(return_time(b, mat, s))


