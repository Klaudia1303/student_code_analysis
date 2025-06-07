def A_Ex8(file):
    
    dizionario = {}
    
    
    with open(file, encoding="UTF-8") as file:
        csv = file.read().replace(" ", "-").strip().split()
        csv.pop(0)
    
    for elem in csv:
        linea = elem.strip().split(",")
        
        
        Nome1 = linea[0]
        Nome2 = linea[1]
        relazione = linea[2]
        
        if Nome1 not in dizionario.keys():
            dizionario[Nome1] = list()
        if Nome2 not in dizionario.keys():
            dizionario[Nome2] = list()
        
        if relazione == "amici": 
            dizionario[Nome1].append(Nome2)
            dizionario[Nome2].append(Nome1)
        else:
            if Nome2 in dizionario[Nome1]: dizionario[Nome1].remove(Nome2)
            if Nome1 in dizionario[Nome2]: dizionario[Nome2].remove(Nome1)

    for elem in dizionario.copy():
        
       
        dizionario[elem] = list(set(dizionario[elem]))
        dizionario[elem].sort()
        
    
    return dizionario
    
    
    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex8, ["amici1.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna'], 'Giorgio': []})
    counter_test_positivi += tester_fun(A_Ex8, ["amici2.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria'], 'Maria': ['Anna'], 'Paola': [], 'Giorgio': []})
    counter_test_positivi += tester_fun(A_Ex8, ["amici3.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna'], 'Giorgio': []})
    counter_test_positivi += tester_fun(A_Ex8, ["amici4.csv"] , {'Marco': ['Giorgio', 'Paolo'], 'Giorgio': ['Marco'], 'Paolo': ['Marco'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna']})
    counter_test_positivi += tester_fun(A_Ex8, ["amici5.csv"] , {'Marco': [], 'Giorgio': [], 'Paola': [], 'Anna': []})

    print('La funzione',A_Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
