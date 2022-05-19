class Zoznamy:
    _znamky = []

    def pridat_znamku(self, znamka):
        self._znamky.append(znamka)

    def pridat_znamky(self, znamky):
        for znamka in znamky:
            self._znamky.append(znamka)

    def get_max(self):
        max_znamka = self._znamky[0]

        for znamka in self._znamky:
            if znamka > max_znamka:
                max_znamka = znamka

        return max_znamka

    def get_min(self):
        min_znamka = self._znamky[0]

        for znamka in self._znamky:
            if znamka < min_znamka:
                min_znamka = znamka

        return min_znamka