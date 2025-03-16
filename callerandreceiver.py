def callerNo(n):
    if n == 0:
        return
    print(f"Caller: Sentence {n}")
    receiverNo(n - 1)
    
def receiverNo(n):
    if n == 0:
        return
    print(f"Receiver: Sentence {n}")
    callerNo(n - 1)  


callerNo(5)
