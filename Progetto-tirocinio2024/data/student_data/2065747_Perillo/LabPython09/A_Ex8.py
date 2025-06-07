def A_Ex8(fileName):
    fin=open(fileName,encoding="utf-8")
    c="casa"
    casa=True
    maiuscole=0
    risultato=0
    indice=1
    indiceVero=1
    while casa:
        c=fin.read(1)
        if c=="\n" or c=="":
            if maiuscole>=risultato:
                indiceVero=indice
                risultato=maiuscole
            maiuscole=0
            indice+=1
        if c.isupper():
            maiuscole+=1
        if c=="":
            casa=False
    return(indiceVero)
 
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
