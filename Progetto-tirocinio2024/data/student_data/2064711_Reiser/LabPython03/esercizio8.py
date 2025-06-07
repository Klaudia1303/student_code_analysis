c=True
while c==True:
    s = input("inserire una stringa palindroma:")
    if str(s) == str(s)[::-1] :
        print("stringa palindroma di lunghezza",len(s))
        c=False
    else:
        print("stringa non palindroma")
