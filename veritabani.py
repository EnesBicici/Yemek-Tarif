import sqlite3

class veritabani:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tarifler'")
        tablo_var_mi = self.cursor.fetchone()

        if not tablo_var_mi:  # Tablo yok
            self.cursor.execute('CREATE TABLE IF NOT EXISTS tarifler (ID INTEGER PRIMARY KEY AUTOINCREMENT, Ad TEXT, KisiSayisi INTEGER, HazirlamaSuresi INTEGER, PisirmeSuresi INTEGER, Fotograf TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS kullanicilar (ID INTEGER PRIMARY KEY AUTOINCREMENT, kullaniciadi TEXT, sifre TEXT, ad TEXT, soyad TEXT, telefon TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS malzemeler (ID INTEGER PRIMARY KEY AUTOINCREMENT, TarifID INTEGER, Malzeme TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS asamalar (ID INTEGER PRIMARY KEY AUTOINCREMENT, TarifID INTEGER, Asama TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS degerlendirmeler (ID INTEGER PRIMARY KEY AUTOINCREMENT, TarifID INTEGER,KullaniciID INTEGER, Puan INTEGER)')


            tarifler_data = [
                ("Fırında Patatesli Tavuk", 5, 15, 30, "tavuk.jpg"),
                ("Tahinli Kurabiye", 8, 10, 15, "kurabiye.jpg"),
                ("Şekerpare", 10, 15, 20, "sekerpare.jpg")
            ]

            malzemeler_data = [
                # Fırında Patatesli Tavuk
                (1, "<b>6 adet</b> tavuk"),
                (1, "<b>2 adet orta boy</b> patates"),
                (1, "<b>1 adet büyük boy</b> domates"),
                (1, "<b>1 adet</b> biber"),
                (1, "<b>2 diş</b> sarımsak"),
                (1, "<b>1 çay bardağı</b> zeytinyağı"),
                (1, "<b>1 tatlı kaşığı</b> kırmızı biber"),
                (1, "<b>1 yemek kaşığı</b> yoğurt"),
                # Tahinli Kurabiye
                (2, "<b>1 su bardağı</b> tahin"),
                (2, "<b>1 su bardağı</b> pudra şekeri"),
                (2, "<b>1 su bardağı</b> sıvı yağ"),
                (2, "<b>4 su bardağı</b> un"),
                (2, "<b>1 adet</b> vanilya"),
                (2, "<b>1 adet</b> kabartma tozu"),
                # Şekerpare
                (3, "<b>180 gram</b> tereyağı"),
                (3, "<b>4 su bardağı</b> un"),
                (3, "<b>5 yemek kaşığı</b> irmik"),
                (3, "<b>2 adet</b> yumurta"),
                (3, "<b>1 paket</b> vanilya"),
                (3, "<b>1 paket</b> kabartma tozu"),
                (3, "<b>2 su bardağı</b> şerbet"),
                (3, "<b>100 gram</b> badem veya fındık")
            ]

            asamalar_data = [
                # Fırında Patatesli Tavuk
                (1, "Sos için gerekli tüm malzemeleri bir kabın içerisine ekleyin."),
                (1, "Güzelce karıştırın."),
                (1, "Tavukları bir borcama ya da ısıya dayanıklı fırın kabına dizin."),
                (1, "Ardından üzerine sosu gezdirin."),
                (1, "Elma şeklinde dilimlediğiniz patatesleri dizin."),
                (1, "Ardından üzerine domates ve biberleri de dizin."),
                (1, "Tavukların kenarından suyu da ilave edin."),
                (1, "Tavukların üzeri kızarana kadar 35-40 dakika kadar pişirin."),
                (1, "Pişince çıkarıp sıcak sıcak servis edin."),
                # Tahinli Kurabiye
                (2, "Malzemeleri bir araya getirin ve güzelce karıştırın."),
                (2, "Azar azar unu ilave ederek yoğurun."),
                (2, "Hamurdan küçük parçalar koparıp yuvarlayın."),
                (2, "Fırında 180 derecede 15 dakika kadar pişirin."),
                (2, "Fırından çıkınca bir süre soğumaya bırakın."),
                # Şekerpare
                (3, "Tereyağı ve şekeri krema kıvamına gelene kadar çırpın."),
                (3, "Yumurtaları ve vanilyayı ekleyin, iyice karıştırın."),
                (3, "İrmik, un ve kabartma tozunu ayrı bir kapta karıştırın."),
                (3, "Kuru malzemeleri yavaşça ıslak karışıma ekleyip yoğurun."),
                (3, "Hamurdan ceviz büyüklüğünde parçalar koparıp yuvarlayın."),
                (3, "Her birine badem ya da fındık batırıp yağlı tepsiye dizin."),
                (3, "180 derecede 20-25 dakika pişirin."),
                (3, "Fırından çıkanlara sıcakken şerbet dökün."),
                (3, "Servisten önce üzerine hindistancevizi serpin.")
            ]



            self.cursor.executemany('INSERT INTO Tarifler (Ad, KisiSayisi, HazirlamaSuresi, PisirmeSuresi, Fotograf) VALUES (?, ?, ?, ?, ?)', tarifler_data)
            self.cursor.executemany('INSERT INTO Malzemeler (TarifID, Malzeme) VALUES (?, ?)', malzemeler_data)
            self.cursor.executemany('INSERT INTO Asamalar (TarifID, Asama) VALUES (?, ?)', asamalar_data)
            self.cursor.execute("INSERT INTO kullanicilar (kullaniciadi, sifre, ad, soyad, telefon) VALUES ('enes', '123', 'Enes', 'Biçici', '5323184256')")
            self.connection.commit()

    def query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()
        return self.cursor
    
    def fetchall(self):
        return self.cursor.fetchall()
    
    def fetchone(self):
        return self.cursor.fetchone()
    
Veritabani = veritabani('sql.db')
