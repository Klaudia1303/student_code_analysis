finito=False
s1=input("Inserisci stringa: ")
s2=input("Inserisci stringa: ")

cassetto3=0
cassetto1=s1
cassetto2=s2
while not finito:
    s3=input("Inserisci stringa: ")
    cassetto3=s3
    if len(cassetto1)+len(cassetto2)==len(cassetto3):
        print(str(cassetto1)+" "+str(cassetto2)+" "+str(cassetto3))
        finito=True
    else:
        cassetto1=cassetto2
        cassetto2=cassetto3

  
        
