import csv
from model.Film import Film
from db_uploader.movies_collection import MovieDbUploader


class MovieUploader:

    def __init__(self, path):
        self.path = path
        self.filmy = self.prepare_movie_list()

    def prepare_movie_list(self):
        filmy = []
        f = open(self.path + 'film.csv')
        with f:
            csvreader = csv.reader(f, delimiter=';')
            next(csvreader, None)
            for record in csvreader:
                idFilmu = record[0]
                nazwa = record[1]
                dlugoscTrwania = record[2]
                dataDodania = record[3]
                cena = record[4]
                rezyser = None
                aktorzy = []
                oceny = []
                film = Film(idFilmu, nazwa, dataDodania, dlugoscTrwania, rezyser, aktorzy, oceny, cena)
                filmy.append(film)
        return filmy

    def set_opinion_for_movie(self, idFilmu, opinion):
        film = self.filmy[int(idFilmu)]
        film.add_opinion(opinion)
        self.filmy[int(idFilmu)] = film

    def set_director_for_movies(self, directorUploader):
        f = open(self.path + 'rezyser_film.csv')
        with f:
            csvreader = csv.reader(f, delimiter=';')
            next(csvreader, None)
            for record in csvreader:
                idFilmu = record[0]
                idRezysera = record[1]
                rezyser = directorUploader.get_director_by_id(idRezysera)
                self.set_director_for_movie(idFilmu, rezyser)

    def set_director_for_movie(self, idFilmu, director):
        film = self.filmy[int(idFilmu)]
        film.set_director(director)
        self.filmy[int(idFilmu)] = film

    def set_actors_for_movies(self, actorUploader):
        f = open(self.path + 'aktor_film.csv')
        with f:
            csvreader = csv.reader(f, delimiter=';')
            next(csvreader, None)
            for record in csvreader:
                idFilmu = record[0]
                idAktora = record[1]
                aktor = actorUploader.get_actor_by_id(idAktora)
                self.set_actor_for_movie(idFilmu, aktor)

    def set_actor_for_movie(self, idFilmu, actor):
        film = self.filmy[int(idFilmu)]
        film.add_actor(actor)
        self.filmy[int(idFilmu)] = film

    def insert_movies_to_db(self, collection_name):
        JSON_list_with_movies = self.prepare_JSON_list_with_movies()
        movieDbUploader = MovieDbUploader()
        movieDbUploader.insert_documents_into_collection(collection_name, JSON_list_with_movies)

    def prepare_JSON_list_with_movies(self):
        JSON_list_with_movies = []
        for movie in self.filmy:
            JSON_movie = movie.prepare_JSON_movie()
            JSON_list_with_movies.append(JSON_movie)
        return JSON_list_with_movies