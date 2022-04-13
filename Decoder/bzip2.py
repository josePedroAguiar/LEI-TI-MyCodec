import bz2
def bdecompress(nome):
    f=open(nome+".bzip2","rb")
    data=f.read()
    c=bz2.decompress(data)
    f=open(nome+".f","wb")
    f.write(c)



