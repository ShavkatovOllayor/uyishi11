def bolish(a, b):
    assert b != 0, "Ikkinchi son nol bo'lmasligi kerak!"
    return a / b


try:
    son1 = float(input("Birinchi son: "))
    son2 = float(input("Ikkinchi son: "))

    natija = bolish(son1, son2)
    print("Natija:", natija)

except ValueError:
    print("Xato! Son o'rniga matn kiritdingiz.")

except ZeroDivisionError:
    print("Xato! Nolga bo'lish mumkin emas.")

except AssertionError as xato:
    print("Xato:", xato)