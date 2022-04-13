bin8 = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(8)] ) )
import collections


def get_key(org, val):
    for key, value in org.items():
        if val == value:
            return key
def filtering(data,type=0):
    s=[]
    if type==0:
        counts =  collections.Counter(data)
        m=max(counts.values())
        m = get_key(counts, m)
        for i in data:
            if (i - m < 0):
                s.append(chr(int(bin8((i - m)), 2)))
            else:
              s.append(chr(int(bin8(i - m), 2)))
    elif type==1:
        m=127
        for i in data:
            if (i-m<0):
                s.append(chr(int(bin8((i-m)),2)))
            else:
                s.append(chr(int(bin8(i-m),2)))
    else:
        m=0
        for i in data:
            if (i - m < 0):
                s.append(chr(int(bin8((i - m)), 2)))
            else:
                s.append(chr(int(bin8(i - m), 2)))
            m=i
    data1=[]
    data1.append(m)
    for i in s:
        data1.append(ord(i))
    newFileByteArray = bytearray(data1)
    return newFileByteArray