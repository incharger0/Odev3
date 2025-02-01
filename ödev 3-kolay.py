string = input("Bir string girin:")
buyuk = 0
kucuk = 0
for char in string: 
    if char.isupper() == True:
        buyuk += 1
    elif char.isupper() == False and char != " ":
        kucuk += 1        
print(f"Büyük harf sayısı: {buyuk}")
print(f"Küçük harf sayısı: {kucuk}")