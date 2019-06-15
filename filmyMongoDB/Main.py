from object_uploader.user_uploader import UserUploader
from object_uploader.director_uploader import DirectorUploader
from object_uploader.actor_uploader import ActorUploader
from object_uploader.movie_uploader import MovieUploader
from object_uploader.opinion_uploader import OpinionUploader

# for different number of record change "path" and "collection_name" variables to wanted

path_100k = 'D:/dev/SBD/wygenerowaneDaneWejsciowe/100k/'
path_250k = 'D:/dev/SBD/wygenerowaneDaneWejsciowe/250k/'
path_500k = 'D:/dev/SBD/wygenerowaneDaneWejsciowe/500k/'
collection_name_100k = "filmy_100k"
collection_name_250k = "filmy_250k"
collection_name_500k = "filmy_500k"

path = path_500k
collection_name = collection_name_500k

userUploader = UserUploader(path)
directorUploader = DirectorUploader(path)
actorUploader = ActorUploader(path)
movieUploader = MovieUploader(path)
opinionUploader = OpinionUploader(path, userUploader)

opinionUploader.set_opinions_for_objects(directorUploader, actorUploader, movieUploader)
movieUploader.set_director_for_movies(directorUploader)
movieUploader.set_actors_for_movies(actorUploader)

movieUploader.insert_movies_to_db(collection_name)