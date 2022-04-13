import arithmeticdecompress as ac
import bzip2 as b
import filter as fl
import os

def main():
    x=""
    while(x!="0"):
        print("1-Comprimir um ficheiro em especifico\n" + "0-Sair\n")
        x = input("Seleção:")
        if(x=="1"):
            nome=input("Nome de Ficheiro:")
            filtro=input("Filtro:")
            ac.acD(nome,filtro)
            b.bdecompress(nome)
            fl.filtering(nome,filtro)
            os.remove(nome+".bzip2")
        elif(x=="0"):
            break
        else:
            print("Seleção Invalda\n")
main()