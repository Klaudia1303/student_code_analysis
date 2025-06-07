def A_Ex5(l):
    lista=[]
    lista_nuova=[]
    lista_finale=[]


    for parole in l:
        for caratteri in parole:
            numero=ord(caratteri)
            lista.append(numero)

        lista_nuova=[sum(lista)]
        lista_finale.append(lista_nuova)
        lista.clear()
    

    lista_def=[]
    for i in range(len(lista_finale)):
        lista_def=lista_def+lista_finale[i]
    
    return(lista_def)






















    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, [["ama","ma","amaca"]], [303,206,499])
    counter_test_positivi += tester_fun(A_Ex5, [[]], [])
    counter_test_positivi += tester_fun(A_Ex5, [["c"]], [99])
    counter_test_positivi += tester_fun(A_Ex5, [["ciao",""]], [412,0])
    counter_test_positivi += tester_fun(A_Ex5, [["",""]], [0,0])

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
