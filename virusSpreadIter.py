def virusSpread_iterative(N, P):
    for _ in range(N):
        P *= 2
    return P

N=int(input("enter the hours :"))
P=int(input("enter the computers :"))
print("Iterative:", virusSpread_iterative(N, P))
