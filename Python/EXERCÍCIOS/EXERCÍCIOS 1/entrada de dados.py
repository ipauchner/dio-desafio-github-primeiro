segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_seg = int(segundos_str)

dias = total_seg // 86400
seg_rest = total_seg % 86400
horas = seg_rest // 3600
minutos_rest = seg_rest % 3600
minutos = minutos_rest // 60
seg_rest_final = seg_rest % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",seg_rest_final,"segundos.")
