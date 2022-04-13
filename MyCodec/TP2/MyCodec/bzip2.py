import bz2

def bzip(i,data):
    c = bz2.compress(data)
    f = open("data/"+i+".bzip2", "wb")
    f.write(c)
    f.close()
