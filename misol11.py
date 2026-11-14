import json


with open("sozlamalar.json", "r") as fayl:
    sozlamalar = json.load(fayl)
mavzu = input("Mavzu (light/dark): ")
bildirishnoma = input("Bildirishnoma (ha/yo'q): ")


if mavzu in ["light", "dark"]:
    sozlamalar["mavzu"] = mavzu

if bildirishnoma.lower() == "ha":
    sozlamalar["bildirishnoma"] = True
    
elif bildirishnoma.lower() in ["yo'q", "yo‘q"]:
    sozlamalar["bildirishnoma"] = False

with open("sozlamalar.json", "w") as fayl:
    json.dump(sozlamalar, fayl, indent=4)

print("Sozlamalar muvaffaqiyatli yangilandi!")