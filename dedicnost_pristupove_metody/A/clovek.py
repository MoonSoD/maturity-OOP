from bydlisko import Bydlisko


class Clovek(Bydlisko):
    def __init__(self, meno, priezvisko, ulica, cislo_domu, mesto):
        self.meno = meno
        self.priezvisko = priezvisko
        Bydlisko.__init__(self, ulica, cislo_domu, mesto)

    def get_meno(self):
        return self.meno

    def set_meno(self, meno):
        self.meno = meno

    def get_priezvisko(self):
        return self.priezvisko

    def set_priezvisko(self, priezvisko):
        self.priezvisko = priezvisko
