

x = int(input("inserisci un intero compresso tra 0 e 10: "))
y = int(input("inserisci un intero compresso tra 0 e 10: "))
if 0<=x<=10 and 0<=y<=10:
    i=0
    while i<=10:

        if(i!=x and i!=y):
            print(i)
        i = i + 1


else :print("gli/l'intero inserito non è compresso tra 0 e 10")
