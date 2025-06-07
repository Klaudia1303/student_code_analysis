s= input('stringa: ')
x=0
dis= 0
dis1= 0

for i in range(len(s)):
    if s.count(s[x])>1:
        pos1= s.find(s[x])
        pos2= s.rfind(s[x])
        dis1 = dis
        dis= pos2 - pos1
        x= x+1
if dis > dis1:
    print(dis)
else:
    print(dis)
