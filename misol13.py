import csv

yonalish = input("Yonalish: ")

talabalar = []

with open("talabalar.csv", "r") as fayl:
    oqish = csv.DictReader(fayl)

    for talaba in oqish:
        if talaba["yonalish"].lower() == yonalish.lower():
            talabalar.append(talaba)

talabalar.sort(key=lambda x: int(x["ball"]), reverse=True)


with open("filtrlangan_talabalar.csv", "w") as fayl:
    ustunlar = ["ism", "yosh", "yonalish", "ball"]

    yozish = csv.DictWriter(fayl, fieldnames=ustunlar)
    yozish.writeheader()
    yozish.writerows(talabalar)

print(f"{len(talabalar)} ta talaba topildi. Natijalar filtrlangan_talabalar.csv fayliga yozildi.")
