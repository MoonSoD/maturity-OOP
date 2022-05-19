# bezparametrický konštruktor je v pythone už od základu a nemôžeme urobiť 2 konštruktory,
# ktoré by sa mohli použiť cez preťaženie

class Ziak:

    def __init__(self, meno, priezvisko, adresa, cislo_telefonu):
        self.meno = meno
        self.priezvisko = priezvisko
        self.adresa = adresa
        self.cislo_telefonu = cislo_telefonu

    def get_meno(self):
        return self.meno

    def get_priezvisko(self):
        return self.priezvisko

    def get_adresa(self):
        return self.adresa

    def get_cislo_telefonu(self):
        return self.cislo_telefonu
