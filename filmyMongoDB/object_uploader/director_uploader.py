import csv

from db_uploader.collection import DbUploader
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
                idRezysera = int(record[0])
                imie = record[1]
                nazwisko = record[2]
                data = record[3]
                dataUrodzenia = int(data[6:10])
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

    def insert_directors_to_db(self, collection_name):
        JSON_list_with_directors = self.prepare_JSON_list_with_directors()
        dbUploader = DbUploader()
        dbUploader.insert_documents_into_collection(collection_name, JSON_list_with_directors)

    def prepare_JSON_list_with_directors(self):
        JSON_list_with_directors = []
        for director in self.rezyserzy:
            JSON_director = director.prepare_JSON_director()
            JSON_list_with_directors.append(JSON_director)
        return JSON_list_with_directors