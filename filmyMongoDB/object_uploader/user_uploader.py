import csv
from model.Uzytkownik import Uzytkownik
import os


class UserUploader:

    def __init__(self, path):
        self.path = path
        self.uzytkownicy = self.prepare_user_list()

    def prepare_user_list(self):
        uzytkownicy = []
        f = open(self.path + 'uzytkownik.csv')
        with f:
            csvreader = csv.reader(f, delimiter=';')
            next(csvreader, None)
            for record in csvreader:
                idUzytkownika = int(record[0])
                imie = record[1]
                nazwisko = record[2]
                data = record[3]
                dataUrodzenia = int(data[6:10])
                login = record[4]
                haslo = record[5]
                uzytkownik = Uzytkownik(idUzytkownika, imie, nazwisko, dataUrodzenia, login, haslo)
                uzytkownicy.append(uzytkownik)
        return uzytkownicy

    def get_user_by_id(self, idUzytkownika):
        for uzytkownik in self.uzytkownicy:
            if uzytkownik.idUzytkownika == idUzytkownika:
                return uzytkownik