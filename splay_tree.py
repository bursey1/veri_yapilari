class Dugum:
    """Splay Tree için düğüm sınıfı"""
    def __init__(self, anahtar):
        self.anahtar = anahtar  # Düğümün değeri
        self.sol = None  # Sol çocuk
        self.sag = None  # Sağ çocuk
        self.ebeveyn = None  # Ebeveyn düğüm


class SplayAgaci:
    """Splay Tree veri yapısı implementasyonu"""
    
    def __init__(self):
        self.kok = None  # Ağacın kök düğümü
    
    def _sola_dondur(self, yukari_cikacak):
        """
        Sol rotasyon işlemi
        yukari_cikacak: Yukarı çıkarılacak düğüm (ebeveyninin yerine geçecek)
        Bu düğüm ebeveyninin SAĞ çocuğu olmalıdır
        
        Örnek:
           ebeveyn              yukari_cikacak
           /    \               /         \
          A   yukari_cikacak   ebeveyn     C
              /    \           /    \
             B      C         A      B
        """
        yukariya = yukari_cikacak  # Yukarı çıkacak düğüm
        asagiya = yukariya.ebeveyn  # Aşağı inecek düğüm
        
        asagiya.sag = yukariya.sol  # Yukarıya'nın sol alt ağacı, aşağıya'nın sağ alt ağacı olur
        
        if yukariya.sol:
            yukariya.sol.ebeveyn = asagiya  # Alt ağacın ebeveynini güncelle
        
        yukariya.ebeveyn = asagiya.ebeveyn  # Yukarıya'nın ebeveyni, aşağıya'nın ebeveyni olur
        
        # Aşağıya'nın ebeveynine göre bağlantıları güncelle
        if not asagiya.ebeveyn:
            self.kok = yukariya  # Aşağıya kök ise, yukarıya yeni kök olur
        elif asagiya == asagiya.ebeveyn.sol:
            asagiya.ebeveyn.sol = yukariya  # Aşağıya sol çocuk ise, yukarıya sol çocuk olur
        else:
            asagiya.ebeveyn.sag = yukariya  # Aşağıya sağ çocuk ise, yukarıya sağ çocuk olur
        
        yukariya.sol = asagiya  # Aşağıya, yukarıya'nın sol çocuğu olur
        asagiya.ebeveyn = yukariya  # Aşağıya'nın ebeveyni yukarıya olur
    
    def _saga_dondur(self, yukari_cikacak):
        """
        Sağ rotasyon işlemi
        yukari_cikacak: Yukarı çıkarılacak düğüm (ebeveyninin yerine geçecek)
        Bu düğüm ebeveyninin SOL çocuğu olmalıdır
        
        Örnek:
              ebeveyn           yukari_cikacak
              /    \            /         \
       yukari_cikacak C        A        ebeveyn
          /    \                        /    \
         A      B                      B      C
        """
        yukariya = yukari_cikacak  # Yukarı çıkacak düğüm
        asagiya = yukariya.ebeveyn  # Aşağı inecek düğüm
        
        asagiya.sol = yukariya.sag  # Yukarıya'nın sağ alt ağacı, aşağıya'nın sol alt ağacı olur
        
        if yukariya.sag:
            yukariya.sag.ebeveyn = asagiya  # Alt ağacın ebeveynini güncelle
        
        yukariya.ebeveyn = asagiya.ebeveyn  # Yukarıya'nın ebeveyni, aşağıya'nın ebeveyni olur
        
        # Aşağıya'nın ebeveynine göre bağlantıları güncelle
        if not asagiya.ebeveyn:
            self.kok = yukariya  # Aşağıya kök ise, yukarıya yeni kök olur
        elif asagiya == asagiya.ebeveyn.sag:
            asagiya.ebeveyn.sag = yukariya  # Aşağıya sağ çocuk ise, yukarıya sağ çocuk olur
        else:
            asagiya.ebeveyn.sol = yukariya  # Aşağıya sol çocuk ise, yukarıya sol çocuk olur
        
        yukariya.sag = asagiya  # Aşağıya, yukarıya'nın sağ çocuğu olur
        asagiya.ebeveyn = yukariya  # Aşağıya'nın ebeveyni yukarıya olur
    
    def _splay(self, dugum):
        """
        Splay operasyonu - verilen düğümü köke getirir
        Üç durum vardır: Zig, Zig-Zig ve Zig-Zag
        """
        while dugum.ebeveyn:  # Düğüm kök olana kadar devam et
            ebeveyn = dugum.ebeveyn  # Ebeveyn düğüm
            buyukebeveyn = ebeveyn.ebeveyn  # Büyükebeveyn düğüm
            
            if not buyukebeveyn:
                # ZIG durumu: Sadece bir rotasyon gerekli (düğüm kökün çocuğu)
                if dugum == ebeveyn.sol:
                    self._saga_dondur(dugum)  # Düğüm sola, sağa döndür
                else:
                    self._sola_dondur(dugum)  # Düğüm sağa, sola döndür
            
            elif dugum == ebeveyn.sol and ebeveyn == buyukebeveyn.sol:
                # ZIG-ZIG durumu (sol-sol): İki sağa rotasyon
                # Önce ebeveyn yukarı çık, sonra düğüm yukarı çık
                self._saga_dondur(ebeveyn)  # Önce ebeveyn
                self._saga_dondur(dugum)  # Sonra düğüm
            
            elif dugum == ebeveyn.sag and ebeveyn == buyukebeveyn.sag:
                # ZIG-ZIG durumu (sağ-sağ): İki sola rotasyon
                # Önce ebeveyn yukarı çık, sonra düğüm yukarı çık
                self._sola_dondur(ebeveyn)  # Önce ebeveyn
                self._sola_dondur(dugum)  # Sonra düğüm
            
            elif dugum == ebeveyn.sag and ebeveyn == buyukebeveyn.sol:
                # ZIG-ZAG durumu (sol-sağ): Sol sonra sağ rotasyon
                # Düğüm iki kez yukarı çıkar
                self._sola_dondur(dugum)  # Önce sol rotasyon (düğüm yukarı)
                self._saga_dondur(dugum)  # Sonra sağ rotasyon (düğüm tekrar yukarı)
            
            else:
                # ZIG-ZAG durumu (sağ-sol): Sağ sonra sol rotasyon
                # Düğüm iki kez yukarı çıkar
                self._saga_dondur(dugum)  # Önce sağ rotasyon (düğüm yukarı)
                self._sola_dondur(dugum)  # Sonra sol rotasyon (düğüm tekrar yukarı)
    
    def ekle(self, anahtar):
        """
        Yeni bir düğüm ekler ve onu köke splayler
        """
        # Standart BST ekleme işlemi
        yeni_dugum = Dugum(anahtar)  # Yeni düğüm oluştur
        
        if not self.kok:
            self.kok = yeni_dugum  # Ağaç boşsa, yeni düğüm kök olur
            return
        
        mevcut = self.kok  # Gezinme için başlangıç noktası
        
        while True:
            if anahtar < mevcut.anahtar:
                # Değer küçükse sola git
                if not mevcut.sol:
                    mevcut.sol = yeni_dugum  # Sol boşsa, ekle
                    yeni_dugum.ebeveyn = mevcut
                    break
                mevcut = mevcut.sol
            else:
                # Değer büyük veya eşitse sağa git
                if not mevcut.sag:
                    mevcut.sag = yeni_dugum  # Sağ boşsa, ekle
                    yeni_dugum.ebeveyn = mevcut
                    break
                mevcut = mevcut.sag
        
        # Eklenen düğümü köke splay et
        self._splay(yeni_dugum)
    
    def ara(self, anahtar):
        """
        Belirtilen anahtarı arar
        Bulunan düğümü köke splayler
        Bulunamazsa, en yakın düğümü splayler
        """
        if not self.kok:
            return None  # Ağaç boş
        
        mevcut = self.kok  # Arama başlangıcı
        son_ziyaret = None  # Son ziyaret edilen düğüm
        
        while mevcut:
            son_ziyaret = mevcut  # Son düğümü kaydet
            
            if anahtar == mevcut.anahtar:
                # Anahtar bulundu
                self._splay(mevcut)  # Bulunan düğümü splay et
                return mevcut
            elif anahtar < mevcut.anahtar:
                mevcut = mevcut.sol  # Sola git
            else:
                mevcut = mevcut.sag  # Sağa git
        
        # Anahtar bulunamadı, en yakın düğümü splay et
        if son_ziyaret:
            self._splay(son_ziyaret)
        
        return None
    
    def sil(self, anahtar):
        """
        Belirtilen anahtarı ağaçtan siler
        """
        dugum = self.ara(anahtar)  # Düğümü ara (ve splay et)
        
        if not dugum:
            return False  # Düğüm bulunamadı
        
        # Silme işlemi: düğümü köke splayledik
        if not dugum.sol:
            # Sol alt ağaç yoksa, sağ alt ağacı kök yap
            self.kok = dugum.sag
            if self.kok:
                self.kok.ebeveyn = None
        elif not dugum.sag:
            # Sağ alt ağaç yoksa, sol alt ağacı kök yap
            self.kok = dugum.sol
            if self.kok:
                self.kok.ebeveyn = None
        else:
            # Her iki alt ağaç da var
            # Sol alt ağacı kök yap
            sol_alt_agac = dugum.sol
            sag_alt_agac = dugum.sag
            
            self.kok = sol_alt_agac
            self.kok.ebeveyn = None
            
            # Sol alt ağacın en büyük elemanını bul (en sağdaki)
            en_buyuk = sol_alt_agac
            while en_buyuk.sag:
                en_buyuk = en_buyuk.sag
            
            # En büyük elemanı splay et
            self._splay(en_buyuk)
            
            # Sağ alt ağacı, yeni kökün sağ çocuğu yap
            self.kok.sag = sag_alt_agac
            sag_alt_agac.ebeveyn = self.kok
        
        return True
    
    def minimum_bul(self):
        """
        Ağaçtaki en küçük değeri bulur ve onu köke splayler
        """
        if not self.kok:
            return None
        
        mevcut = self.kok
        # En soldaki düğüme git
        while mevcut.sol:
            mevcut = mevcut.sol
        
        # En küçük düğümü splay et
        self._splay(mevcut)
        return mevcut.anahtar
    
    def maksimum_bul(self):
        """
        Ağaçtaki en büyük değeri bulur ve onu köke splayler
        """
        if not self.kok:
            return None
        
        mevcut = self.kok
        # En sağdaki düğüme git
        while mevcut.sag:
            mevcut = mevcut.sag
        
        # En büyük düğümü splay et
        self._splay(mevcut)
        return mevcut.anahtar
    
    def sirali_dolasma(self, dugum=None, sonuc=None):
        """
        Inorder (sıralı) dolaşma: Sol - Kök - Sağ
        Ağacı küçükten büyüğe sıralı şekilde döndürür
        """
        if sonuc is None:
            sonuc = []
            dugum = self.kok
        
        if dugum:
            self.sirali_dolasma(dugum.sol, sonuc)  # Sol alt ağaç
            sonuc.append(dugum.anahtar)  # Kök
            self.sirali_dolasma(dugum.sag, sonuc)  # Sağ alt ağaç
        
        return sonuc
    
    def oncelikli_dolasma(self, dugum=None, sonuc=None):
        """
        Preorder (öncelikli) dolaşma: Kök - Sol - Sağ
        """
        if sonuc is None:
            sonuc = []
            dugum = self.kok
        
        if dugum:
            sonuc.append(dugum.anahtar)  # Kök
            self.oncelikli_dolasma(dugum.sol, sonuc)  # Sol alt ağaç
            self.oncelikli_dolasma(dugum.sag, sonuc)  # Sağ alt ağaç
        
        return sonuc
    
    def sonraki_dolasma(self, dugum=None, sonuc=None):
        """
        Postorder (sonraki) dolaşma: Sol - Sağ - Kök
        """
        if sonuc is None:
            sonuc = []
            dugum = self.kok
        
        if dugum:
            self.sonraki_dolasma(dugum.sol, sonuc)  # Sol alt ağaç
            self.sonraki_dolasma(dugum.sag, sonuc)  # Sağ alt ağaç
            sonuc.append(dugum.anahtar)  # Kök
        
        return sonuc


