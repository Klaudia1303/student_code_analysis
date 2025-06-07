s=input()
s1=input()
corretto= False
while not corretto:
    if s1[0]==s[len(s)-1] or s[0]==s1[len(s1)-1]:
        print (s,s1)
        corretto=True
    s=input()
    s1=input()
        
