base=int(input("Inserire la base del triangolo isoscele: "))
num=base//2
num2=1
for i in range(num+1):
    print((' '*num+'*'*num2))
    num=num-1
    num2=num2+2
