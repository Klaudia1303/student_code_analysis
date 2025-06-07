corretto= False
s=input()
i=0
while not corretto:
    if s.islower() and s.isalpha():
        

        corretto= True
    else :
        s=input()
print((s[0]),(s[len(s)-1]))

