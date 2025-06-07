def Ex8(file):
     f = open(file)
     r = f.readlines()
     lista = []
     for i in r:
         pattern = r"[A-Z]{3}\s*[A-Z]{3}\s*([0-9]{2})([A-Z])([0-9]{2})\s*[A-Z][0-9]{3}[A-Z]"
         match = re.search(pattern, i)
         if match:
             if 1 <= int(match.group(3)) <= 31 or 41 <= int(match.group(3)) <= 71:
                 if match.group(2) in "SDHPBACELMRT":
                      if match.group(2) in "SDHP" and (1 <= int(match.group(3)) <= 30 or 41 <= int(match.group(3)) <= 70):
                          if match.group(2) == "S":
                              mese = "11"
                          elif match.group(2) == "D":
                              mese = "04"
                          elif match.group(2) == "H":
                               mese = "06"
                          elif match.group(2) == "P":
                              mese == "07"
                          if 1 <= int(match.group(3)) <= 30:
                              giorno = match.group(3)
                          else:
                              giorno = str(int(match.group(3)) - 40)
                          if len(giorno) == 1:
                              giorno = "0" + giorno 
                          if int(match.group(1)) <= 20:
                              anno = "20" + match.group(1)
                              lista.append(giorno + "/" + mese + "/" + anno)
                          else:
                              anno = "19" + match.group(1)
                              lista.append(giorno + "/" + mese + "/" + anno)
                      elif match.group(2) in "B" and (1 <= int(match.group(3)) <= 28 or 41 <= int(match.group(3)) <= 68):
                          if match.group(2) == "B":
                              mese = "02"
                          if 1 <= int(match.group(3)) <= 30:
                              giorno = match.group(3)
                          else:
                              giorno = str(int(match.group(3)) - 40)
                          if len(giorno) == 1:
                              giorno = "0" + giorno 
                          if int(match.group(1)) <= 20:
                              anno = "20" + match.group(1)
                              lista.append(giorno + "/" + mese + "/" + anno)
                          else:
                              anno = "19" + match.group(1)
                              lista.append(giorno + "/" + mese + "/" + anno)
                      elif match.group(2) in "ACELMRT" and (1 <= int(match.group(3)) <= 31 or 41 <= int(match.group(3)) <= 71):
                          if match.group(2) == "A":
                              mese = "01"
                          elif match.group(2) == "C":
                              mese = "03"
                          elif match.group(2) == "E":
                               mese = "05"
                          elif match.group(2) == "L":
                              mese == "06"
                          elif match.group(2) == "M":
                              mese == "08"
                          elif match.group(2) == "R":
                              mese == "10"
                          elif match.group(2) == "T":
                              mese == "12"
                          if 1 <= int(match.group(3)) <= 30:
                              giorno = match.group(3)
                          else:
                              giorno = str(int(match.group(3)) - 40)
                          if len(giorno) == 1:
                              giorno = "0" + giorno  
                          if int(match.group(1)) <= 20:
                              anno = "20" + match.group(1)
                              lista.append(giorno + "/" + mese + "/" + anno)
                          else:
                              anno = "19" + match.group(1)

                              lista.append(giorno + "/" + mese + "/" + anno)

                      if match.group(2) in "ACELMRT" and (31 < int(match.group(3)) < 71 or int(match.group(3)) > 71):
                           lista.append("Giorno errato")
                      elif match.group(2) in "B" and (28 < int(match.group(3)) < 68 or int(match.group(3)) > 68):
                           lista.append("Giorno errato")
                      elif match.group(2) in "SDHP" and (30 < int(match.group(3)) > 70 or int(match.group(3)) > 70):
                           lista.append("Giorno errato")        
                 else:
                    lista.append("Mese errato")
             else:
                  lista.append("Giorno errato")
         else:
             lista.append("Codice errato")
     return lista
     
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
