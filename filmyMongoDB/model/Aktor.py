class Aktor:

    def __init__(self, idAktora, imie, nazwisko, dataUrodzenia, oceny):
        self.idAktora = idAktora
        self.imie = imie
        self.nazwisko = nazwisko
        self.dataUrodzenia = dataUrodzenia
        self.oceny = oceny

    def add_opinion(self, opinion):
        self.oceny.append(opinion)

    def prepare_JSON_actor(self):
        JSON_actor = {}
        JSON_actor["idAktora"] = self.idAktora
        JSON_actor["imie"] = self.imie
        JSON_actor["nazwisko"] = self.nazwisko
        JSON_actor["dataUrodzenia"] = self.dataUrodzenia
        JSON_actor["oceny"] = self.prepare_JSON_list_with_opinions()
        return JSON_actor

    def prepare_JSON_list_with_opinions(self):
        JSON_list_with_opinions = []
        for opinion in self.oceny:
            JSON_opinion = opinion.prepare_JSON_opinion()
            JSON_list_with_opinions.append(JSON_opinion)
        return JSON_list_with_opinions