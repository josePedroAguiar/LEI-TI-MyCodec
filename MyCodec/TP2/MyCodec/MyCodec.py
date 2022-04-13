import aritemeticcompress as ac
import bzip2 as b
import Filter as fl
import os
def compress(i):
    f = open(("data/"+i + ".bmp"), "rb")
    return f.read()
def main():
    x=""
    while(x!="0"):
        print("1-Comprimir todos os ficheiros\n" + "2-Comprimir um ficheiro em especifico\n" + "0-Sair\n")
        x = input("Seleção:")
        if(x=="2"):
            nome=input("Nome de Ficheiro:")
            data=compress(nome)
            filtro = input("Filter(0,1,2):")
            b.bzip(nome,fl.filtering(data,int(filtro)))
            ac.accompress(nome)
            os.remove("data/"+nome+".bzip2")
        elif (x== "1"):
            array = ["egg", "landscape", "pattern", "zebra"]
            for i in array:
                data = compress(i)
                filtro = input("Filter(0,1,2):")
                b.bzip(i,fl.filtering(data,int(filtro)))
                ac.accompress(i)
                os.remove("data/"+i + ".bzip2")
        elif(x=="0"):
            break
        else:
            print("Seleção Invalda\n")
main()
