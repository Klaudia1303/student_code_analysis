side=int(input('insert a number: '))
inside=False
spaceMid=side-4
spaceSide=0
if side==1:
    print('*')
elif side%2==0:
    for counter in range(0,side+1):
        if counter==0 or counter==side:
            print('*'*side)
        else:
            if inside==False:
                for inside in range(0,int(((side)/2)-1)):
                    print('*'+' '*spaceSide+'*'+' '*spaceMid+'*'+' '*spaceSide+'*')
                    spaceMid-=2
                    spaceSide+=1
                spaceMid=0
                spaceSide=int((side-4)/2)
                for inside in range(int(((side)/2)+1),side):
                    print('*'+' '*spaceSide+'*'+' '*spaceMid+'*'+' '*spaceSide+'*')
                    spaceMid+=2
                    spaceSide-=1
            inside=True
else:
    for counter in range(0,side+1):
        if counter==0 or counter==side:
            print('*'*side)
        else:
            if inside==False:
                for inside in range(0,int(((side)/2)-1)):
                    print('*'+' '*spaceSide+'*'+' '*spaceMid+'*'+' '*spaceSide+'*')
                    spaceMid-=2
                    spaceSide+=1
                print('*'+' '*spaceSide+'*'+' '*spaceSide+'*')
                spaceMid=1
                spaceSide=int((side-4)/2)
                for inside in range(int(((side)/2)+2),side):
                    print('*'+' '*spaceSide+'*'+' '*spaceMid+'*'+' '*spaceSide+'*')
                    spaceMid+=2
                    spaceSide-=1
            inside=True