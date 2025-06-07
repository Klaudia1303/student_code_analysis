def A_Ex8(fileName):
    f=open(fileName,encoding="UTF-8")
    frasi=[]
    for riga in f:
        frasi.append(riga.replace('\n','').split(' '))
    f.close()
    cont2=0
    indice=0
    for frase in range(0,len(frasi)):
        cont=0
        for parola in frasi[frase]:
            for lettera in parola:
                if lettera.isupper():
                    cont+=1
        if cont>=cont2:
            cont2=cont
            indice=frase+1
    return indice
 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex8, ["file1.txt"] , 2)
    counter_test_positivi += tester_fun(A_Ex8, ["file2.txt"] , 2)
    counter_test_positivi += tester_fun(A_Ex8, ["file3.txt"] , 2)
    counter_test_positivi += tester_fun(A_Ex8, ["file4.txt"] , 3)
    counter_test_positivi += tester_fun(A_Ex8, ["file5.txt"] , 3)

    print('La funzione',A_Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
