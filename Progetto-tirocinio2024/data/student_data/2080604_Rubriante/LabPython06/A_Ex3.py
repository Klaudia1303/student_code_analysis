n1=0
n2=0
ris=0
for i in range(1,9):
    for j in range(1,9):
        ris=i*j
        if ris>=8:
            ris=str(ris//8)+str(ris%8)
        else:
            ris="0"+str(ris)
        if i>=8:
            n1=str(i//8)+str(i%8)
        else:
            n1="0"+str(i)
        if j>=8:
            n2=str(j//8)+str(j%8)
        else:
            n2="0"+str(j)
        if int(ris)>=80:
            ris=str(int(ris)//80)+str(int(ris)%8)+str(int(ris)%8)
        print(n1+"*"+n2+"="+ris)
