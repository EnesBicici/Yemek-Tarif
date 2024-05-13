from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal
from tarifekle_ui import Ui_Form
from yemek import Tarif

class TarifEkleSayfa(QWidget):
    ekle_sinyal = pyqtSignal()
    def __init__(self) -> None:
        super().__init__()
        self.form = Ui_Form()
        self.form.setupUi(self)
        self.form.ekleButon.clicked.connect(self.ekle)
        for i in range(5, 9):
            label = getattr(self.form, f'malzeme{i}label')
            label2 = getattr(self.form, f'adim{i}label')
            line = getattr(self.form, f'malzeme{i}Line')
            line2 = getattr(self.form, f'adim{i}Line')
            line.setVisible(False)
            line2.setVisible(False)
            label.setVisible(False)
            label2.setVisible(False)
        self.form.adim9Line.setVisible(False)
        self.form.adim9label.setVisible(False)
        self.form.malzemeBox.valueChanged.connect(self.malzemelineguncelle)
        self.form.adimBox.valueChanged.connect(self.adimlineguncelle)
        self.malzemesayisi = 4
        self.adimsayisi = 4
        
    def ekle(self):
        hazirlama = self.form.hazirlamaBox.value()
        pisirme = self.form.pisirmeBox.value()
        kisi = self.form.kisiBox.value()
        tarifisim = self.form.tarifAdLine.text()
        if not tarifisim:
            QMessageBox.warning(self, "tarif","Tarif ismi boş geçilemez.", QMessageBox.Ok)
            return

        malzemeler = []
        for i in range(1,self.malzemesayisi+1):
            line = getattr(self.form, f'malzeme{i}Line')
            malzeme = line.text()
            if not malzeme:
                QMessageBox.warning(self, "tarif","Malzeme boş geçilemez.", QMessageBox.Ok)
                return
            malzemeler.append(malzeme)
        
        adimlar = []
        for i in range(1,self.adimsayisi+1):
            line = getattr(self.form, f'adim{i}Line')
            adim = line.text()
            if not adim:
                QMessageBox.warning(self, "tarif","Aşama boş geçilemez.", QMessageBox.Ok)
                return
            adimlar.append(adim)

        Tarif.ekle(tarifisim, hazirlama, pisirme, kisi, malzemeler, adimlar)
        self.ekle_sinyal.emit()
        yanit = QMessageBox.information(self, "tarif","Tarif eklendi.", QMessageBox.Ok)    
        self.close()
        
    def malzemelineguncelle(self):
        yenimalzemesayisi = self.form.malzemeBox.value()
        if self.malzemesayisi == yenimalzemesayisi:
            return
    
        if yenimalzemesayisi == 8:
            for i in range(1,9):
                label = getattr(self.form, f'malzeme{i}label')
                line = getattr(self.form, f'malzeme{i}Line')
                line.setVisible(True)
                label.setVisible(True)
        else:
            for i in range(1,yenimalzemesayisi+1):
                label = getattr(self.form, f'malzeme{i}label')
                line = getattr(self.form, f'malzeme{i}Line')
                line.setVisible(True)
                label.setVisible(True)

            for i in range(yenimalzemesayisi+1,9):
                label = getattr(self.form, f'malzeme{i}label')
                line = getattr(self.form, f'malzeme{i}Line')
                line.setVisible(False)
                label.setVisible(False)
        self.malzemesayisi = yenimalzemesayisi

    def adimlineguncelle(self):
        yeniadimsayisi = self.form.adimBox.value()

        if self.adimsayisi == yeniadimsayisi:
            return
    
        if yeniadimsayisi == 9:
            for i in range(1,10):
                label = getattr(self.form, f'adim{i}label')
                line = getattr(self.form, f'adim{i}Line')
                line.setVisible(True)
                label.setVisible(True)
        else:
            for i in range(1,yeniadimsayisi+1):
                label = getattr(self.form, f'adim{i}label')
                line = getattr(self.form, f'adim{i}Line')
                line.setVisible(True)
                label.setVisible(True)

            for i in range(yeniadimsayisi+1,10):
                label = getattr(self.form, f'adim{i}label')
                line = getattr(self.form, f'adim{i}Line')
                line.setVisible(False)
                label.setVisible(False)

        self.adimsayisi = yeniadimsayisi