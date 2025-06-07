print("Inserire una sequenza di unemri interi")
i=False
while i==False:
    n=int(input())
    if n%5==0:
        ris=n/5
        ris=int(ris)
        print(ris)
        i=True
