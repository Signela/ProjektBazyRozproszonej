import csv
from model.Rezyser import Rezyser


class DirectorUploader:

    def __init__(self, path):
        self.path = path
        self.rezyserzy = self.prepare_director_list()

    def prepare_director_list(self):
        rezyserzy = []
        f = open(self.path + 'rezyser.csv')
        with f:
            csvreader = csv.reader(f, delimiter=';')
            next(csvreader, None)
            for record in csvreader:
                idRezysera = record[0]
                imie = record[1]
                nazwisko = record[2]
                dataUrodzenia = record[3]
                oceny = []
                rezyser = Rezyser(idRezysera, imie, nazwisko, dataUrodzenia, oceny)
                rezyserzy.append(rezyser)
        return rezyserzy

    def get_director_by_id(self, idRezysera):
        for rezyser in self.rezyserzy:
            if rezyser.idRezysera == idRezysera:
                return rezyser

    def set_opinion_for_director(self, idRezysera, opinion):
        for idx, rezyser in enumerate(self.rezyserzy):
            if rezyser.idRezysera == idRezysera:
                rezyser.add_opinion(opinion)
                self.rezyserzy[idx] = rezyser
                break