viaggiatore1=20
viaggiatore2=0
for i in range(1,1002):
    viaggiatore1=20*i
    viaggiatore2=viaggiatore2+i
    if int(viaggiatore2)>=int(viaggiatore1):
        print(i)
        break
    
    
