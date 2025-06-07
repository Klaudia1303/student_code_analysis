finito=False
while not finito:
        n=input('inserire un intero (divisibile per 5 per interrompere): ')
        n=int(n)
        if n%5==0:
            print(int(n/5))
            finito=True