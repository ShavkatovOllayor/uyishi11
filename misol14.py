import matplotlib.pyplot as plt

oylar = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun"]
daromad = [12, 15, 11, 19, 22, 18]

kategoriyalar = ["Texnika", "Kiyim", "Oziq-ovqat"]
savdo = [35, 20, 45]

buyurtma_qiymatlari = [50, 75, 80, 120, 150, 150, 180, 220, 250, 300]

plt.figure(figsize=(8, 5))
plt.plot(oylar, daromad, marker='o')

plt.title("Oylik daromad dinamikasi")
plt.xlabel("Oylar")
plt.ylabel("Daromad (mln so'm)")
plt.grid(True)

plt.show()

plt.figure(figsize=(8, 5))
plt.bar(kategoriyalar, savdo)

plt.title("Kategoriyalar savdosi")
plt.xlabel("Kategoriyalar")
plt.ylabel("Savdo (dona)")

plt.show()

plt.figure(figsize=(8, 5))
plt.hist(buyurtma_qiymatlari, bins=5, edgecolor='black')

plt.title("Buyurtma qiymatlari taqsimoti")
plt.xlabel("Buyurtma qiymati")
plt.ylabel("Buyurtmalar soni")

plt.show()
