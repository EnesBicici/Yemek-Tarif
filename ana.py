from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
from ana_ui import Ui_MainWindow
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtGui
from yemek import Tarif
from arama import AramaSayfa
from tarifekle import TarifEkleSayfa
from veritabani import Veritabani
from degerlendirme import DegerlendirmeSayfa
from puan import PuanSayfa

class AnaSayfa(QMainWindow):
    def __init__(self, uye) -> None:
        super().__init__()
        self.anasayfa = Ui_MainWindow()
        self.anasayfa.setupUi(self)
        self.index = 0
        self.uye = uye
        self.anasayfa.sonrakiButon.clicked.connect(self.sonraki)
        self.anasayfa.oncekiButon.clicked.connect(self.onceki)
        self.tarif_liste_guncelle()
        self.tarifguncelle()
        #self.anasayfa.biletButon.clicked.connect(self.oduncal)
        aramasayfa = AramaSayfa()
        tarifeklesayfa = TarifEkleSayfa()
        self.anasayfa.tarifAra.triggered.connect(lambda: aramasayfa.goster(self.tarifler))
        self.anasayfa.tarifEkle.triggered.connect(lambda: tarifeklesayfa.show())
        aramasayfa.arama_sinyal.connect(self.tarifgoster)
        tarifeklesayfa.ekle_sinyal.connect(self.tarif_liste_guncelle)
        degerlendirmesayfa = DegerlendirmeSayfa()
        self.anasayfa.degerlendirButon.clicked.connect(lambda: degerlendirmesayfa.goster(self.tarifler[self.index], self.uye))
        puansayfa = PuanSayfa()
        self.anasayfa.degerlendirmeler.triggered.connect(lambda: puansayfa.goster())

    def sonraki(self):
        self.index += 1
        if len(self.tarifler) == self.index:
            self.index = 0
        self.tarifguncelle()

    def onceki(self):
        self.index -= 1
        if self.index == -1:
            self.index = len(self.tarifler)-1
        self.tarifguncelle()

    def tarifgoster(self, yeni_indeks):
        self.index = yeni_indeks
        self.tarifguncelle()

    def tarifguncelle(self):
        tarif = self.tarifler[self.index]

        self.anasayfa.foto.setPixmap(QtGui.QPixmap("fotograflar/" + tarif.fotograf))
        self.anasayfa.tarifLabel.setText(tarif.ad)
        self.anasayfa.kisiLabel.setText(f'{tarif.kisi_sayisi} kişilik')
        self.anasayfa.hazirlamaLabel.setText(f'{tarif.hazirlama_suresi} dakika')
        self.anasayfa.pisirmeLabel.setText(f'{tarif.pisirme_suresi} dakika')

        Veritabani.query('SELECT Malzeme FROM Malzemeler WHERE TarifID = ?', (tarif.id,))
        malzemeler = Veritabani.fetchall()
        Veritabani.query('SELECT Asama FROM Asamalar WHERE TarifID = ?', (tarif.id,))
        asamalar = Veritabani.fetchall()

        yarim = len(malzemeler) // 2
        malzemeler1 = malzemeler[:yarim]
        malzemeler2 = malzemeler[yarim:]

        malzemestring1 = ""
        malzemestring2 = ""

        for malzeme in malzemeler1:
            malzemestring1 += f"- {malzeme[0]}<br>"
        for malzeme in malzemeler2:
            malzemestring2 += f"- {malzeme[0]}<br>"

        self.anasayfa.malzeme1.setText(malzemestring1)
        self.anasayfa.malzeme2.setText(malzemestring2)

        tarifstring = ""

        for index, asama in enumerate(asamalar):
            tarifstring += f"{index + 1}. {asama[0]}<br>"

        self.anasayfa.aciklamaLabel.setText(tarifstring)

    def tarif_liste_guncelle(self):
        Veritabani.query('SELECT * FROM tarifler')
        tarifler = Veritabani.fetchall()
        self.tarifler = []
        for tarif in tarifler:
            self.tarifler.append(Tarif(*tarif))
            