import random
import string



def kn(tanlangan_harf):
    with open(tanlangan_harf + ".txt", 'w') as fayl:
        fayl.write("Hacked https://t.me/Kamolov_X7VIP ")

for i in range(1000):
    def tahminiy_harf_tanlash(harf_soni=1):
        if harf_soni < 1:
            raise ValueError("Harf soni kamida 1 bo'lishi kerak.")
        tanlangan_harflar = ''.join(random.choices(string.ascii_lowercase, k=harf_soni)) 
        return tanlangan_harflar
    tanlangan_harf = tahminiy_harf_tanlash(random.randint(1,25))  
    print("Tahminiy tanlangan harflar:", tanlangan_harf)
    kn(tanlangan_harf)
