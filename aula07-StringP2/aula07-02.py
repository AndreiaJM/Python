curso="Curso de Python"
canal="CFB Cursos"

dia=15
mes="dezembro"
ano=2022
cidade="São Paulo"

data="{},{} de {} de {} \n {}" #varival com placeholders
# \n quebra de linha no placeholder
#\"\" aspas na impressão da variavel com placeholder
#\'\' apostrofo
#\r enter
#\t tabulação (tecla tab)
#\b backspace (tecla de apagar)

res=curso+" "+canal # + concatena strings e espaços

#O python nao concatena String com inteiro
#Sendo necessario fazer o casting com o metodo srt()
print(cidade+" "+str(dia)+" "+mes+" "+str(ano))

#metodo format substitui as variáveis passadas no placeholder
print(data.format(cidade,dia,mes,ano,canal))



