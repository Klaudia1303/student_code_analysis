def A_Ex6(filename):
    a=open(filename,encoding="utf-8")
    casa=a.readline()
    casa=casa.strip().split(",")
    casa.remove(casa[0])
    b=[]
    risultato=0
    somma=0
    for riga in a:
        riga=riga.strip().split(",")
        riga.remove(riga[0])
        b.append(riga)
    for i in range(len(casa)):
        for oggetto in b:
              for costo in range(len(oggetto)):
                  if costo==i:
                      somma=somma+int(oggetto[costo])
        if somma>=risultato:
            risultato=somma
            annoVero=i
        somma=0
    return(int(casa[annoVero]))
              
               
            
 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, ['Vendite1.csv'] , 2010)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite2.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite3.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite4.csv'] , 2020)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite5.csv'] , 2022)

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
