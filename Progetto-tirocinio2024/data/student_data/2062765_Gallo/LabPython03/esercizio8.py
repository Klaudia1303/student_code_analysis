
finito=False
while not finito:
    s=input("inserire stringa palindroma: ")
    if not s[len(s):-len(s):-1]+s[0]==s: #vedere se è palindroma:
        print("non palindroma")
    else:
        print("Stringa palindroma di lunghezza: "+ str(len(s)))
        finito=True
