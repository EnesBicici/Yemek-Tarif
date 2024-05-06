from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal
from arama_ui import Ui_Form
from yemek import Tarif

class AramaSayfa(QWidget):
    arama_sinyal = pyqtSignal(int)
    def __init__(self) -> None:
        super().__init__()
        self.aramaform = Ui_Form()
        self.aramaform.setupUi(self)
        self.aramaform.araButon.clicked.connect(self.ara)

    def goster(self, tarifler):
        self.show()
        self.tarifler = tarifler
        hazirlamabox = self.aramaform.hazirlamaBox
        pisirmeBox = self.aramaform.pisirmeBox
        kisibox = self.aramaform.kisiBox
        hazirlamabox.clear()
        pisirmeBox.clear()
        kisibox.clear()
        hazirlamabox.addItem("Seçiniz", 0)
        hazirlamabox.addItem("10 dakika", 10)
        hazirlamabox.addItem("15 dakika", 15)
        hazirlamabox.addItem("20 dakika", 20)
        hazirlamabox.addItem("30 dakika", 30)
        pisirmeBox.addItem("Seçiniz", 0)
        pisirmeBox.addItem("15 dakika", 15)
        pisirmeBox.addItem("20 dakika", 20)
        pisirmeBox.addItem("30 dakika", 30)
        kisibox.addItem("Seçiniz", 0)
        kisibox.addItem("5 kişi", 5)
        kisibox.addItem("8 kişi", 8)
        kisibox.addItem("10 kişi", 10)
        
    def ara(self):
        hazirlama = self.aramaform.hazirlamaBox.currentData()
        pisirme = self.aramaform.pisirmeBox.currentData()
        kisi = self.aramaform.kisiBox.currentData()
        tarifisim = self.aramaform.isimLine.text()

        tarif = Tarif.ara(hazirlama, pisirme, kisi, tarifisim)

        if tarif is None:
            QMessageBox.warning(self, "Tarif", "Tarif bulunamadı.", QMessageBox.Ok)
            return
        
        self.arama_sinyal.emit(tarif.id-1)
        self.close()