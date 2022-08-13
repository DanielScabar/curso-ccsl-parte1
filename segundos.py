segundos = int(input("Por favor, entre com o número de segundos que deseja converter:"))

dias = segundos // (60*60*24)
segundosRestantes = segundos % (60*60*24)
horas = segundosRestantes // (60*60)
segundosRestantes = segundosRestantes % (60*60)
minutos = segundosRestantes // 60
segundosRestantes = segundosRestantes % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundosRestantes,"segundos.")
