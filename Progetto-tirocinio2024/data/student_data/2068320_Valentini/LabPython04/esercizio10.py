lun_n1=1
lun_n2=1
lun_n3=3
n1=str(input("Inserire una stringa: "))
n2=str(input("Inserire una stringa: "))
while lun_n1+lun_n2 != lun_n3:
    n3=str(input("Inserire una stringa: "))
    lun_n1=len(n1)
    lun_n2=len(n2)
    lun_n3=len(n3)
    if lun_n1+lun_n2 == lun_n3:
        print(n1 +" "+n2+ " "+n3)
        break
    n1 = n2
    n2 = n3
