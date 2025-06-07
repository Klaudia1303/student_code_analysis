def Ex8(file):
    import re
    f = open(file,encoding="UTF-8")
    l = []
    for e in f:
        e = e.strip().split("\n")
        l.append(e)
    f.close()

    l2 = []
    for i in range(len(l)):
        for j in range(len(l[i])):
            l2.append(l[i][j])

    l3 = []
    for i in range(len(l2)):
        p = r"[A-Z][A-Z][A-Z] *[A-Z][A-Z][A-Z] *[0-9][0-9][A-Z][0-9][0-9] *[A-Z][0-9][0-9][0-9][A-Z]"
        if re.match(p,l2[i]) and len(re.match(p,l2[i]).group()) == len(l2[i]):
            l3.append(l2[i])
        else:
            l3.append("Codice errato")
    l4 = []
    d = {"A":"01","B":"02","C":"03","D":"04","E":"05","H":"06","L":"07","M":"08","P":"09","R":"10","S":"11","T":"12"}
    for i in range(len(l3)):
        if l3[i] == "Codice errato":
            l4.append(l3[i])
        for j in range(len(l3[i])):
            if l3[i][j] in "0123456789":
                
                if int(l3[i][j]+l3[i][j+1]) > 20:
                    a = "19"+l3[i][j]+l3[i][j+1]
                else:
                    a = "20"+l3[i][j]+l3[i][j+1]

                if l3[i][j+2] in "ABCDEHLMPRST":
                    m = d[l3[i][j+2]]
                else:
                    l4.append("Mese errato")
                    break

                if int(l3[i][j+3]+l3[i][j+4]) > 40:
                    gp = int(l3[i][j+3]+l3[i][j+4]) - 40
                    if l3[i][j+2] in "DHPS":
                        if gp <= 30:
                            g = str(gp)
                        else:
                            l4.append("Giorno errato")
                            break
                    elif l3[i][j+2] == "B":
                        if gp <= 28:
                            g = str(gp)
                        else:
                            l4.append("Giorno errato")
                            break
                    else:
                        if gp <= 31:
                            g = str(gp)
                        else:
                            l4.append("Giorno errato")
                            break
                else:
                    gp = int(l3[i][j+3]+l3[i][j+4])
                    if l3[i][j+2] in "DHPS":
                        if gp <= 30:
                            g = str(gp)
                        else:
                            l4.append("Giorno errato")
                            break
                    elif l3[i][j+2] == "B":
                        if gp <= 28:
                            g = str(gp)
                        else:
                            l4.append("Giorno errato")
                            break
                    else:
                        if gp <= 31:
                            g = str(gp)
                        else:
                            l4.append("Giorno errato")
                            break
                if len (g) == 1:
                    g = "0"+g
                l4.append(g+"/"+m+"/"+a)
                break
    r = []
    for i in range(len(l4)):
        if l4[i] not in r:
            r.append(l4[i])
        elif "errato" in l4[i]:
            r.append(l4[i])
        else:
            continue
    return r
    






    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex8, ["codici1.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici2.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici3.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921'])
    counter_test_positivi += tester_fun(Ex8, ["codici4.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931'])
    counter_test_positivi += tester_fun(Ex8, ["codici5.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931', 'Codice errato', 'Giorno errato'])

    print('La funzione',Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
