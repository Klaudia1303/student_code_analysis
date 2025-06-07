number=int(input('insert a number: '))
times=int(input('insert a number: '))
total=0
if times>=0:
    for sum in range(0,times):
        total+=number
    print(total)
if times<0:
    for sum in range(times,0):
        total-=number
    print(total)
