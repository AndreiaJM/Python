"""
Condicionais em python: and / or

and = todas devem ser verdadeiras para o retorno verdadeiro
or = caso apenas uma condição seja verdadeira o retorno é verdadeiro

"""

clima="chuva"
lugar="clube"
dinheiro=550

if clima=="sol" and (dinheiro>300 and dinheiro<500):
    lugar="clube"
else:
    lugar="cinema"

print("Vou ao "+lugar)