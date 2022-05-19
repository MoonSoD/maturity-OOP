class BankovyUcet:
    def __init__(self, klient, rodne_cislo, peniaze):
        self.klient = klient
        self.rodne_cislo = rodne_cislo
        self.peniaze = peniaze

    def poslat_peniaze(self, bankovy_ucet, peniaze):
        if bankovy_ucet == self:
            print("Nemozes poslat peniaze samemu sebe!")
            return

        if self.peniaze >= peniaze:
            bankovy_ucet.peniaze += peniaze
            self.peniaze -= peniaze
        else:
            print("Nedostatok penazi na ucte!")

    def get_peniaze(self):
        return self.peniaze
