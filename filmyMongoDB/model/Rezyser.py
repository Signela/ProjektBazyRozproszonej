class Rezyser:

    def __init__(self, idRezysera, imie, nazwisko, dataUrodzenia, oceny):
        self.idRezysera = idRezysera
        self.imie = imie
        self.nazwisko = nazwisko
        self.dataUrodzenia = dataUrodzenia
        self.oceny = oceny

    def add_opinion(self, opinion):
        self.oceny.append(opinion)

    def prepare_JSON_director(self):
        JSON_director = {}
        JSON_director["idRezysera"] = self.idRezysera
        JSON_director["imie"] = self.imie
        JSON_director["nazwisko"] = self.nazwisko
        JSON_director["dataUrodzenia"] = self.dataUrodzenia
        JSON_director["oceny"] = self.prepare_JSON_list_with_opinions()
        return JSON_director

    def prepare_JSON_list_with_opinions(self):
        JSON_list_with_opinions = []
        for opinion in self.oceny:
            JSON_opinion = opinion.prepare_JSON_opinion()
            JSON_list_with_opinions.append(JSON_opinion)
        return JSON_list_with_opinions