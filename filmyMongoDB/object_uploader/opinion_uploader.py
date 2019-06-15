import csv
from model.Ocena import Ocena


class OpinionUploader:

    def __init__(self, path, user_uploader):
        self.path = path
        self.user_uploader = user_uploader
        self.oceny = self.prepare_opinion_list()

    def prepare_opinion_list(self):
        oceny = []
        f = open(self.path + 'ocena.csv')
        with f:
            csvreader = csv.reader(f, delimiter=';')
            next(csvreader, None)
            for record in csvreader:
                idOceny = record[0]
                idUzytkownika = record[1]
                dataWystawienia = record[2]
                wartoscOceny = record[3]

                uzytkownik = self.user_uploader.get_user_by_id(idUzytkownika)
                ocena = Ocena(idOceny, wartoscOceny, dataWystawienia, uzytkownik)
                oceny.append(ocena)
        return oceny

    def set_opinions_for_objects(self, directorUploader, actorUploader, movieUploader):
        self.set_opinions_for_directors(directorUploader)
        self.set_opinions_for_actors(actorUploader)
        self.set_opinions_for_movies(movieUploader)

    def set_opinions_for_directors(self, directorUploader):
        f = open(self.path + 'rezyser_ocena.csv')
        with f:
            csvreader = csv.reader(f, delimiter=';')
            next(csvreader, None)
            for record in csvreader:
                idOceny = record[0]
                idRezysera = record[1]

                ocena = self.get_opinion_by_id(idOceny)
                directorUploader.set_opinion_for_director(idRezysera, ocena)

    def set_opinions_for_actors(self, actorUploader):
        f = open(self.path + 'aktor_ocena.csv')
        with f:
            csvreader = csv.reader(f, delimiter=';')
            next(csvreader, None)
            for record in csvreader:
                idOceny = record[0]
                idAktora = record[1]

                ocena = self.get_opinion_by_id(idOceny)
                actorUploader.set_opinion_for_actor(idAktora, ocena)

    def set_opinions_for_movies(self, movieUploader):
        f = open(self.path + 'film_ocena.csv')
        with f:
            csvreader = csv.reader(f, delimiter=';')
            next(csvreader, None)
            for record in csvreader:
                idOceny = record[0]
                idFilmu = record[1]

                ocena = self.get_opinion_by_id(idOceny)
                movieUploader.set_opinion_for_movie(idFilmu, ocena)

    def get_opinion_by_id(self, idOceny):
        return self.oceny[int(idOceny)]