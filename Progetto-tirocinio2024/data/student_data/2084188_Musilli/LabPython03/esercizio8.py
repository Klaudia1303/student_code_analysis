b=True
while b:
    s=input("Inserire una stringa per vedere se palindroma: ")
    if s[len(s)-1::-1]==s:
        print("Stringa palindroma di lunghezza",len(s))
        b=False
    else:   print("Stringa non palindroma.\n Inserire una stringa palindroma\n")
