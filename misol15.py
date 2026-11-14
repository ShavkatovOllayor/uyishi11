import csv
import os
import matplotlib.pyplot as plt

FAYL = "kitoblar.csv"

def fayl_tekshir():
    if not os.path.exists(FAYL):
        with open(FAYL, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["nom", "kategoriya", "muallif", "oqilgan"])

def kitoblarni_oqish():
    fayl_tekshir()

    with open(FAYL, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def kitoblarni_korish():
    kitoblar = kitoblarni_oqish()

    if not kitoblar:
        print("Kutubxonada kitob yo'q!")
        return

    for kitob in kitoblar:
        print(
            f"{kitob['nom']} | "
            f"{kitob['kategoriya']} | "
            f"{kitob['muallif']} | "
            f"{kitob['oqilgan']} marta"
        )



def kitob_qidirish():
    nom = input("Kitob nomini kiriting: ").lower()

    kitoblar = kitoblarni_oqish()
    topildi = False

    for kitob in kitoblar:
        if nom in kitob["nom"].lower():
            print("Kitob topildi:")
            print(kitob)
            topildi = True

    if not topildi:
        print("Kitob topilmadi!")


def kategoriya_filtrlash():
    kategoriya = input("Kategoriyani kiriting: ").strip().lower()

    kitoblar = kitoblarni_oqish()
    topildi = False

    for kitob in kitoblar:
        if kitob["kategoriya"].strip().lower() == kategoriya:
            print(kitob)
            topildi = True

    if not topildi:
        print("Bu kategoriyada kitob topilmadi!")



def eng_kop_oqilgan():
    kitoblar = kitoblarni_oqish()

    if not kitoblar:
        print("Kitoblar mavjud emas!")
        return

    eng_kop = max(kitoblar, key=lambda x: int(x["oqilgan"]))

    print(
        f"Eng ko'p o'qilgan kitob: "
        f"{eng_kop['nom']} — {eng_kop['oqilgan']} marta"
    )



def kategoriya_grafik():
    kitoblar = kitoblarni_oqish()

    if not kitoblar:
        print("Grafik uchun ma'lumot yo'q!")
        return

    kategoriyalar = {}

    for kitob in kitoblar:
        kategoriya = kitob["kategoriya"].strip()

        kategoriyalar[kategoriya] = (
            kategoriyalar.get(kategoriya, 0) + 1
        )

    plt.bar(
        kategoriyalar.keys(),
        kategoriyalar.values()
    )

    plt.title("Kategoriyalar bo'yicha kitoblar")
    plt.xlabel("Kategoriyalar")
    plt.ylabel("Kitoblar soni")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.show()



def kitob_qoshish():
    nom = input("Kitob nomi: ").strip()
    kategoriya = input("Kategoriya: ").strip()
    muallif = input("Muallif: ").strip()

    try:
        oqilgan = int(input("O'qilgan soni: "))
        if oqilgan < 0:
            print("Son manfiy bo'lmasligi kerak!")
            return
    except ValueError:
        print("Iltimos, son kiriting!")
        return

    if not nom or not kategoriya or not muallif:
        print("Maydonlar bo'sh bo'lmasligi kerak!")
        return

    with open(FAYL, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([nom, kategoriya, muallif, oqilgan])

    print("Yangi kitob muvaffaqiyatli qo'shildi!")


def main():
    fayl_tekshir()

    while True:
        print("\n===== KUTUBXONA STATISTIKASI =====")
        print("1. Kitoblarni ko'rish")
        print("2. Kitob qidirish")
        print("3. Kategoriya bo'yicha filtrlash")
        print("4. Eng ko'p o'qilgan kitob")
        print("5. Grafik chiqarish")
        print("6. Yangi kitob qo'shish")
        print("0. Dasturdan chiqish")

        tanlov = input("Tanlov: ")

        if tanlov == "1":
            kitoblarni_korish()

        elif tanlov == "2":
            kitob_qidirish()

        elif tanlov == "3":
            kategoriya_filtrlash()

        elif tanlov == "4":
            eng_kop_oqilgan()

        elif tanlov == "5":
            kategoriya_grafik()

        elif tanlov == "6":
            kitob_qoshish()

        elif tanlov == "0":
            print("Dastur yakunlandi!")
            break

        else:
            print("Noto'g'ri tanlov!")


if __name__ == "__main__":
    main()
