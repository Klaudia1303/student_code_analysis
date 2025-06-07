x=int(input("inserisci intero compreso tra 0 e 10: "))
y=int(input("inserisci intero compreso tra 0 e 10: "))
if 0<=x<=10:
    if 0<=y<=10:
        n=int(0)
    while n<=10:
        if x!=n:
            if y!=n:
                print(n)
                n+=1
            else:
                n+=1
        else:
            n+=1
        
        
