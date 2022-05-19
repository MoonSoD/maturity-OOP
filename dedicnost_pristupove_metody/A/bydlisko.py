class Bydlisko:
    def __init__(self, ulica, cislo_domu, mesto):
        self.ulica = ulica
        self.cislo_domu = cislo_domu
        self.mesto = mesto

    def get_ulica(self):
        return self.ulica

    def set_ulica(self, ulica):
        self.ulica = ulica

    def get_cislo_domu(self):
        return self.cislo_domu

    def set_cislo_domu(self, cislo_domu):
        self.cislo_domu = cislo_domu

    def get_mesto(self):
        return self.mesto

    def set_mesto(self, mesto):
        self.mesto = mesto
