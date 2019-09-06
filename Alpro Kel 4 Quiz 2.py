print("----------------------------------GIVEAWAY PROVIDER UNTUK MAHASISWA TELKOM UNIVERSITY----------------------------------")

mhs = str(input("Nama Mahasiswa = "))
card = str(input("Provider = "))
ip = float(input("IPK = "))

if card == "Telkomsel" and ip > 3:
    print(mhs, "Selamat Anda Mendapatkan Giveaway Iphone X")

elif card != "Telkomsel" and ip > 3:
    print(mhs, "Selamat Anda Mendapatkan Giveaway Samsung J Galaxy")

elif card == "Telkomsel" and 2.5 <= ip <= 3:
    print(mhs, "Selamat Anda Mendapatkan Giveaway Playstation 4")

elif card != "Telkomsel" and 2.5 <= ip <= 3:
    print(mhs, "Selamat Anda Mendapatkan Giveaway Voucher Menginap di IBIS Hotel")

elif card == "Telkomsel" and ip == 2 <= 2.5:
    print(mhs, "Selamat Anda Mendapatkan Giveaway Voucher Menginap di Pondok Pesantren Darul Tauhid")

elif card != "Telkomsel" and ip == 2 <= 2.5:
    print(mhs, "Selamat Anda Mendapatkan Giveawat Voucher Berkunjung Ke Klinik Sikologi")

else:
    print("SELAMAT DAN TERIMAKASIH")