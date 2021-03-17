import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    def test_pelaajan_maalit_oikein(self):
        pelaajat=self.statistics
        #self.assertRegex(str((pelaajat.top_scorers(1)[0])), "Gretzky EDM 35 + 89 = 124")
        #return ("self.statistics.top_scorers(1)") 
   
    def test_pelaajan_pisteet_loytyy(self):
        pelaajat=self.statistics
        self.assertAlmostEqual((pelaajat.search("Gretzky").points), 124)

    def test_pelaaja_loytyy(self):
        pelaajat=self.statistics
        self.assertEqual(str((pelaajat.search("Gretzky"))), "Gretzky EDM 35 + 89 = 124")

    def test_vaara_pelaaja_eiloydy(self):
        pelaajat=self.statistics
        self.assertEqual((pelaajat.search("Kummola")), None)

    def test_top_scorers_toimii(self):
        pelaajat=self.statistics
        lista=pelaajat.top_scorers(2)
        self.assertEqual(str(lista[0]), "Gretzky EDM 35 + 89 = 124")

    def test_tiiminpelaajat(self):
        pelaajat=self.statistics
        lista=pelaajat.team("EDM")
        self.assertEqual(lista[0].name, "Semenko")
