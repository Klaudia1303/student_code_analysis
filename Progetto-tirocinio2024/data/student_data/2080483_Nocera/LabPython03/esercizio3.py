f=1
while f>0:

    l = int(input("scrivi un intero (se vuoi terminare il programma scrivi un numero divisibile per 5) :") )
    print (int(l))
    if l%5==0:
        print(int(l/5))
        f = 0