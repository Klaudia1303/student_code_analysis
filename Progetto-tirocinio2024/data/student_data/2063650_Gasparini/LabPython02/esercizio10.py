eta_cane = float(input("Età del cane: "))
if eta_cane < 0:
    print("input non valido")
else:
    eta_umana = min(eta_cane, 2) * 10.5 + max(eta_cane - 2, 0) * 4
    print(eta_umana)
