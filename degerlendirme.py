from PyQt5.QtWidgets import QWidget, QMessageBox
from degerlendirme_ui import Ui_Form
from PyQt5.QtGui import QPixmap
from veritabani import Veritabani

class DegerlendirmeSayfa(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.form = Ui_Form()
        self.form.setupUi(self)
        self.form.degerlendirButon.clicked.connect(self.degerlendir)
        self.form.yildiz1.clicked.connect(lambda: self.yildizguncelle(1))
        self.form.yildiz2.clicked.connect(lambda: self.yildizguncelle(2))
        self.form.yildiz3.clicked.connect(lambda: self.yildizguncelle(3))
        self.form.yildiz4.clicked.connect(lambda: self.yildizguncelle(4))
        self.form.yildiz5.clicked.connect(lambda: self.yildizguncelle(5))
        self.yildiz = 1

    def goster(self, tarif, uye):
        self.show()
        self.tarif = tarif
        self.uye = uye
        
    def degerlendir(self):
        Veritabani.query("select * from degerlendirmeler where kullaniciid=? and tarifid=?",(self.uye.id, self.tarif.id))
        varmi = Veritabani.fetchone()
        if varmi is not None:
            QMessageBox.warning(self, "Değerlendirme", "Bu tarifi zaten değerlendirmişsiniz.", QMessageBox.Ok)
            return
        yanit = QMessageBox.information(self, "Değerlendirme", "Tarifi değerlendirmek istediğinize emin misiniz?", QMessageBox.Yes, QMessageBox.No)   
        if yanit == QMessageBox.No:
            return 
        
        self.tarif.degerlendir(self.uye.id, self.yildiz)
        QMessageBox.information(self, "Değerlendirme", "Tarif değerlendirildi.", QMessageBox.Ok)

    def yildizguncelle(self, yildiz):
        if self.yildiz == yildiz:
            return
        
        if self.yildiz < yildiz:
            for i in range(1,yildiz+1):
                yildizz = getattr(self.form, f'yildiz{i}')
                yildizz.setPixmap(QPixmap("ui/yıldızdolu.png"))
        else:
            for i in range(yildiz+1,6):
                yildizz = getattr(self.form, f'yildiz{i}')
                yildizz.setPixmap(QPixmap("ui/yıldızbos.png"))
        self.yildiz = yildiz


