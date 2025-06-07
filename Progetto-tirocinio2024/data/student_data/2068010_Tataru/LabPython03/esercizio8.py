while(True==True):
    s=input()
    if (s[0]==s[len(s)-1]):
        print("stringa palindroma di lunghezza "+str(len(s)))
        break
    print("non palindroma, inserire una stringa palindroma")
