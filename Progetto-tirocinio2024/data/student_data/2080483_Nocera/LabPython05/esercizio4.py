n1=int(input("inserisci un numero min:"))
n2=int(input("inserisci un numero max"))
finito=True
i=1
    
if n1<=n2:
       while finito:
           multipli=n1*i
           i+=1
           if multipli<n2:
               print(multipli)
           else:
               finito=False
           
    
else:
    print("il numero",n1,"è piu grande di",n2)
       
