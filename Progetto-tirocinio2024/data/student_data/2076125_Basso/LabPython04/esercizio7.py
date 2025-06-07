
s=input("Inserire una stringa:\t")
a=0
M=0

while a < len(s):
    b=s[a]
    conta2= s.count(b)
    M=max(M,conta2)
    a = a+1


a=len(s)-1

while a < len(s):
    b=s[a]
    if M == s.count(b):
        print(b)
        a=len(s)+1
    a=a-1



