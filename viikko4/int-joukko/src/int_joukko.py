class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin on oltava positiivinen kokonaisluku!")
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Kasvatuskoon on oltava positiivinen kokonaisluku!")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, testattava_luku):
        if testattava_luku in self.ljono:
            return True

        return False

    def lisaa(self, lisattava_luku):
        if not self.kuuluu(lisattava_luku):
            self.ljono[self.alkioiden_lkm] = lisattava_luku
            self.alkioiden_lkm += 1
            self.kasvata_joukkoa_tarvittaessa()
            

    def kasvata_joukkoa_tarvittaessa(self):
        if self.alkioiden_lkm == len(self.ljono):
            for i in range(0, self.kasvatuskoko):
                self.ljono.append(0)

    def poista(self, poistettava_luku):
        if self.kuuluu(poistettava_luku):
            self.ljono.remove(poistettava_luku)
            self.alkioiden_lkm -= 1

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = []
        for i in self.ljono:
            if i != 0:
                taulu.append(i)

        return taulu

    @staticmethod
    def yhdiste(joukko_1, joukko_2):
        yhdistetty_joukko = IntJoukko()
        yhdistetty_lista = joukko_1.to_int_list() + joukko_2.to_int_list()
        for i in yhdistetty_lista:
            yhdistetty_joukko.lisaa(i)
        return yhdistetty_joukko

    @staticmethod
    def leikkaus(joukko_1, joukko_2):
        leikattu_joukko = IntJoukko()
        lista_1 = joukko_1.to_int_list()
        lista_2 = joukko_2.to_int_list()

        for i in lista_1:
            for j in lista_2:
                if i == j:
                    leikattu_joukko.lisaa(j)

        return leikattu_joukko

    @staticmethod
    def erotus(joukko_1, joukko_2):
        erotusjoukko = IntJoukko()
        lista_1 = joukko_1.to_int_list()
        lista_2 = joukko_2.to_int_list()

        for i in lista_1:
            erotusjoukko.lisaa(i)

        for i in lista_2:
            erotusjoukko.poista(i)

        return erotusjoukko

    def __str__(self):
        luvut_listana = self.to_int_list()
        luvut_stringina_ilman_hakasulkeita = str(luvut_listana)[1:-1]
        luvut_stringina_aaltosulkeilla = "{" + luvut_stringina_ilman_hakasulkeita + "}"
        return luvut_stringina_aaltosulkeilla