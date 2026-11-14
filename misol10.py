with open("ish_vaqti.txt", "r") as fayl:
    malumot = fayl.read().split()

jami_soat = 0
xodimlar = {}

for i in range(0, len(malumot), 2):
    ism = malumot[i]
    soat = malumot[i + 1]

    try:
        soat = int(soat)
        jami_soat += soat
        xodimlar[ism] = soat

    except ValueError:
        print(f"Ogohlantirish: {ism} uchun soat qiymati noto'g'ri.")

eng_kop = max(xodimlar, key=xodimlar.get)

print("Jami ish soati:", jami_soat)
print(f"Eng ko'p ishlagan: {eng_kop} — {xodimlar[eng_kop]} soat")