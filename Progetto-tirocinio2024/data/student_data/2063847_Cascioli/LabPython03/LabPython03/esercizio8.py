palindroma=False
while not(palindroma):
    s=input("Inserire una stringa palindroma: ")
    if (s[-1]==s[0]):
        palindroma=True
    else:
        print("stringa non palindroma reinserire")
print("stringa palindroma di lunghezza", len(s))
