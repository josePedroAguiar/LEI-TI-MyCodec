
def filtering(nome,type):
    f=open(nome+".f","rb")
    s=f.read()
    data1=[]
    for i in s:
        data1.append(ord(chr(i)))
    dataf = []
    if type==1:
        m= data1[0]
        for i in range(1,len(data1),1):
            if ((data1[i]+m)>255):
                dataf.append(m+(~data1[i])+1)
            else:
                dataf.append(m+data1[i])
    else:
        m = data1[1]
        for i in range(2, len(data1), 1):
            if ((data1[i] + m)> 255):
                dataf.append(m+(~data1[i]+1))
                m=(m+(~data1[i]+1))
            else:
                dataf.append(m + data1[i])
                m=(data1[i]+m)
    f=open(nome+".bmp","wb")
    a=bytearray(dataf)
    f.write(a)



