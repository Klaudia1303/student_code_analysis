n=int(input("Inserire un numero intero positivo maggiore di 1:"))
i=2
while i<=n:
    j=2
    primo=True
    while j<i and primo:
        if i%j==0:
            primo=False
        else:
            j=j+1
    if primo:
        print(i)
    i=i+1












    
