import pandas
# xlwt, xlrd, openpyxl
nosaukums = 'dzivnieki.xls'
dati = pandas.read_excel(nosaukums)
print(dati)
print(dati.shape)

dati = pandas.read_excel(nosaukums, sheet_name="Sheet1")
print("1.tabula\n",dati)
dati2 = pandas.read_excel(nosaukums, sheet_name="Sheet2")
print("2.tabula\n",dati2)

apvienotie_dati = pandas.concat([dati,dati2]) # konkatenācija
print("apvienotie dati\n", apvienotie_dati)

saskirots = apvienotie_dati.sort_values("Vecums")
print("sašķirots\n", saskirots)
saskirots = apvienotie_dati.sort_values("Vecums", ascending=False) # augoša secība = False
print("sašķirots\n", saskirots)

print("\n",type(saskirots))
saskirots.to_excel("dzivnieki_apvienoti.xls", index=False)