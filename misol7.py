natijalar = [
    {"ism": "Aziza", "ball": 82},
    {"ism": "Jasur", "ball": 64},
    {"ism": "Madina", "ball": 91},
    {"ism": "Sardor", "ball": 70}
]

yuqori = list(filter(lambda x: x["ball"] > 70, natijalar))

print("70 dan yuqori:", ", ".join(map(lambda x: x["ism"], yuqori)))
oshirilgan = list(map(lambda x: x["ball"] * 1.1, natijalar))

print("10% oshirilgan ballar:", oshirilgan)
saralangan = sorted(
    natijalar,
    key=lambda x: x["ball"],
    reverse=True
)

print("Saralangan:", ", ".join(map(lambda x: x["ism"], saralangan)))