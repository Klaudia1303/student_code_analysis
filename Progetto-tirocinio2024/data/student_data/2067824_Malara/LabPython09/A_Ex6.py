def A_Ex6(filename):
    f=open(filename,'r',encoding='UTF-8')
    rigaAnni=f.readline()
    rigaAnni=rigaAnni.strip().split(',')
    contatore=[0 for a in range((len(rigaAnni)))]
    for riga in f:
        riga=riga.strip().split(',')
        i=1
        while i<len(riga):
            contatore[i]=contatore[i]+int(riga[i])
            i+=1
    indiceAnnoMax=contatore.index(max(contatore))
    if contatore.count(max(contatore))>1:
        cercaInA=contatore.count(max(contatore))-1
        while cercaInA==0:
            slicing=contatore[contatore.index(max(contatore)+1):]
            indiceAnno=slicing.index(max(contatore))
            cercaInA-=1
    else:   
        indiceAnnoMax=contatore.index(max(contatore))
    
    return int(rigaAnni[indiceAnnoMax])
        
 
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
