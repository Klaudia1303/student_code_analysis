finito=False
while not finito:
    s=input("inserisci stringa: ")
    if s.islower()==False:
        print(s[0]+s[len(s)-1])
    elif s.isalpha()==False:
        print(s[0]+s[len(s)-1])
    else:
        print(s[0]+s[len(s)-1])
        print("fine")
        finito=True
              
