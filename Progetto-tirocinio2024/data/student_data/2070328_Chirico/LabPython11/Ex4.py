def Ex4(file):
    import re
    x = open(file,'r',encoding = 'UTF-8')
    z = open(file,'r',encoding = 'UTF-8')
    xx = x.readline()
    zz = z.readline()
    z = z.read()
    d = {}


    for i in x:
        j = i.strip().split(',')
        if j[0] not in d:
            d[j[0]] = [j[1]]
            oggetto = j[0]
            erede = d[j[0]][0]
            pattern = r'^'+oggetto+',(\w*,\w*)$'
            a = re.findall(pattern, z, flags = re.MULTILINE)

            for k in a:
                k = k.strip().split(',')
                if erede == k[0]:
                    erede = k[1]
            d[j[0]].append(erede)
            
    x.close()
    return d
                


    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
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
