import os
import random
from re import S
from colorama import Fore,Back,Style

jogarNovamente="s"
jogadas=0
quemJoga=2 # 1 = CPU, 2 = JOGADOR
maxJogadas=9
vit="n"
velha=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def tela():
    global velha
    global jogadas
    os.system("cls")
    print("    0   1   2")
    print("0:  "+velha[0][0]+ " | " +velha[0][1]+ " | " + velha[0][2])
    print("   ----------")
    print("1:  "+velha[1][0]+ " | " +velha[1][1]+ " | " + velha[1][2])
    print("   ----------")
    print("2:  "+velha[2][0]+ " | " +velha[2][1]+ " | " + velha[2][2])
    print("   ----------")
    print("Jogadas: "+ Fore.GREEN + str(jogadas)+Fore.RESET)

def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga==2 and jogadas<maxJogadas:
        l=int(input("Linha..: "))
        c=int(input("Coluna..: "))
        try:
            while velha[l][c]!=" ":
                os.system("cls")
                print("Jogada invalida, tente novamente")
                l=int(input("Linha..: "))
                c=int(input("Coluna..: "))
                
            velha[l][c]="X"
            quemJoga=1
            jogadas+=1
        except:
            print("Linha e ou coluna invalida")
            
def cpuJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas
    if quemJoga==1 and jogadas<maxJogadas:
        l=random.randrange(0,3)
        c=random.randrange(0,3)
        while velha[l][c]!=" ":
            l=random.randrange(0,3)
            c=random.randrange(0,3)
        velha[l][c]="O"
        jogadas+=1
        quemJoga=2

def verificarVitoria():
    global velha
    vitoria="n"
    simbolos=["X","O"]
    for s in simbolos:
        vitoria="n"
        #verificar vitorias em linha
        il=ic=0
        while il<3:
            soma=0
            ic=0
            while ic<3:
                if(velha[il][ic]==s):
                    soma+=1
                ic+=1
            if(soma==3):
                vitoria=s
                break
            il+=1
        if(vitoria!="n"):
            break
        #verificar vitorias em coluna
        il=ic=0
        while ic<3:
            soma=0
            il=0
            while il<3:
                if(velha[il][ic]==s):
                    soma+=1
                ic+=1
            if(soma==3):
                vitoria=s
                break
            ic+=1
        if(vitoria!="n"):
            break
        #verifica diagonal 1
        soma=0
        indiag=0
        while indiag<3:
            if(velha[indiag][indiag]==s):
                soma+=1
            indiag+=1
        if(soma==3):
            vitoria=s
            break
        #Verifica diagonal 2
        soma=0
        indiagl=0
        indiagc=2
        while indiagc>=0:
            if(velha[indiagl][indiagc]==s):
                soma+=1
            indiagl+=1
            indiagc-=1
        if(soma==3):
            vitoria=s
            break
    return vitoria

def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    jogadas=0
    quemJoga=2 # 1 = CPU, 2 = JOGADOR
    maxJogadas=9
    vit="n"
    velha=[
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
        ]   
    


while True:
    tela()
    jogadorJoga()
    cpuJoga()
    tela()
    vit=verificarVitoria()
    if(vit!="n") or (jogadas>=maxJogadas):
        break
    
    #Não terminado

