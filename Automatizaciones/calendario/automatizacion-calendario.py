import calendar
from pathlib import Path

meses_ano = list(calendar.month_name[1:])
dia_semana = ['Dia 1','Dia 2','Dia 3', 'Dia 4', 'Dia 5']

for i, mes in enumerate(meses_ano):
    for dia in dia_semana:
        Path(f'2022/{i+1}.{mes}/{dia}').mkdir(parents=True, exist_ok=True)