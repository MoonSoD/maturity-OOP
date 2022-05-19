# spúšťacie triedy v pythone úplne nie sú, scripty sa spúšťajú rovno
from ziak import Ziak


class Main:
    def start(self):
        ziak = Ziak("Ferko", "Mrkvička", "Kysucké Nové Mesto 24", "0944555666")

        print(
            ziak.get_meno() + " " + ziak.get_priezvisko() + ", " + ziak.get_adresa() + "; " + ziak.get_cislo_telefonu()
        )


Main().start()
