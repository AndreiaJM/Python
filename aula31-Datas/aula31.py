import datetime

data=datetime.datetime.now()

#criar elemento com data expedifica
nasc=datetime.datetime(1994,12,27) #construtor
print(nasc)

#strftime("%A") = dia da semana da data expedificada
print(nasc.strftime("%A"))
#%w = numero do dia da semana
#%d = numero dia do mes
#%a = texto dia da semana abreviado
#%b = texto mes abreviado
#%B = texto mes
#%m = numero do mes
#%y = ano com dois digitos
#%Y = ano com quatro digitos
#%H = 00 - 23
#%I = 00 - 24
#%p = AM / PM
#%M = minutos
#%S = segundos
#%f = microsegundos
#%j = dia do ano 001-365



print(str(data.day)+"/"+str(+data.month)+"/"+str(+data.year))