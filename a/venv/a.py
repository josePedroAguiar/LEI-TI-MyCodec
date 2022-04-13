bin8 = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(8)] ) )
print ("char-"+chr(int(bin8((0)))))