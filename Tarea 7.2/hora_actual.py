
import time
def trabajo(hora,total_de_segundos_h_a,hora_actual):

    horaestablecida = time.strftime('19:00:00')
    lista_h_e = horaestablecida.split(":")
    hora1 = int(lista_h_e[0])
    hora1_convertido = hora1 * 3600
    minuto1 = int(lista_h_e[1])
    minuto1_convertido = minuto1 * 60
    segundo1 = int(lista_h_e[2])
    total_de_segundos_h_e = hora1_convertido + minuto1_convertido + segundo1
    if hora1 <= hora:
        return f"Son a las {hora_actual}, Es hora de ir a casa"

    else:
        segundo_restantes = total_de_segundos_h_e - total_de_segundos_h_a
        falta_horas = segundo_restantes // 3600
        sobrante1 = segundo_restantes % 3600
        falta_minutos = sobrante1 // 60
        falta_segundos = sobrante1 % 60
        return f"Queda {falta_horas}:{falta_minutos}:{falta_segundos} de trabajo "

def hora_actual_sistema():

    hora_actual = time.strftime('%H:%M:%S')
    lista_h_a = hora_actual.split(":")
    hora = int(lista_h_a[0])
    hora_convertido = hora * 3600
    minuto = int(lista_h_a[1])
    minuto_convertido = minuto * 60
    segundo = int(lista_h_a[2])
    total_de_segundos_h_a = hora_convertido + minuto_convertido + segundo
    return int(hora),int(total_de_segundos_h_a),str(hora_actual)

