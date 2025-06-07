anno=input("Inserire un anno: ")
bis=int(anno)%4
if bis==0:
    print("Anno bisestile")
else:
    print("Anno non bisestile")
