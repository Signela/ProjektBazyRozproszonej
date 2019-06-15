class Uzytkownik:

    def __init__(self, idUzytkownika, imie, nazwisko, dataUrodzenia, login, haslo):
        self.idUzytkownika = idUzytkownika
        self.imie = imie
        self.nazwisko = nazwisko
        self.dataUrodzenia = dataUrodzenia
        self.login = login
        self.haslo = haslo

    def prepare_JSON_user(self):
        JSON_user = {}
        JSON_user["idUzytkownika"] = self.idUzytkownika
        JSON_user["imie"] = self.imie
        JSON_user["nazwisko"] = self.nazwisko
        JSON_user["dataUrodzenia"] = self.dataUrodzenia
        JSON_user["login"] = self.login
        JSON_user["haslo"] = self.haslo
        return JSON_user