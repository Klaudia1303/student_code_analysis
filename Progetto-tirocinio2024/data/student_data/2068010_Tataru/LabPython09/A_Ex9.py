def A_Ex9(fileName,squadra):
    f=open(fileName,encoding="UTF-8")
    s=f.readline()
    s=f.readlines()
    for i in range(0,len(s)):
        s[i]=s[i].replace("\n","")
        for elem in '.,;:!?<>"-«»()\'':
            s[i]=s[i].replace(elem," ")
    c=0
    for i in s:
        l=i.split()
        if (l[0]==squadra):
            if(l[2]>l[3]):
                c+=3
            elif(l[2]==l[3]):
                c+=1
        elif (l[1]==squadra):
            if(l[3]>l[2]):
                c+=3
            elif(l[2]==l[3]):
                c+=1
    return c
    
    
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex9, ["partite1.csv",'Chelsea'] , 3)
    counter_test_positivi += tester_fun(A_Ex9, ["partite1.csv",'Tottenham'] , 1)
    counter_test_positivi += tester_fun(A_Ex9, ["partite2.csv",'Arsenal'] , 4)
    counter_test_positivi += tester_fun(A_Ex9, ["partite2.csv",'Bayern'] , 0)
    counter_test_positivi += tester_fun(A_Ex9, ["partite3.csv",'Bayern'] , 4)

    print('La funzione',A_Ex9.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
