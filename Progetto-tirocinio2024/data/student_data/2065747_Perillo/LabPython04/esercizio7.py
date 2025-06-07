s=input("inserire una stringa")
a=0
b=0
while a<len(s) :
    if s.count(s[a])>=b:
        b=s.count(s[a])
        carattere=s[a]
    a+=1
print(carattere)
