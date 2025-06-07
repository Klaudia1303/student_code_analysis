n=int(input("Inserisci intero maggiore di 0: "))
conta=0
cassetto1=0
cassetto2=1
cassetto3=0
while conta<n:
    print(cassetto2)
    cassetto3=cassetto1+cassetto2
    cassetto1=cassetto2
    cassetto2=cassetto3
    conta+=1
    
    
