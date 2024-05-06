from veritabani import Veritabani

class Uye:
    def __init__(self, id, kullaniciadi, sifre, ad, soyad, telefon):
        self.id = id
        self.kullaniciadi = kullaniciadi
        self.sifre = sifre
        self.ad = ad
        self.soyad = soyad
        self.telefon = telefon

    @staticmethod
    def kayitol(kullaniciadi, sifre, ad, soyad, telefon):
        Veritabani.query('INSERT INTO kullanicilar (kullaniciadi, sifre, ad, soyad, telefon) VALUES(?, ?, ?, ?, ?)', (kullaniciadi, sifre, ad, soyad, telefon))
    
class Tarif:
    def __init__(self, id, ad, kisi_sayisi, hazirlama_suresi, pisirme_suresi, fotograf) -> None:
        self.id = id
        self.ad = ad
        self.kisi_sayisi = kisi_sayisi
        self.hazirlama_suresi = hazirlama_suresi
        self.pisirme_suresi = pisirme_suresi
        self.fotograf = fotograf

    def degerlendir(self, kullaniciid, puan):
        Veritabani.query('INSERT INTO degerlendirmeler (tarifid, kullaniciid, puan) VALUES(?, ?, ?)', (self.id, kullaniciid, puan))

    @staticmethod
    def ara(hazirlama, pisirme, kisi, tarifisim):
        print(hazirlama, pisirme, kisi, tarifisim)
        if hazirlama == 0 and pisirme == 0 and kisi == 0 and len(tarifisim) > 2: # Sadece tarif ismi girilmiş
            Veritabani.query('SELECT * FROM tarifler WHERE ad LIKE ?', (f"%{tarifisim}%",))
        elif kisi != 0 and pisirme == 0 and hazirlama == 0 and len(tarifisim) < 2:  # Sadece kişi seçilmiş
            Veritabani.query('SELECT * FROM tarifler WHERE kisisayisi = ?', (kisi,))
        elif kisi == 0 and pisirme != 0 and hazirlama == 0 and len(tarifisim) < 2:  # Sadece Pişirme seçilmiş
            Veritabani.query('SELECT * FROM tarifler WHERE pisirmesuresi = ?', (pisirme,))
        elif kisi == 0 and pisirme == 0 and hazirlama != 0 and len(tarifisim) < 2:  # Sadece Hazırlama seçilmiş
            Veritabani.query('SELECT * FROM tarifler WHERE hazirlamasuresi = ?', (hazirlama,))
        elif kisi != 0 and pisirme != 0 and hazirlama != 0 and len(tarifisim) < 2:  # Hepsi seçilmiş, isim girilmemiş
            Veritabani.query('SELECT * FROM tarifler WHERE kisisayisi = ? and pisirmesuresi = ? and hazirlamasuresi = ?', (kisi, pisirme, hazirlama))
        elif kisi != 0 and pisirme != 0 and hazirlama == 0 and len(tarifisim) < 2:  # Kişi ve Pişirme Seçilmiş
            Veritabani.query('SELECT * FROM tarifler WHERE kisisayisi = ? and pisirmesuresi = ?', (kisi,pisirme))
        elif kisi != 0 and pisirme == 0 and hazirlama != 0 and len(tarifisim) < 2:  # Kişi ve Hazırlama
            Veritabani.query('SELECT * FROM tarifler WHERE kisisayisi = ? and hazirlamasuresi = ?', (kisi,hazirlama))
        elif kisi == 0 and pisirme != 0 and hazirlama != 0 and len(tarifisim) < 2:  # Hazırlama ve Pişirme
            Veritabani.query('SELECT * FROM tarifler WHERE pisirmesuresi = ? and hazirlamasuresi = ?', (pisirme,hazirlama))

        # Tarif ismi girilmiş

        elif kisi != 0 and pisirme == 0 and hazirlama == 0 and len(tarifisim) > 2:  # Sadece kişi seçilmiş
            Veritabani.query('SELECT * FROM tarifler WHERE ad LIKE ? and kisisayisi = ?', (f"%{tarifisim}%",kisi))
        elif kisi == 0 and pisirme != 0 and hazirlama == 0 and len(tarifisim) > 2:  # Sadece Pişirme seçilmiş
            Veritabani.query('SELECT * FROM tarifler WHERE ad LIKE ? and pisirmesuresi = ?', (f"%{tarifisim}%",pisirme))
        elif kisi == 0 and pisirme == 0 and hazirlama != 0 and len(tarifisim) > 2:  # Sadece Hazırlama seçilmiş
            Veritabani.query('SELECT * FROM tarifler WHERE ad LIKE ? and hazirlamasuresi = ?', (f"%{tarifisim}%",hazirlama))
        elif kisi != 0 and pisirme != 0 and hazirlama != 0 and len(tarifisim) > 2:  # Hepsi seçilmiş
            Veritabani.query('SELECT * FROM tarifler WHERE ad LIKE ? and kisisayisi = ? and pisirmesuresi = ? and hazirlamasuresi = ?', (f"%{tarifisim}%",kisi,pisirme,hazirlama))
        elif kisi != 0 and pisirme != 0 and hazirlama == 0 and len(tarifisim) > 2:  # Kişi ve Pişirme Seçilmiş
            Veritabani.query('SELECT * FROM tarifler WHERE ad LIKE ? and kisisayisi = ? and pisirmesuresi = ?', (f"%{tarifisim}%", kisi, pisirme))
        elif kisi != 0 and pisirme == 0 and hazirlama != 0 and len(tarifisim) > 2:  # Kişi ve Hazırlama
            Veritabani.query('SELECT * FROM tarifler WHERE ad LIKE ? and kisisayisi = ? and hazirlamasuresi = ?', (f"%{tarifisim}%", kisi, hazirlama))
        elif kisi == 0 and pisirme != 0 and hazirlama != 0 and len(tarifisim) > 2:  # Hazırlama ve Pişirme
            Veritabani.query('SELECT * FROM tarifler WHERE ad LIKE ? and hazirlamasuresi = ? and pisirmesuresi = ?', (f"%{tarifisim}%", hazirlama, pisirme))

        sqlsonuc = Veritabani.fetchone()
        if sqlsonuc is None:
            return None
        
        return Tarif(*sqlsonuc)

    @staticmethod
    def ekle(tarifisim, hazirlama, pisirme, kisi, malzemeler, adimlar):
        Veritabani.query('INSERT INTO tarifler (ad, kisisayisi, hazirlamasuresi, pisirmesuresi, fotograf) VALUES(?, ?, ?, ?, ?)', (tarifisim, hazirlama, pisirme, kisi, "topluyemek.jpg"))
        Veritabani.query('SELECT id FROM Tarifler WHERE ad = ?', (tarifisim,))
        tarifid = Veritabani.fetchone()[0]
        for malzeme in malzemeler:
            Veritabani.query('INSERT INTO Malzemeler (TarifID, Malzeme) VALUES (?, ?)', (tarifid, malzeme))

        for adim in adimlar:
            Veritabani.query('INSERT INTO Asamalar (TarifID, Asama) VALUES (?, ?)', (tarifid, adim))
