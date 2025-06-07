x=1
t=input("inserie una stringa: ")
y=int(len(t)-1)
while x!=0:
    s=input("inserire stringa: ")
    if s[:1]==t[y:]:
        print(s,t)
        x=0
    t=s
    y=int(len(t)-1)
