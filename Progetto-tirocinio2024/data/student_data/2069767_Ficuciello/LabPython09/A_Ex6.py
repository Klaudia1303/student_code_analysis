def A_Ex6(filename):
    f=open(filename,encoding="UTF-8")
    l=[]
    
    sv=[]
    somma1=0
    somma2=0
    somma3=0
    for riga in f:
        riga=riga.strip().split(",")
        sv.append(riga)
    for elem in range(1,len(sv)):
        somma1+=int(sv[elem][1])
        somma2+=int(sv[elem][2])
        somma3+=int(sv[elem][3])
    l.append((somma1,somma2,somma3))
    massimo=max(l)
    anno=[]
    if massimo==somma1:
        anno.append(sv[0][1])
    elif massimo==somma2:
        anno.append(sv[0][2])
    elif massimo==somma3:
        anno.append(sv[0][3])
    f.close()
    return str(anno)
        
 
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
