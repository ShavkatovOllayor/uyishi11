import math

shaharlar = {
    "A": (0, 0),
    "B": (3, 4),
    "C": (6, 0)
}

def masofa(a, b):
    x1, y1 = a
    x2, y2 = b

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

eng_uzoq = 0
eng_uzoq_juftlik = ()

nomlar = list(shaharlar.keys())

for i in range(len(nomlar)):
    for j in range(i + 1, len(nomlar)):
        a = nomlar[i]
        b = nomlar[j]

        natija = masofa(shaharlar[a], shaharlar[b])

        print(f"{a} va {b}: {natija}")

        if natija > eng_uzoq:
            eng_uzoq = natija
            eng_uzoq_juftlik = (a, b)

print(
    f"Eng uzoq yo'nalish: {eng_uzoq_juftlik[0]} — "
    f"{eng_uzoq_juftlik[1]} ({eng_uzoq})"
)