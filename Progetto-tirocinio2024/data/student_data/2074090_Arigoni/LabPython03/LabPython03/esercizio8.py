finito= True


while finito:
    s=input("Scrivi una stringa e scopri se si tratta di una stringa palindroma>> ")
    if s==s[::-1]:
        print("Si tratta di una stringa palindroma")
        finito=False
        else:
            print("Non si tratta di una stringa palindroma")

    