# Örnek kullanım
if __name__ == "__main__":
    # Yeni bir Splay Tree oluştur
    agac = SplayAgaci()
    
    print("=== Splay Ağacı Örnek Kullanım ===\n")
    
    # Elemanları ekle
    print("Elemanlar ekleniyor: 10, 20, 30, 40, 50, 25")
    for anahtar in [10, 20, 30, 40, 50, 25]:
        agac.ekle(anahtar)
    
    print("Sıralı dolaşma:", agac.sirali_dolasma())
    print("Öncelikli dolaşma:", agac.oncelikli_dolasma())
    print("Sonraki dolaşma:", agac.sonraki_dolasma())
    print("Kök düğüm:", agac.kok.anahtar if agac.kok else None)
    print()
    
    # Arama işlemi
    print("30 aranıyor...")
    sonuc = agac.ara(30)
    print("Bulundu!" if sonuc else "Bulunamadı!")
    print("Arama sonrası kök:", agac.kok.anahtar)
    print()
    
    # Minimum ve maksimum bulma
    print("Minimum değer:", agac.minimum_bul())
    print("Min bulma sonrası kök:", agac.kok.anahtar)
    print()
    
    print("Maksimum değer:", agac.maksimum_bul())
    print("Max bulma sonrası kök:", agac.kok.anahtar)
    print()
    
    # Silme işlemi
    print("20 siliniyor...")
    agac.sil(20)
    print("Silme sonrası sıralı dolaşma:", agac.sirali_dolasma())
    print("Silme sonrası kök:", agac.kok.anahtar)
    print()
    
    print("40 aranıyor...")
    agac.ara(40)
    print("Arama sonrası kök:", agac.kok.anahtar)
    print()
    
    # Ağaç yapısını göster
    print("=== Detaylı Test ===")
    agac2 = SplayAgaci()
    elemanlar = [50, 30, 70, 20, 40, 60, 80]
    print(f"Elemanlar ekleniyor: {elemanlar}")
    for e in elemanlar:
        agac2.ekle(e)
        print(f"  {e} eklendi - Yeni kök: {agac2.kok.anahtar}")
    
    print("\nSon durum:")
    print("Sıralı dolaşma:", agac2.sirali_dolasma())
    print("Kök:", agac2.kok.anahtar)