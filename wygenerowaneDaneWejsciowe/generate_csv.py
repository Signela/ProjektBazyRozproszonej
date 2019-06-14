import csv
from random import randint

header = []
names = []
surnames = []
dates = []
datesOfBirth = []
films = []
logins = []
passwords = []
times = []
liczbaFilmow = 69
liczbaAktorow = 100
liczbaRezyserow = 30 + liczbaAktorow
liczbaUzytkownikow = 1000
liczbaOcen = 500000
liczbaAktorowGrajacychWFilmach = liczbaAktorow * 2
profession = ["aktor", "rezyser"]

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

header = ['id', 'imie', 'nazwisko', 'dataUrodzenia', 'zawod']
aktor = open('aktor.csv', 'w', newline='')
with aktor:
    fnames = header
    writer = csv.DictWriter(aktor, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for i in range(0, liczbaAktorow):
        tab.__setitem__(header[0], i)
        tab.__setitem__(header[1], names[randint(0, liczbaFilmow)])
        tab.__setitem__(header[2], surnames[randint(0, liczbaFilmow)])
        tab.__setitem__(header[3], datesOfBirth[randint(0, liczbaFilmow)])
        tab.__setitem__(header[4], profession[0])
        writer.writerow(tab)
        tab.clear()
rezyser = open('rezyser.csv', 'w', newline='')
with rezyser:
    fnames = header
    writer = csv.DictWriter(rezyser, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for i in range(liczbaAktorow, liczbaRezyserow):
        tab.__setitem__(header[0], i)
        tab.__setitem__(header[1], names[randint(0, liczbaFilmow)])
        tab.__setitem__(header[2], surnames[randint(0, liczbaFilmow)])
        tab.__setitem__(header[3], datesOfBirth[randint(0, liczbaFilmow)])
        tab.__setitem__(header[4], profession[1])
        writer.writerow(tab)
        tab.clear()
header = ['id', 'nazwa', 'dlugoscTrwania', 'dataDodania', 'cena']
film = open('film.csv', 'w', newline='')
with film:
    fnames = header
    writer = csv.DictWriter(film, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for i in range(0, films.__len__()):
        tab.__setitem__(header[0], i)
        tab.__setitem__(header[1], films[i])
        tab.__setitem__(header[2], times[i])
        tab.__setitem__(header[3], dates[i])
        tab.__setitem__(header[4], randint(70, 300))
        writer.writerow(tab)
        tab.clear()
header = ['id', 'imie', 'nazwisko', 'dataUrodzenia', 'login', 'haslo']
uzytkownik = open('uzytkownik.csv', 'w', newline='')
with uzytkownik:
    fnames = header
    writer = csv.DictWriter(uzytkownik, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for i in range(0, liczbaUzytkownikow):
        tab.__setitem__(header[0], i)
        tab.__setitem__(header[1], names[randint(0, liczbaFilmow)])
        tab.__setitem__(header[2], surnames[randint(0, liczbaFilmow)])
        tab.__setitem__(header[3], datesOfBirth[randint(0, liczbaFilmow)])
        tab.__setitem__(header[4], logins[randint(0, liczbaFilmow)] + str(i))
        tab.__setitem__(header[5], passwords[randint(0, liczbaFilmow)] + str(i))
        writer.writerow(tab)
        tab.clear()
header = ['id', 'idUzytkownika', 'dataWstawienia', 'wartoscOceny']
ocena = open('ocena.csv', 'w', newline='')
with ocena:
    fnames = header
    writer = csv.DictWriter(ocena, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for i in range(0, liczbaOcen):
        tab.__setitem__(header[0], i)
        tab.__setitem__(header[1], randint(0, liczbaRezyserow-1))
        tab.__setitem__(header[2], dates[randint(0, liczbaFilmow)])
        tab.__setitem__(header[3], randint(1, 5))
        writer.writerow(tab)
        tab.clear()
header = ['idOceny', 'idUzytkownika']
filmOcena = open('film_ocena.csv', 'w', newline='')
with filmOcena:
    fnames = header
    writer = csv.DictWriter(filmOcena, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for i in range(0, int(liczbaOcen/2)):
        tab.__setitem__(header[0], i)
        tab.__setitem__(header[1], randint(0, liczbaFilmow))
        writer.writerow(tab)
        tab.clear()
header = ['idOceny', 'idAktor']
aktorOcena = open('aktor_ocena.csv', 'w', newline='')
with aktorOcena:
    fnames = header
    writer = csv.DictWriter(aktorOcena, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for i in range(int(liczbaOcen/2), int(liczbaOcen/2) + int(liczbaOcen/4)):
        tab.__setitem__(header[0], i)
        tab.__setitem__(header[1], randint(0, liczbaAktorow-1))
        writer.writerow(tab)
        tab.clear()
header = ['idOceny', 'idRezyser']
rezyserOcena = open('rezyser_ocena.csv', 'w', newline='')
with rezyserOcena:
    fnames = header
    writer = csv.DictWriter(rezyserOcena, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for i in range(int(liczbaOcen/2) + int(liczbaOcen/4), liczbaOcen):
        tab.__setitem__(header[0], i)
        tab.__setitem__(header[1], randint(liczbaAktorow, liczbaRezyserow-1))
        writer.writerow(tab)
        tab.clear()
header = ['idFilm', 'idRezyser']
rezyserFilm = open('rezyser_film.csv', 'w', newline='')
with rezyserFilm:
    fnames = header
    writer = csv.DictWriter(rezyserFilm, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for i in range(0, films.__len__()):
        tab.__setitem__(header[0], i)
        tab.__setitem__(header[1], randint(liczbaAktorow, liczbaRezyserow-1))
        writer.writerow(tab)
        tab.clear()
header = ['idFilm', 'idAktor']
aktorFilm = open('aktor_film.csv', 'w', newline='')
with aktorFilm:
    fnames = header
    writer = csv.DictWriter(aktorFilm, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for i in range(0, liczbaAktorowGrajacychWFilmach):
        tab.__setitem__(header[0], randint(0, liczbaFilmow))
        tab.__setitem__(header[1], randint(0, liczbaAktorow-1))
        writer.writerow(tab)
        tab.clear()
