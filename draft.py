from datetime import datetime,date
day = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
# thisXMas = date(2020,4,20)
# print(thisXMas)
# thisXMasDay = thisXMas.weekday()
# print(thisXMasDay)
thisXMasDayAsString = day[(date(2020,4,20)).weekday()]
print(thisXMasDayAsString)


# now = datetime.now()
# today = date.today()
# print(now)
# print(today)

now = datetime.now()
dia=now.weekday()
print(dia)