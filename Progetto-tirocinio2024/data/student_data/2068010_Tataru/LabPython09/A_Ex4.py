def A_Ex4(filename,anno):
    f=open(filename,encoding="UTF-8")
    s=f.readlines()
    for i in range(0,len(s)):
        s[i]=s[i].replace("\n","")
        for elem in '.,;:!?<>"-«»()\'':
            s[i]=s[i].replace(elem," ")
    ind=int()
    mx=0
    im=""
    for i in s:
        l=i.split()
        if (l[0]=="Anno"):
            for j in range(1,len(l)):
                if (l[j]==str(anno)):
                    ind=j
                    break
            continue
        if (int(l[ind])>mx):
            mx=int(l[ind])
            im=l[0]
        elif (int(l[ind])==mx and im<l[0]):
            mx=int(l[ind])
            im=l[0]
    return im
            


    
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, ['Vendite1.csv',2012] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2012] , 'Maglione')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2013] , 'Zaino')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2011] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2010] , 'Cellulare')
    
    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
