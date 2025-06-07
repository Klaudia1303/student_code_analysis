
num = int(input('Inserire un numero'))

pen = 0
ult = 0
index = 1
count = 0
while(count <= num):
    
    valore = index + pen + ult
    print(valore)
    if(ult == 0):
        ult = 1
        index = 0
    else:
        pen = ult
        ult = valore

    count += 1
