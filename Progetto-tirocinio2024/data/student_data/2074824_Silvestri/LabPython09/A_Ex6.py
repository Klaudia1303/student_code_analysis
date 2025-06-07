def A_Ex6(filename):
    anno = 2010
    lista = []
    kLista = []
    with open(filename, encoding="UTF-8") as file:
        csv = file.readlines()
        kAnno = csv[0].strip().split(",")
        
        for k in range(1,len(csv)):
            lista.append(csv[k].strip().split(","))
            
        
        
        for i in range(1,len(lista[0])):
            countVendite = 0
            for j in range(len(lista)):
                countVendite += int(lista[j][i])
                
            kLista.append((kAnno[i], countVendite))
    
    print(kLista)
    maxVendite = 0
    for elem in kLista:
        
        if elem[1] >= maxVendite:
            
            anno = elem[0]
            maxVendite = int(elem[1])
            
    return int(anno)
    
 
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
