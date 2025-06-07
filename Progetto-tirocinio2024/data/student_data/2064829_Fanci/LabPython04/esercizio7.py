s = input("inserisci stringa: ")
i=0
c=0
char=''
while i<len(s):
    cmax = s.count(s[i])
    if cmax>=c:
        c = cmax
        char= s[i]
    i = i+1
print(char)
