
for i in range (1,11):
    for j in range(1, 11):
        val = str(oct(i*j))
        print(val[1:].replace("o", "0"), end ="\t")
    print()
