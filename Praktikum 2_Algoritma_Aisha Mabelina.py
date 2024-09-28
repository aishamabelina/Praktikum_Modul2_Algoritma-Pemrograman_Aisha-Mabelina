#LATIHAN PERTAMA
import math
#Program Python Operator Aritmatika 

nilai1 = float(input("Masukkan nilai pertama: "))
nilai2 = float(input("Masukkan nilai kedua: "))
hasiljumlah = nilai1+nilai2
hasilselisih = nilai1-nilai2
hasilkali = nilai1*nilai2
hasilfloatdev1 = nilai1//nilai2
hasilfloatdev2 = nilai1/nilai2
hasilloga = math.log(nilai1)
hasilpangkat = nilai1**nilai2

print(f"hasil dari penjumlahan A+B adalah = {hasiljumlah}.")
print(f"selisih antara A dan B = {hasilselisih}.")
print(f"jumlah A dikali B = {hasilkali}.")
print(f"jumlah sisa pembagian dari hasil A dibagi B adalah = {hasilfloatdev1}.")
print(f"jumlah A dibagi B adalah = {hasilfloatdev2}.")
print(f"hasil dari log(A) = {hasilloga}")
print(f"hasil A pangkat B adalah = {hasilpangkat}.")

#LATIHAN KEDUA
import math 
#Konversi derajat ke radian
 
Lintang1 = math.radians(float(input("Lintang Kota 1: ")))
Bujur1 = math.radians(float(input("Bujur Kota 1: ")))
Lintang2 = math.radians(float(input("Lintang kota 2: ")))
Bujur2 = math.radians(float(input("Bujur kota 2: ")))
R = 6371
Lat = Lintang2 - Lintang1
Long = Bujur2 - Bujur1

a = math.sin(Lat/2)*2 + math.cos(Lintang1) * math.cos(Lintang2) * math.sin(Long/2)*2
C3 = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
d = R * C3
print(f"Jarak antara dua titik tersebut adalah {d} kilometer.")








