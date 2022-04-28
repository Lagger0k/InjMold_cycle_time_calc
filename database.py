# тут будет логика связанная с БД

import pandas as pd


b = pd.read_excel('Данные ТПА.xlsx', sheet_name=0)

data = dict()
for d in b.values:
    mat, s, t = d
    data.setdefault(mat, {s: t})
    data[mat][s] = t


mat, s = input('введите название материала, затем нажмите enter: ').strip(), \
         float(input('введите толщину детали, затем нажмите enter: '))

print(f'время цикла {data[mat][s]} с')


