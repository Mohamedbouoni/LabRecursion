def pascal(n, k):
    if k == 0 or k == n:
        return 1
    return pascal(n - 1, k - 1) + pascal(n - 1, k)

def print_pascal(n, row=0):
    if row == n:
        return
    
    line = "".join(str(pascal(row, k)) for k in range(row + 1))
    print(line)
    
    print_pascal(n, row + 1)
n=int(input("enter number :"))
print(print_pascal(n))