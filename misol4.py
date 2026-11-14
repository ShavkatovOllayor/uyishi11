
ombor_1 = {"olma": 20, "anor": 12, "nok": 8}
ombor_2 = {"olma": 15, "banan": 10, "nok": 5}

natija = ombor_1.copy()

for mahsulot, miqdor in ombor_2.items():
    if mahsulot in natija:
        natija[mahsulot] += miqdor
    else:
        natija[mahsulot] = miqdor

print(natija)
