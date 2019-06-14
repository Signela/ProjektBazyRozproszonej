import csv
from random import randint

header = []
names = []
surnames = []
dates = []
datesOfBirth = []
films = []
logins = []
passwords =[]
times = []
profession = ["aktor","rezyser"]

f = open('dane_do_generowania.csv', encoding="utf8")
with f:
    csvreader = csv.reader(f, delimiter=';')
    for i in csvreader:
        for j in i:
            header.append(j)
        break
    header.remove(header[0])
    csvreader = csv.reader(f, delimiter=';')
    for i in csvreader:
        names.append(i[0])
        surnames.append(i[1])
        dates.append(i[2])
        datesOfBirth.append(i[4])
        films.append(i[7])
        logins.append(i[5])
        passwords.append(i[6])
        times.append(i[8])

header = ['id','imie','nazwisko','dataUrodzenia','zawod']
aktor = open('aktor.csv', 'w', newline='')
with aktor:
    fnames = header
    writer = csv.DictWriter(aktor, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for i in range(0,5000):
        tab.__setitem__(header[0], i)
        tab.__setitem__(header[1], names[randint(0, 69)])
        tab.__setitem__(header[2], surnames[randint(0, 69)])
        tab.__setitem__(header[3], datesOfBirth[randint(0, 69)])
        tab.__setitem__(header[4], profession[0])
        writer.writerow(tab)
        tab.clear()
rezyser = open('rezyser.csv', 'w', newline='')
with rezyser:
    fnames = header
    writer = csv.DictWriter(rezyser, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for i in range(5000,10000):
        tab.__setitem__(header[0], i)
        tab.__setitem__(header[1], names[randint(0, 69)])
        tab.__setitem__(header[2], surnames[randint(0, 69)])
        tab.__setitem__(header[3], datesOfBirth[randint(0, 69)])
        tab.__setitem__(header[4], profession[1])
        writer.writerow(tab)
        tab.clear()
header = ['id','nazwa','dlugoscTrwania','dataDodania']
film = open('film.csv', 'w', newline='')
with film:
    fnames = header
    writer = csv.DictWriter(film, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for i in range(0,films.__len__()):
        tab.__setitem__(header[0], i)
        tab.__setitem__(header[1], films[i])
        tab.__setitem__(header[2], times[i])
        tab.__setitem__(header[3], dates[i])
        writer.writerow(tab)
        tab.clear()
header = ['id','imie','nazwisko','dataUrodzenia','login','haslo']
uzytkownik = open('uzytkownik.csv', 'w', newline='')
with uzytkownik:
    fnames = header
    writer = csv.DictWriter(uzytkownik, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for i in range(0,10000):
        tab.__setitem__(header[0], i)
        tab.__setitem__(header[1], names[randint(0, 69)])
        tab.__setitem__(header[2], surnames[randint(0, 69)])
        tab.__setitem__(header[3], datesOfBirth[randint(0, 69)])
        tab.__setitem__(header[4], logins[randint(0, 69)]+str(i))
        tab.__setitem__(header[4], passwords[randint(0, 69)]+str(i))
        writer.writerow(tab)
        tab.clear()
header = ['id','idUzytkownika','dataWstawienia','wartoscOceny']
ocena = open('ocena.csv', 'w', newline='')
with ocena:
    fnames = header
    writer = csv.DictWriter(ocena, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for i in range(0,1000000):
        tab.__setitem__(header[0], i)
        tab.__setitem__(header[1], randint(0, 9999))
        tab.__setitem__(header[2], dates[randint(0, 69)])
        tab.__setitem__(header[3], randint(1, 5))
        writer.writerow(tab)
        tab.clear()
header = ['idOceny','idUzytkownika']
filmOcena = open('film_ocena.csv', 'w', newline='')
with filmOcena:
    fnames = header
    writer = csv.DictWriter(filmOcena, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for i in range(0,500000):
        tab.__setitem__(header[0], i)
        tab.__setitem__(header[1], randint(0, 69))
        writer.writerow(tab)
        tab.clear()
header = ['idOceny','idAktor']
aktorOcena = open('aktor_ocena.csv', 'w', newline='')
with aktorOcena:
    fnames = header
    writer = csv.DictWriter(aktorOcena, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for i in range(500000,750000):
        tab.__setitem__(header[0], i)
        tab.__setitem__(header[1], randint(0, 69))
        writer.writerow(tab)
        tab.clear()
header = ['idOceny','idRezyser']
rezyserOcena = open('rezyser_ocena.csv', 'w', newline='')
with rezyserOcena:
    fnames = header
    writer = csv.DictWriter(rezyserOcena, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for i in range(750000,1000000):
        tab.__setitem__(header[0], i)
        tab.__setitem__(header[1], randint(0, 69))
        writer.writerow(tab)
        tab.clear()
header = ['idFilm','idRezyser']
rezyserOcena = open('rezyser_film.csv', 'w', newline='')
with rezyserOcena:
    fnames = header
    writer = csv.DictWriter(rezyserOcena, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for i in range(0,films.__len__()):
        tab.__setitem__(header[0], i)
        tab.__setitem__(header[1], randint(5000, 10000))
        writer.writerow(tab)
        tab.clear()
header = ['idFilm','idAktor']
rezyserOcena = open('aktor_film.csv', 'w', newline='')
with rezyserOcena:
    fnames = header
    writer = csv.DictWriter(rezyserOcena, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for i in range(0,100000):
        tab.__setitem__(header[0], randint(0, 69))
        tab.__setitem__(header[1], randint(0, 5000))
        writer.writerow(tab)
        tab.clear()