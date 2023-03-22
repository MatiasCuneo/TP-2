setup = [
    {"procesador":"i7 11700k","ram":"fury 3260 Mb","gpu":"RTX 3070Ti","price":1699},
    {"procesador":"ryzen 9 5900X","ram":"fury 3260 Mb","gpu":"Radeon Rx6500","price":1899},
    {"procesador":"ryzen 7 5700G","ram":"HyperX 16 GB","gpu":"Radeon Rx6500","price":1199},
    {"procesador":"i5 10400F","ram":"HyperX 8 GB","gpu":"RTX 2060","price":1099}
]

def findRam(lista):
    pcs = []

    for i in lista:
        ram = i["ram"].split()
        ram_val = int(ram[-2])
        if ram_val > 1000:
            if ram_val > 8000:
                pcs.append(str(ram_val) + "Mb ")
        else:
            if ram_val > 8:
                pcs.append(str(ram_val) + "GB ")

    total = f"Las PCs con mas de 8GBs de RAM contienen: {...pcs}"

    return total
