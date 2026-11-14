matn = "Python dasturlash qiziqarli. Python imkoniyatlari keng."


matn = matn.lower()
sozlar = matn.replace(".", "").split()
print("So'zlar soni:", len(sozlar))
eng_uzun = max(sozlar, key=len)
print("Eng uzun so'z:", eng_uzun)
harflar = {}

for harf in matn:
    if harf.isalpha():
        harflar[harf] = harflar.get(harf, 0) + 1

eng_kop_harf = max(harflar, key=harflar.get)
print("Eng ko'p uchragan harf:", eng_kop_harf)
takrorlanmaydigan = []

for soz in sozlar:
    if sozlar.count(soz) == 1:
        takrorlanmaydigan.append(soz)

print("Takrorlanmaydigan so'zlar:",
      ", ".join(takrorlanmaydigan))
