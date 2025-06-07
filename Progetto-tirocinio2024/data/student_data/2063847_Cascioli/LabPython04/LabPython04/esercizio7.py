s=input("Inserisci la stringa: ")
i=0
magg=0
p_max=0
while(i<len(s)):
    if(s.count(s[i])>magg and s.rfind(s[i])>p_max):
        p_max=s.rfind(s[i])
        magg=s.count(s[i])
    elif(s.count(s[i])==magg):
        if(s.rfind(s[i])>p_max):
            p_max=s.rfind(s[i])
    i+=1
print(s[p_max])
