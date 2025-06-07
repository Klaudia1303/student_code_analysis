base=int(input("Inserisci il valore della base di un triangolo isoscele:"))
n=base//2
for i in range(1,base+1,2):
    print(' '*n+'*'*i)
    n-=1
