x=int(input('inserire la base del triangolo isoscele: '))
f=' '
s=0
for i in range(1,x+1,2):
      spa=f*(x//2-s)
      s+=1
      carat='*'*i
      print(spa+carat)
