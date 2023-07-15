import os
import sys
import json
import time
import requests as req
from colorama import Fore, init
# ========================================

os.system("clear")

init(autoreset=True)

banner = """
          +-+-+-+-+ +-+-+-+-+
          |B|M|K|G| |I|n|f|o|
          +-+-+-+-+ +-+-+-+-+


         F I B R E Y Y A N T 2.
 """
for bannersaya in banner.split("\n"):
    print (bannersaya)
    time.sleep(0.1)
# ===============================================================-

url = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json"
res = req.get(url, "html.parser")
data = json.loads(res.content)

print (Fore.GREEN + f"▶ (Tanggal)───────: {data['Infogempa']['gempa']['Tanggal']}")
print (Fore.YELLOW + f"▶ (Jam)───────────: {data['Infogempa']['gempa']['Jam']}")
print (Fore.GREEN + f"▶ (Date Time)─────: {data['Infogempa']['gempa']['DateTime']}")
print (Fore.YELLOW + f"▶ (Coordinates)───: {data['Infogempa']['gempa']['Coordinates']}")
print (Fore.GREEN + f"▶ (Lintang)───────: {data['Infogempa']['gempa']['Lintang']}")
print (Fore.YELLOW +f"▶ (Bujur)─────────: {data['Infogempa']['gempa']['Bujur']}")
print (Fore.GREEN + f"▶ (Magnitude)─────: {data['Infogempa']['gempa']['Magnitude']}")
print (Fore.YELLOW + f"▶ (Kedalaman)─────: {data['Infogempa']['gempa']['Kedalaman']}")
print (Fore.GREEN + f"▶ (Wilayah)───────: {data['Infogempa']['gempa']['Wilayah']}")
print (Fore.YELLOW + f"▶ (Potensi)───────: {data['Infogempa']['gempa']['Potensi']}")
print (Fore.GREEN + f"▶ (Dirasakan)─────: {data['Infogempa']['gempa']['Dirasakan']}")
print (Fore.YELLOW + f"▶ (Shakemap)──────: {data['Infogempa']['gempa']['Shakemap']}")

simpan = input(Fore.YELLOW + "\n\n[+] Simpan Data? [Y / N] ▶" + Fore.GREEN + " ").lower()

if "y" in simpan:
    jenis_file = ".json"
    nama_file = input(Fore.YELLOW + "[+] Nama File Tanpa Ekstensi ▶ ")
    with open(f"{nama_file}{jenis_file}", "w") as f:
        json.dump(data, f)
        f.close()
        print (Fore.YELLOW + "[!] Data Berhasil Disimpan dengan nama", Fore.GREEN + f"{nama_file}{jenis_file}\n")
        for datas in data:
            print (data)

elif "n" in simpan:
    sys.exit("\n[!] Good Bye!~")

else:
    sys.exit("Bai")
    print ("[!] Thanks!")
