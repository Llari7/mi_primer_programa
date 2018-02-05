import datetime

print("A continuación deberá introducir una fecha.")
dia_usuario = int(input("Día: "))
mes_usuario = int(input("Mes: "))
anho_usuario = int(input("Año: "))

fecha_usuario = datetime.datetime(day=dia_usuario, month=mes_usuario, year=anho_usuario)
fecha_actual = datetime.datetime.now()

if fecha_usuario < fecha_actual:
    dif_fechas = fecha_actual - fecha_usuario
else:
    dif_fechas = fecha_usuario - fecha_actual

print("La diferencia entre la fecha introducida y la fecha actual es de {} horas".format(int(dif_fechas.seconds/3600)))