from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from puan_ui import Ui_Form
from PyQt5 import QtCore
from veritabani import Veritabani
from yemek import Uye, Tarif

class PuanSayfa(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.form = Ui_Form()
        self.form.setupUi(self)
    
    def goster(self):
        tablo = self.form.tableWidget
        tablo.setRowCount(0)
        tablo.setColumnWidth(0, 120)
        tablo.setColumnWidth(1, 130)
        tablo.setColumnWidth(2, 70)
        Veritabani.query('SELECT * FROM degerlendirmeler')
        degerlendirmeler = Veritabani.fetchall()
        if degerlendirmeler is None:
            return
        satir = 0
        tablo.setRowCount(len(degerlendirmeler))

        for degerlendirme in degerlendirmeler:
            Veritabani.query('SELECT * FROM kullanicilar where id=?', (degerlendirme[2],))
            kullanicisql = Veritabani.fetchone()
            kullanici = Uye(*kullanicisql)

            Veritabani.query('SELECT * FROM tarifler where id=?', (degerlendirme[1],))
            tarifsql = Veritabani.fetchone()
            tarif = Tarif(*tarifsql)

            kullanicicell = QTableWidgetItem(kullanici.ad + ' ' + kullanici.soyad)
            tarifcell = QTableWidgetItem(tarif.ad)
            puan = QTableWidgetItem(str(degerlendirme[3]) + "/5")

            #Hepsinin yazısını ortala
            kullanicicell.setTextAlignment(QtCore.Qt.AlignCenter)
            tarifcell.setTextAlignment(QtCore.Qt.AlignCenter)
            puan.setTextAlignment(QtCore.Qt.AlignCenter)

            tablo.setItem(satir, 0, kullanicicell)
            tablo.setItem(satir, 1, tarifcell)
            tablo.setItem(satir, 2, puan)
            
            satir+=1
            

        self.show()