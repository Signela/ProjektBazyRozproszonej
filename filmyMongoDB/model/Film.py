class Film:

    def __init__(self, idFilmu, nazwa, dataDodania, dlugoscTrwania, rezyser, aktorzy, oceny, cena):
        self.idFilmu = idFilmu
        self.nazwa = nazwa
        self.dataDodania = dataDodania
        self.dlugoscTrwania = dlugoscTrwania
        self.rezyser = rezyser
        self.aktorzy = aktorzy
        self.oceny = oceny
        self.cena = cena

    def add_opinion(self, opinion):
        self.oceny.append(opinion)

    def set_director(self, director):
        self.rezyser = director

    def add_actor(self, actor):
        self.aktorzy.append(actor)

    def prepare_JSON_movie(self):
        JSON_movie = {}
        JSON_movie["idFilmu"] = self.idFilmu
        JSON_movie["nazwa"] = self.nazwa
        JSON_movie["dataDodania"] = self.dataDodania
        JSON_movie["dlugoscTrwania"] = self.dlugoscTrwania
        JSON_movie["cena"] = self.cena
        JSON_movie["rezyser"] = self.rezyser.prepare_JSON_director()
        JSON_movie["aktorzy"] = self.prepare_JSON_list_with_actors()
        JSON_movie["oceny"] = self.prepare_JSON_list_with_opinions()
        return JSON_movie

    def prepare_JSON_list_with_actors(self):
        JSON_list_with_actors = []
        for actor in self.aktorzy:
            JSON_actor = actor.prepare_JSON_actor()
            JSON_list_with_actors.append(JSON_actor)
        return JSON_list_with_actors

    def prepare_JSON_list_with_opinions(self):
        JSON_list_with_opinions = []
        for opinion in self.oceny:
            JSON_opinion = opinion.prepare_JSON_opinion()
            JSON_list_with_opinions.append(JSON_opinion)
        return JSON_list_with_opinions