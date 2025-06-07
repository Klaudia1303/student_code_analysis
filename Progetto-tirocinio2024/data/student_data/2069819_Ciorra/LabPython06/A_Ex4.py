pr = int(input())
se = int(input())
for i in range(1000):
    print("giorno: ",i, "||| distanza tra i due:", pr-se)
    se+=1
    if pr-se==0:
        print ("i due viaggiatori si sono incontrati il giorno ",i)
        break
