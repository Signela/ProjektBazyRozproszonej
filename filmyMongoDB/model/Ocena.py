class Ocena:

    def __init__(self, idOceny, wartoscOceny, dataWystawienia, uzytkownik):
        self.idOceny = idOceny
        self.wartoscOceny = wartoscOceny
        self.dataWystawienia = dataWystawienia
        self.użytkownik = uzytkownik

    def prepare_JSON_opinion(self):
        JSON_opinion = {}
        JSON_opinion["idOceny"] = self.idOceny
        JSON_opinion["wartoscOceny"] = self.wartoscOceny
        JSON_opinion["dataWystawienia"] = self.dataWystawienia
        JSON_opinion["użytkownik"] = self.użytkownik.prepare_JSON_user()
        return JSON_opinion