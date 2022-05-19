# spúšťacie triedy v pythone úplne nie sú, scripty sa spúšťajú rovno
from bankovy_ucet import BankovyUcet


class Main:
    def start(self):
        prvy_ucet = BankovyUcet("Marek Palek", "991225/4568", 500)
        druhy_ucet = BankovyUcet("Fero Mrkvička", "555555/4798", 1000)

        print("Posielam z prvehu uctu na druhy ucet 500€...")
        prvy_ucet.poslat_peniaze(druhy_ucet, 500)
        print(f'Prvy ucet: {prvy_ucet.get_peniaze()}, Druhy ucet: {druhy_ucet.get_peniaze()}')

        print("Posielam z druheho uctu na prvy ucet 1500€...")
        druhy_ucet.poslat_peniaze(prvy_ucet, 1500)
        print(f'Prvy ucet: {prvy_ucet.get_peniaze()}, Druhy ucet: {druhy_ucet.get_peniaze()}')

        print("Posielam z druheho uctu na prvy ucet 200€...")
        druhy_ucet.poslat_peniaze(prvy_ucet, 200)
        print(f'Prvy ucet: {prvy_ucet.get_peniaze()}, Druhy ucet: {druhy_ucet.get_peniaze()}')

        print("Posielam z druheho uctu na druhy ucet 500€...")
        druhy_ucet.poslat_peniaze(druhy_ucet, 500)
        print(f'Prvy ucet: {prvy_ucet.get_peniaze()}, Druhy ucet: {druhy_ucet.get_peniaze()}')

Main().start()
