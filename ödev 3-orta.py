seçimler = "Hesap Makinesi\n1. Toplama\n2. Çıkarma\n3. Çarpma\n4. Bölme\n5. Çıkış "
while 1:
    print(seçimler)
    seçim = input("İşlem seçin:")
    if seçim == "1":
        while 1:
            try:
                sayı1 = float(input("İlk sayıyı girin:"))
                sayı2 = float(input("İkinci sayıyı girin:"))
            except:
                print("İşlem yapılamaz")
                break
            else:
                toplam = sayı1 + sayı2
                if toplam == round(toplam):
                    toplam = int(toplam)
                print(f"Sonuç: {toplam}")
                break
    elif seçim == "2":
        while 1:
            try:
                sayı1 = float(input("İlk sayıyı girin:"))
                sayı2 = float(input("İkinci sayıyı girin:"))
            except:
                print("İşlem yapılamaz")
                break
            else:
                fark = sayı1 - sayı2
                if fark == round(fark):
                    fark = int(fark)
                print(f"Sonuç: {fark}")
                break
    elif seçim == "3":
        while 1:
            try:
                sayı1 = float(input("İlk sayıyı girin:"))
                sayı2 = float(input("İkinci sayıyı girin:"))
            except:
                print("İşlem yapılamaz")
                break
            else:
                çarpım = sayı1 * sayı2
                if çarpım == round(çarpım):
                    çarpım = int(çarpım)
                print(f"Sonuç: {çarpım}")
                break
    elif seçim == "4":
        while 1:
            try:
                sayı1 = float(input("İlk sayıyı girin:"))
                sayı2 = float(input("İkinci sayıyı girin:"))
            except:
                print("İşlem yapılamaz")
                break
            else:
                if sayı2 == 0:
                    print("Bu işlem yapılamaz")
                    break
                else:
                    bölüm = sayı1 / sayı2
                    if bölüm == round(bölüm):
                        bölüm = int(bölüm)
                    print(f"Sonuç: {bölüm}")
                    break
    elif seçim == "5":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Lütfen geçerli bir seçim yapın")
        continue