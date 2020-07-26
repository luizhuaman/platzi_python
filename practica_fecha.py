#¿cuantos meses han transcurrido desde mi fec nac?
from datetime import datetime, date, timedelta

Hoy=datetime.now()
dia_nac=int(input("Día de nacimiento: "))
mes_nac=int(input("Mes de nacimiento: "))
year_nac=int(input("Año de nacimiento; "))
fecha_nac=datetime(year_nac,mes_nac,dia_nac)
meses=(int(Hoy.year)-int(fecha_nac.year))*12+int(Hoy.month)-int(fecha_nac.month)
print(meses)

#Día actual
today = date.today()
#Fecha actual
now = datetime.now()

print(today)
# 2020-04-16
print(now)
# 2020-04-16 16:46:23.821276
#Date : ATRIBUTOS
print("El día actual es {}".format(today.day))
print("El mes actual es {}".format(today.month))
print("El año actual es {}".format(today.year))

# PARA TRABAJAR CON UNA FECHA EN PARTICULAR
new_datetime = datetime(2019, 2, 28, 10, 15, 00, 00000)
new_date = date (2020,1,1)

#FORMATO DE FECHAS strftime
naw = datetime.now()
format = naw.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
print(format)

#Sumar dos días a la fecha actual
ahora = datetime.now()
nueva_fecha = ahora + timedelta(days=2)
#Comparación
if ahora < nueva_fecha:
    print("La fecha actual: {}, es menor que la nuevafecha: {}".format(nueva_fecha,ahora))


#con funcion
def formato_mes_dia(date):
    months=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
    days = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
    day = days[date.weekday()]
    # print(day)
    month=months[date.month-1]
    # print(month)
    year = date.year
    # print(year)
    message = "{} {} de {} del {}".format(day,date.day, month, year)

    return message

# now = datetime.now()
print(formato_mes_dia(datetime.now()))