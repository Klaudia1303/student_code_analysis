def A_Ex7(file):
    
    dizionario = {}
    lista = []
    
    with open(file, encoding="UTF-8") as file:
        csv = file.read().replace(" ", "-").strip().split()
        csv.pop(0)
    
    for elem in csv:
        linea = elem.strip().split(",")
        
        squadra1 = {"Nome": linea[0], "Risultato": int(linea[2])}
        squadra2 = {"Nome": linea[1], "Risultato": int(linea[3])}
        print(squadra1,squadra2)
        
        if squadra1["Nome"] not in dizionario.keys():
            dizionario[squadra1["Nome"]] = 0
        if squadra2["Nome"] not in dizionario.keys():
            dizionario[squadra2["Nome"]] = 0
        
        if squadra1["Risultato"] == squadra2["Risultato"]:
            dizionario[squadra1["Nome"]] += 1
            dizionario[squadra2["Nome"]] += 1
        elif squadra1["Risultato"] > squadra2["Risultato"]:
            dizionario[squadra1["Nome"]] += 3
        else:
            dizionario[squadra2["Nome"]] += 3
    
    return dizionario
            
    

 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex7, ["partite1.csv"] , {'Chelsea': 3, 'Everton': 3, 'Arsenal': 4, 'Tottenham': 1})
    counter_test_positivi += tester_fun(A_Ex7, ["partite2.csv"] , {'Chelsea': 4, 'Everton': 6, 'Arsenal': 4, 'Tottenham': 2})
    counter_test_positivi += tester_fun(A_Ex7, ["partite3.csv"] , {'Bayern': 4, 'Schalke': 3, 'Amburgo': 4, 'Werder': 1, 'Colonia': 4, 'Stoccarda': 0})
    counter_test_positivi += tester_fun(A_Ex7, ["partite4.csv"] , {'Bayern': 8, 'Schalke': 6, 'Amburgo': 8, 'Werder': 2, 'Colonia': 8, 'Stoccarda': 0})
    counter_test_positivi += tester_fun(A_Ex7, ["partite5.csv"] , {'Bayern': 5, 'Schalke': 6, 'Amburgo': 5, 'Werder': 5, 'Colonia': 5, 'Stoccarda': 6})

    print('La funzione',A_Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
