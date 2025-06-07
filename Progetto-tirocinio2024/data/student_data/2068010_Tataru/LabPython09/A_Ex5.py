def A_Ex5(filename,oggetto):
    f=open(filename,encoding="UTF-8")
    a=f.readline()
    s=f.readlines()
    a=a.replace("\n","")
    for elem in '.,;:!?<>"-«»()\'':
        a=a.replace(elem," ")
    for i in range(0,len(s)):
        s[i]=s[i].replace("\n","")
        for elem in '.,;:!?<>"-«»()\'':
            s[i]=s[i].replace(elem," ")
    mx="0"
    dm=0
    im=0
    for i in s:
        l=i.split()
        if (l[0]==oggetto):
            mx=l[1]
            im=1
            for j in range(2,len(l)):
                if (int(l[j])-int(mx)>dm):
                    im=j
                    mx=l[j]
                    dm=int(l[j])-int(mx)
        else:
            continue

    return int(a.split()[im]) 


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Giubbotto'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Zaino'] , 2010)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Maglione'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Zaino'] , 2013)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite3.csv','Giubbotto'] , 2013)

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
