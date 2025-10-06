"""
vamos a realizar un programa que lea el archiva el sistema_log_extenso
e imprima por pantalla todos los mensajes del tipo error
"""

log = open("sistema_log_extenso.txt", "r")
log_info= open("info.txt", "w")
log_data = log.readlines()

for line in log_data:
    if "INFO" in line:
        log_info.write(line)