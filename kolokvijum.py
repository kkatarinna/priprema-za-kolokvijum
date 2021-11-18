file = open("D:/fakultet/osnove programiranja/vezbe/vezbe 5/priprema za kolokvijum/bank_log.txt", "r")
content = file.readlines()
korisnici = {}
uplate = {}
for lines in content:
    lines = lines[:-1]
    line = lines.split(" ")
    if line[1] == "newaccount":
        korisnici[line[0]] = 0
        uplate[line[0]] = 0
    if line[1] == "income":
        korisnici[line[0]] = korisnici[line[0]] + float(line[2])
        uplate[line[0]] += 1
    if line[1] == "withdrawal":
        korisnici[line[0]] = korisnici[line[0]] - float(line[2])
print("unesite opciju koju zelite: ")
print("a) Za zadatog korisnika odrediti stanje na računu.")
print("b) Pronaći korisnika koji ima najviše novca na računu")
print("c) Pronaći korisnika sa najvećim brojem uplata")
print("d) Pronaći korisnike čije je stanje na računu manje od unetog iznosa")
print("e) Pronaći sve korisnike čije ime počinje zadatim/unetim stringom")
print("f) Kreirati izveštaj stanja na računu za sve postojeće korisnike. ")
odgovor = str.lower(input())

match odgovor:
    case "a":
        korisnik = input("Unesite username od korisnika: ")
        print("Trenutno stanje na racunu korisnika",korisnik,"je",korisnici[korisnik])
    case "b":
        rich = 0
        richuser = ""
        for i in korisnici:
            if rich < korisnici[i]:
                rich = korisnici[i]
                richuser = i
        print("Korisnik koji ima najvise novca na racunu je",richuser)
    case "c":
        bruplata = 0
        user = ""
        for i in uplate:
            if bruplata < uplate[i]:
                bruplata = uplate[i]
                user = i
        print("Korisnik sa najvecim brojem uplata je",user)
    case "d":
        iznos = eval(input("Unesite iznos: "))
        print("Korisnici sa stanjem na racunu manjim od unetog iznosa su: ")
        for i in korisnici:
            if iznos > korisnici[i]:
                print(i)
    case "e":
        ime = input("Unesite string: ")
        print("Korisnici cije ime pocinje zadatim stringom",ime,"su: ")
        for i in korisnici:
            if i.startswith(ime):
                print(i)
    case "f":
        for i in korisnici:
            print ("Stanje na racunu korisnika",i,"je",korisnici[i])
            print ("Broj uplata korisnika",i,"je",uplate[i])
file.close()