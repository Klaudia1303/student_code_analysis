i=0
x=0
y=0
while not (x!=0 and y!=0):
    s=str(input("Inserisci una stringa: "))
    i=i+1
    x=s.count('a')
    y=s.count('c')
print(i)
