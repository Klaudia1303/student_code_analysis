s=input("Inserire una stringa: ")
n=len(s)
s1=""
while n>0:
    s1=s1+s[n-1]
    n-=1
while s1!=s:
    print("non palindroma, inserire una stringa palindroma")
    s=input("Inserire una stringa: ")
    s1=""
    n=len(s)
    while n>0:
        s1=s1+s[n-1]
        n-=1
print("stringa palindroma di lunghezza ",len(s))
