import datetime

nombre_dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
dia_cumpleaños = int(input("¿Que día de mes es tu cumpleaños? "))
mes_cumpleaños = int(input("¿Que mes del año (númerico del 1 al 12) es tu cumpleaños? "))
hoy = datetime.datetime.today()
anho_actual = hoy.year
cumpleanhos_usuario = datetime.datetime(day=dia_cumpleaños, month=mes_cumpleaños, year=anho_actual)
restante_cumpleaños = cumpleanhos_usuario - hoy

print("Falta {} días y {} horas para tu cumpleaños.".format(restante_cumpleaños.days, int(restante_cumpleaños.seconds/3600)))
print("Tu cumpleaños caerá en {}".format(nombre_dias_semana[cumpleanhos_usuario.weekday()]))