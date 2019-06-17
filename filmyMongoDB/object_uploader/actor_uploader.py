import csv

from db_uploader.collection import DbUploader
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
                idAktora = int(record[0])
                imie = record[1]
                nazwisko = record[2]
                data = record[3]
                dataUrodzenia = int(data[6:10])
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

    def insert_actors_to_db(self, collection_name):
        JSON_list_with_actors = self.prepare_JSON_list_with_actors()
        dbUploader = DbUploader()
        dbUploader.insert_documents_into_collection(collection_name, JSON_list_with_actors)

    def prepare_JSON_list_with_actors(self):
        JSON_list_with_actors = []
        for actor in self.aktorzy:
            JSON_actor = actor.prepare_JSON_actor()
            JSON_list_with_actors.append(JSON_actor)
        return JSON_list_with_actors