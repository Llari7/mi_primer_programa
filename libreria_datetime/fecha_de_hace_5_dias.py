import datetime

nombre_dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
fecha_hace_cinco_dias = datetime.datetime.today() - datetime.timedelta(days=5)

print("La fecha de hace 5 días es {}".format(fecha_hace_cinco_dias.strftime("%d/%m/%Y")))
print("El dái de la semana  de hace 5 días es {}".format(nombre_dias_semana[fecha_hace_cinco_dias.weekday()]))
