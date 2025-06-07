s=input("inserici stringa")
len(s)
somma=0
x=0
y=''
while somma<len(s):
    s.count(s[somma])
    if x<=s.count(s[somma]) :
        y=s[somma]
        x=s.count(s[somma])
    somma=somma+1
print(y)

    

