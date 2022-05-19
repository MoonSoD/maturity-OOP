# spúšťacie triedy v pythone úplne nie sú, scripty sa spúšťajú rovno
from clovek import Clovek


class Main:
    def start(self):
        clovek = Clovek("Stanislav", "Feri", "Sládkovičova 1", 562, "Bratislava")

        print(
            f'{clovek.get_meno()} {clovek.get_priezvisko()}: {clovek.get_mesto()}, {clovek.get_ulica()} {clovek.get_cislo_domu()}'
        )

        clovek.set_ulica("Žilinská")
        print(
            f'{clovek.get_meno()} {clovek.get_priezvisko()}: {clovek.get_mesto()}, {clovek.get_ulica()} {clovek.get_cislo_domu()}'
        )

        clovek.set_meno("Jožko")
        print(
            f'{clovek.get_meno()} {clovek.get_priezvisko()}: {clovek.get_mesto()}, {clovek.get_ulica()} {clovek.get_cislo_domu()}'
        )

Main().start()
