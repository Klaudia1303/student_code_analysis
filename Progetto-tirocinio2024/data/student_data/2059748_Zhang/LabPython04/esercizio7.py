s=input("scrivi una stringa: ")
i=0
n=0

while i<len(s):
    s.count(s[i])
    if s.count(s[i])>=n:
        n=s.count(s[i])
        x=s[i]
    i+=1

print(x)
