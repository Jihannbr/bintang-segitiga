string = ""
x = int(input("Masukkan angka :"))
bar = x

#Looping baris
while bar >= 0:

    #Looping kolom spasi kolom
    kol = bar
    while kol > 0:
        string = string + "   "
        kol = kol - 1

    #Looping kolom bintang
    kanan = 1
    while kanan < (x - (bar-1)):
        string = string + " * "
        kanan = kanan + 1

    string = string +"\n"
    bar = bar -1

print (string)
