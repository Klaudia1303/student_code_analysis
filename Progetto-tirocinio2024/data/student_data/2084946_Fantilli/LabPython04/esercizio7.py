s = input()
i=0
c1 = s[i:i+1]
c2 = s[i+1:i+2]
while i<len(s):
    i+=1
if s.count(c1)>s.count(c2):
    print(c1)
elif s.count(c1)<s.count(c2):
    print(c2)
elif s.count(c1)==s.count(c2) and s.rfind(c1)>s.rfind(c2):
    print(c2)
elif s.count(c1)==s.count(c2) and s.rfind(c1)<s.rfind(c2):
    print(c1)
