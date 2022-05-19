# spúšťacie triedy v pythone úplne nie sú, scripty sa spúšťajú rovno
from zoznamy import Zoznamy


class Main:
    def start(self):
        zoznamy = Zoznamy()

        print("Vkladam znamku 1")
        zoznamy.pridat_znamku(1)

        print("Vkladam znamky 2, 3, 4")
        zoznamy.pridat_znamky([2, 3, 4])

        print(f'Max: {zoznamy.get_max()}, Min: {zoznamy.get_min()}')

Main().start()
