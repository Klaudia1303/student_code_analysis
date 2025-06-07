c = str(input())
w= True
while w:
    s = str(input())
    s1= s.count(c)
    if s1>2:
        print(s.count(c))
        w= False