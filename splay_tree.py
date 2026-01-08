class Dugum:
    def __init__(self, anahtar):
        self.anahtar = anahtar  
        self.sol = None  
        self.sag = None 
        self.ebeveyn = None  


class SplayAgaci:
    def __init__(self):
        self.kok = None  

    def _sola_dondur(self, yukari_cikacak):
       
        yukariya = yukari_cikacak  
        asagiya = yukariya.ebeveyn 
        
        asagiya.sag = yukariya.sol 
        
        if yukariya.sol:
            yukariya.sol.ebeveyn = asagiya  
        
        yukariya.ebeveyn = asagiya.ebeveyn  
        
        if not asagiya.ebeveyn:
            self.kok = yukariya  
        elif asagiya == asagiya.ebeveyn.sol:
            asagiya.ebeveyn.sol = yukariya  
        else:
            asagiya.ebeveyn.sag = yukariya  
        
        yukariya.sol = asagiya  
        asagiya.ebeveyn = yukariya  
    
    def _saga_dondur(self, yukari_cikacak):
        
        yukariya = yukari_cikacak  
        asagiya = yukariya.ebeveyn  
        
        asagiya.sol = yukariya.sag  
        
        if yukariya.sag:
            yukariya.sag.ebeveyn = asagiya 
        
        yukariya.ebeveyn = asagiya.ebeveyn  
        
        if not asagiya.ebeveyn:
            self.kok = yukariya  
        elif asagiya == asagiya.ebeveyn.sag:
            asagiya.ebeveyn.sag = yukariya  
        else:
            asagiya.ebeveyn.sol = yukariya  
        
        yukariya.sag = asagiya  
        asagiya.ebeveyn = yukariya 
    
    def _splay(self, dugum):
       
        while dugum.ebeveyn: 
            ebeveyn = dugum.ebeveyn  
            buyukebeveyn = ebeveyn.ebeveyn 
            
            if not buyukebeveyn:
                if dugum == ebeveyn.sol:
                    self._saga_dondur(dugum) 
                else:
                    self._sola_dondur(dugum)  
            
            elif dugum == ebeveyn.sol and ebeveyn == buyukebeveyn.sol:
              
                self._saga_dondur(ebeveyn) 
                self._saga_dondur(dugum)  
            
            elif dugum == ebeveyn.sag and ebeveyn == buyukebeveyn.sag:
            
                self._sola_dondur(ebeveyn)  
                self._sola_dondur(dugum)  
            
            elif dugum == ebeveyn.sag and ebeveyn == buyukebeveyn.sol:
    
                self._sola_dondur(dugum)  
                self._saga_dondur(dugum)  
            
            else:

                self._saga_dondur(dugum)  
                self._sola_dondur(dugum)  
    
    def ekle(self, anahtar):
    
    
        yeni_dugum = Dugum(anahtar) 
        
        if not self.kok:
            self.kok = yeni_dugum  
            return
        
        mevcut = self.kok  
        
        while True:
            if anahtar < mevcut.anahtar:
                if not mevcut.sol:
                    mevcut.sol = yeni_dugum  
                    yeni_dugum.ebeveyn = mevcut
                    break
                mevcut = mevcut.sol
            else:
                if not mevcut.sag:
                    mevcut.sag = yeni_dugum 
                    yeni_dugum.ebeveyn = mevcut
                    break
                mevcut = mevcut.sag
        
        self._splay(yeni_dugum)
    
    def ara(self, anahtar):
    
        if not self.kok:
            return None  
        
        mevcut = self.kok  
        son_ziyaret = None  
        
        while mevcut:
            son_ziyaret = mevcut  
            
            if anahtar == mevcut.anahtar:
                # Anahtar bulundu
                self._splay(mevcut) 
                return mevcut
            elif anahtar < mevcut.anahtar:
                mevcut = mevcut.sol  
            else:
                mevcut = mevcut.sag 
        
    
        if son_ziyaret:
            self._splay(son_ziyaret)
        
        return None
    
    def sil(self, anahtar):
       
        dugum = self.ara(anahtar)  
        
        if not dugum:
            return False 
        
       
        if not dugum.sol:
            
            self.kok = dugum.sag
            if self.kok:
                self.kok.ebeveyn = None
        elif not dugum.sag:
            
            self.kok = dugum.sol
            if self.kok:
                self.kok.ebeveyn = None
        else:
           
            sol_alt_agac = dugum.sol
            sag_alt_agac = dugum.sag
            
            self.kok = sol_alt_agac
            self.kok.ebeveyn = None
            
            en_buyuk = sol_alt_agac
            while en_buyuk.sag:
                en_buyuk = en_buyuk.sag
            
            self._splay(en_buyuk)
            
            self.kok.sag = sag_alt_agac
            sag_alt_agac.ebeveyn = self.kok
        
        return True

    def minimum_bul(self):
        if not self.kok:
            return None
        mevcut = self.kok
        while mevcut.sol:
            mevcut = mevcut.sol
        self._splay(mevcut)
        return mevcut.anahtar
    def maksimum_bul(self):
        if not self.kok:
            return None
        mevcut = self.kok
        while mevcut.sag:
            mevcut = mevcut.sag
        self._splay(mevcut)
        return mevcut.anahtar
    
    def sirali_dolasma(self, dugum=None, sonuc=None):
      
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
            sonuc.append(dugum.anahtar) 
            self.oncelikli_dolasma(dugum.sol, sonuc)  
            self.oncelikli_dolasma(dugum.sag, sonuc)
        
        return sonuc
    
    def sonraki_dolasma(self, dugum=None, sonuc=None):
        """
        Postorder (sonraki) dolaşma: Sol - Sağ - Kök
        """
        if sonuc is None:
            sonuc = []
            dugum = self.kok
        
        if dugum:
            self.sonraki_dolasma(dugum.sol, sonuc)  
            self.sonraki_dolasma(dugum.sag, sonuc)  
            sonuc.append(dugum.anahtar) 
        
        return sonuc



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
    
   
    print("30 aranıyor...")
    sonuc = agac.ara(30)
    print("Bulundu!" if sonuc else "Bulunamadı!")
    print("Arama sonrası kök:", agac.kok.anahtar)
    print()
    
    
    print("Minimum değer:", agac.minimum_bul())
    print("Min bulma sonrası kök:", agac.kok.anahtar)
    print()
    
    print("Maksimum değer:", agac.maksimum_bul())
    print("Max bulma sonrası kök:", agac.kok.anahtar)
    print()
    
    
    print("20 siliniyor...")
    agac.sil(20)
    print("Silme sonrası sıralı dolaşma:", agac.sirali_dolasma())
    print("Silme sonrası kök:", agac.kok.anahtar)
    print()
    
    print("40 aranıyor...")
    agac.ara(40)
    print("Arama sonrası kök:", agac.kok.anahtar)
    print()
    
   
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
