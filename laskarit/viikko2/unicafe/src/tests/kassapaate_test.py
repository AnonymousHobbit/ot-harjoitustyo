import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_oikea_maara_kassassa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisella_riittava(self):
        eaten = self.kassapaate.syo_edullisesti_kateisella(400)
        self.assertEqual(eaten, 400-240)
        self.assertEqual(self.kassapaate.edulliset, 1)

        eaten = self.kassapaate.syo_maukkaasti_kateisella(537)
        self.assertEqual(eaten, 537-400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kateisella_ei_riittava(self):
        eaten = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(eaten, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)

        eaten = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(eaten, 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maksukortti_rahaa(self):
        card = Maksukortti(400)
        eaten = self.kassapaate.syo_edullisesti_kortilla(card)
        self.assertEqual(eaten, True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        card = Maksukortti(500)
        eaten = self.kassapaate.syo_maukkaasti_kortilla(card)
        self.assertEqual(eaten, True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maksukortti_ei_rahaa(self):
        card = Maksukortti(200)
        eaten = self.kassapaate.syo_edullisesti_kortilla(card)
        self.assertEqual(eaten, False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        card = Maksukortti(300)
        eaten = self.kassapaate.syo_maukkaasti_kortilla(card)
        self.assertEqual(eaten, False)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kortille(self):
        card = Maksukortti(200)
        self.kassapaate.lataa_rahaa_kortille(card, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.assertEqual(card.saldo, 300)

    def test_lataa_rahaa_kortille_negatiivinen(self):
        card = Maksukortti(200)
        self.kassapaate.lataa_rahaa_kortille(card, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(card.saldo, 200)

    

        