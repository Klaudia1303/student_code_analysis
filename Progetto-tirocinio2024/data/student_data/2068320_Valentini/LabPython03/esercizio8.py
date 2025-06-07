palindroma=0
while palindroma<1:
    s=input("Inserire una stringa palindroma: ")
    s=s.casefold()
    s_inv=reversed(s)
    if list(s)==list(s_inv):
        palindroma = 1
    else:
        s=input("Non palindroma. Inserire una stringa palindroma: ")
lunghezza=len(s)
print("Stringa palindroma di lunghezza "+str(lunghezza)) 
