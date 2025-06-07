n1=int(input("inserire il primo numero:")) 
n2=int(input("inserire secondo numero:"))
risultato=[n1]
k=0
for i in range (1,n2):
    risultato[len(risultato)-1]=int(risultato[len(risultato)-1])+n1
    risultato[len(risultato)-1]=str(risultato[len(risultato)-1])
    for y in range (0, len(risultato)):
        if int(risultato[len(risultato)-y-1])>7:
            k=int(risultato[len(risultato)-y-1])-8
            risultato[len(risultato)-y-1]=k
            if risultato[0]==k:
                risultato.insert(0,1)
            else:
                risultato[0]=int(risultato[0])+1
for i in range (0,len(risultato)):
    print(int(risultato[i]), end="")
