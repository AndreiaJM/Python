import re #RegEx

#search = não retorna coleção, retorna a posição da primeira ocorrencia


texto="Cursos de Python do CFB Cursos, canal no Youtube"

res=re.search("Cursos", texto)


if res !=None:
    pi=res.start() #posição inicial da ocorrencia
    pf=res.end() #posição final da ocorrencia
    tam = pf-pi
    print("Posição inicial:"+str(pi))
    print("Posição inicial: "+str(pf))
    print("Tamanho da string: "+ str(tam))
else:
    print("Não localizado")
