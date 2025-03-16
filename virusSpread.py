def virusSpread(N,P):
    if(N==0):
        return P
    else:
        return P+virusSpread(N-1,P*2)
N=int(input("enter the hours :"))
P=int(input("enter the computers :"))
print(virusSpread(N,P))