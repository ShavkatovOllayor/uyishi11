
tadbir_1 = {"Ali", "Vali", "Sami", "Lola"}
tadbir_2 = {"Ali", "Sami", "Nodir"}
tadbir_3 = {"Ali", "Lola", "Nodir"}

barcha = tadbir_1 & tadbir_2 & tadbir_3
hamma = tadbir_1 | tadbir_2 | tadbir_3

faqat_bitta = set()

for ism in hamma:
    soni = (
        (ism in tadbir_1) +
        (ism in tadbir_2) +
        (ism in tadbir_3)
    )

    if soni == 1:
        faqat_bitta.add(ism)

kamida_ikkita = set()

for ism in hamma:
    soni = (
        (ism in tadbir_1) +
        (ism in tadbir_2) +
        (ism in tadbir_3)
    )

    if soni >= 2:
        kamida_ikkita.add(ism)

print("Barcha tadbirlarda:", ", ".join(sorted(barcha)))
print("Faqat bitta tadbirda:", ", ".join(sorted(faqat_bitta)))
print("Kamida ikkita tadbirda:", ", ".join(sorted(kamida_ikkita)))
