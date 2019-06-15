import csv
from model.Aktor import Aktor


class ActorUploader:

    def __init__(self, path):
        self.path = path
        self.aktorzy = self.prepare_actor_list()

    def prepare_actor_list(self):
        aktorzy = []
        f = open(self.path + 'aktor.csv')
        with f:
            csvreader = csv.reader(f, delimiter=';')
            next(csvreader, None)
            for record in csvreader:
                idAktora = record[0]
                imie = record[1]
                nazwisko = record[2]
                dataUrodzenia = record[3]
                oceny = []
                aktor = Aktor(idAktora, imie, nazwisko, dataUrodzenia, oceny)
                aktorzy.append(aktor)
        return aktorzy

    def set_opinion_for_actor(self, idAktora, opinion):
        for idx, aktor in enumerate(self.aktorzy):
            if aktor.idAktora == idAktora:
                aktor.add_opinion(opinion)
                self.aktorzy[idx] = aktor
                break

    def get_actor_by_id(self, idAktora):
        for aktor in self.aktorzy:
            if aktor.idAktora == idAktora:
                return aktor