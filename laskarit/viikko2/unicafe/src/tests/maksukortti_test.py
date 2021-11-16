import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_saldo_kasvattaa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(self.maksukortti.saldo, 20)
    
    def test_saldo_vahenee_oikein_jos_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(self.maksukortti.saldo, 5)

    def test_saldo_ei_muutu_kun_raha_loppu(self):
        self.maksukortti.ota_rahaa(15)
        self.assertEqual(self.maksukortti.saldo, 10)
    
    def test_saldo_ota_rahaa_toimii(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)