from time import sleep
import datetime

NIGHT_STARTS = 19
DAY_STARTS = 8
HOUR_DURATION = 0.25
WEEK_DAYS = "LMXJVSD"


def write_file_and_screen(text, file_name):
    with open(file_name, "a") as hours_file:
        hours_file.write("{}{}".format(text, "\n"))
        print(text)

def repeat_alarm():
    if input("¿Quiere que la alarma se repita?(S/N)  ").upper() == "S":
        return True
    else:
        return False

def unique_day():
    if input("¿Quiere que la alarma suene un único día?(S/N) ").upper() == "S":
        return True
    else:
        return False

def current_time_equals_alarm_date(current_time, alarm_date):
    if current_time.year == alarm_date.year:
        if current_time.month == alarm_date.month:
            if current_time.day == alarm_date.day:
                if current_time.hour == alarm_date.hour:
                    return True
    else:
        return False



def main():
    current_time = datetime.datetime.now()
    is_night = False
    alarm_unique_date = False
    alarm_weekdays = {"L": False, "M": False, "X": False, "J": False, "V": False, "S": False, "D": False}

    alarm_hour = int(input("¿A qué hora quiere que suene la alarma?(Formato 24h) "))
    if repeat_alarm():
        alarm_days = input("¿Qué días quiere que suene la alarma?(L/M/X/J/V/S/D) ")
        for day in alarm_days:
            if not day == "/":
                alarm_weekdays[day] = True
    elif unique_day():
        alarm_unique_date = True
        alarm_unique_day = input("¿Qué fecha quiere que suene la alarma?(dd/mm/yyyy) ")
        alarm_date = datetime.datetime.strptime(alarm_unique_day, "%d/%m/%Y")
        alarm_date = alarm_date.replace(hour = alarm_hour)
    else:
        if current_time.hour > alarm_hour:
            alarm_weekdays[WEEK_DAYS[current_time.weekday() + 1]] = True
        else:
            alarm_weekdays[WEEK_DAYS[current_time.weekday()]] = True


    while True:
        sleep(HOUR_DURATION)
        current_time += datetime.timedelta(hours=1)
        light_changed = False

        if (current_time.hour >= NIGHT_STARTS or current_time.hour <= DAY_STARTS) and not is_night:
            is_night = True
            light_changed = True

        elif (current_time.hour > DAY_STARTS and current_time.hour < NIGHT_STARTS) and is_night:
            is_night = False
            light_changed = True


        if light_changed:
            if is_night:
                write_file_and_screen("Se ha hecho de noche", "horas.txt")
            else:
                write_file_and_screen("Se ha hecho de día", "horas.txt")

        write_file_and_screen("La hora actual es {}".format(current_time), "horas.txt")

        if alarm_unique_date:
            if current_time_equals_alarm_date(current_time, alarm_date):
                write_file_and_screen("¡¡¡¡ALARMAAAAA!!!!", "horas.txt")
        else:
            if alarm_weekdays[WEEK_DAYS[current_time.weekday()]] and current_time.hour == alarm_hour:
                write_file_and_screen("¡¡¡¡ALARMAAAAA!!!!", "horas.txt")

if __name__ == "__main__":
    main()
