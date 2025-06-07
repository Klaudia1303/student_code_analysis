b = int(input("inserisci base triangolo: "))
if b%2==0 or b<3: print("impossibile stamapre il triangolo")
else:
    for i in range(1,b+1,2):
        t=int((b-i)/2)
        print((" "*t)+("*"*i)+(" "*t))
    
