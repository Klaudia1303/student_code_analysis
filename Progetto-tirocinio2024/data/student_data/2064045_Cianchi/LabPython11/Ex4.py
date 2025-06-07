def Ex4(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(file,encoding='UTF-8')
    riga1=f.readline()
    d={}
    d2={}
    for riga in f:
        riga=riga.strip().split(',')
        if riga[0] not in d:
            d[riga[0]]=[]
            d[riga[0]].append(riga[1])
            d[riga[0]].append(riga[2])
        if riga[0] not in d2:
            d2[riga[0]]=[]
        if riga[0] in d and riga[1] in d[riga[0]][1]:
            d[riga[0]].remove(d[riga[0]][1])
            d[riga[0]].append(riga[2])
        if riga[0] in d and riga[1] in d2[riga[0]]:
            d[riga[0]].remove(d[riga[0]][1])
            d[riga[0]].append(riga[2])
            d2[riga[0]].remove(riga[1])
        if riga[0] in d and riga[1] in d[riga[0]][0] and riga[2] not in d:
            d2[riga[0]].append(d[riga[0]][1])
            d[riga[0]].remove(d[riga[0]][1])
            d[riga[0]].append(riga[2])
    return d
            
        
    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex4, ["eredita1.csv"] , {'Anello_di_smeraldi': ['Maria', 'Giorgia'], 'Anello': ['Silvia', 'Paolo']})
    counter_test_positivi += tester_fun(Ex4, ["eredita2.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Sergio']})
    counter_test_positivi += tester_fun(Ex4, ["eredita3.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Sergio'], 'Vaso': ['Anna', 'Sergio']})
    counter_test_positivi += tester_fun(Ex4, ["eredita4.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Giorgio'], 'Vaso': ['Anna', 'Anna']})
    counter_test_positivi += tester_fun(Ex4, ["eredita5.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Sergio'], 'Vaso': ['Sergio', 'Anna']})

    print('La funzione',Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
