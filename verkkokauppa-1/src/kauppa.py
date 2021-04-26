from ostoskori import Ostoskori
from pankki import Pankki as default_bank
from viitegeneraattori import Viitegeneraattori as default_vg
from varasto import Varasto as default_var

class Kauppa:
    def __init__(self, va=default_var, pa=default_bank, vi=default_vg ):
        self._varasto = va
        self._pankki = pa
        self._viitegeneraattori = vi
        self._kaupan_tili = "33333-44455"

    def aloita_asiointi(self):
        self._ostoskori = Ostoskori()

    def poista_korista(self, id):
        tuote = self._varasto.hae_tuote(id)
        self._ostoskori.poista(tuote)
        self._varasto.palauta_varastoon(tuote)

    def lisaa_koriin(self, tuote_id):
        tsekki=self._varasto.saldo(tuote_id)
        print (tsekki)
        if tsekki > 0:
            tuote = self._varasto.hae_tuote(tuote_id)
            self._ostoskori.lisaa(tuote)
            self._varasto.ota_varastosta(tuote)

    def tilimaksu(self, nimi, tili_numero):
        viite = self._viitegeneraattori.uusi()
        summa = self._ostoskori.hinta()

        return self._pankki.tilisiirto(nimi, viite, tili_numero, self._kaupan_tili, summa)
