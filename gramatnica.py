import pandas
from termcolor import colored as c
fails = pandas.ExcelFile('dati_masiviem.xlsx')
lapas = [] # tukšs masīvs priekš faila lapām
for lapas_nosaukums in fails.sheet_names:
    # sheet_names ir daļa no faila
    # nolasa visu lapu nosaukumus un cikliski iet tiem cauri
    lapas.append(fails.parse(lapas_nosaukums)) # pievieno masīvam pēc nosaukuma atrasto lapu
print(lapas)
print(c("Darbības", "green"))
# grey, red, green, yellow, blue, magenta, cyan, white
print(lapas[0].columns)

"""
Cena gab = (Pašizmaksa + 30% uzcenojums) * PVN
"""    
lapas[0]["Cena gab"] = lapas[0]["Pašizmaksa"]*1.3*1.21
# 100% = 1 50% = 0.5 30% = 0.3 130% = 1.3 21% = 1.21
print(lapas[0]["Cena gab"])