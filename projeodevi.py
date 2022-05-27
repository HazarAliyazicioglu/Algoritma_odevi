import sqlite3

vt = sqlite3.connect("projeodevi2.db")

cursor = vt.cursor()

def tabloolustur1():
    cursor.execute("CREATE TABLE IF NOT EXISTS kullanıcı_adı(kullanıcı_adı)")

def degerekle1():
    cursor.execute("INSERT INTO kullanıcı_adı VALUES ('admin')")
    vt.commit()
    
def tabloolustur2():
    cursor.execute("CREATE TABLE IF NOT EXISTS sifre(sifre)")

def degerekle2():
    cursor.execute("INSERT INTO sifre VALUES (123456)")
    vt.commit()
    vt.close()
    

tabloolustur1()
degerekle1()
tabloolustur2()
degerekle2()

import sqlite3

vt = sqlite3.connect("projeodevi.db")

cursor = vt.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS personel(ad TEXT, soyad TEXT, numara INT)")

def degerekle():
    cursor.execute("INSERT INTO personel VALUES ('Hazar','Aliyazıcıoğlu',1)")
    cursor.execute("INSERT INTO personel VALUES ('Emre','Öz',2)")
    cursor.execute("INSERT INTO personel VALUES ('Başar','Kurtuluş',3)")
    cursor.execute("INSERT INTO personel VALUES ('Selda','Kaçak',4)")
    cursor.execute("INSERT INTO personel VALUES ('Bülent','Varış',5)")
    vt.commit()
    vt.close()

tabloolustur()
degerekle()

class tip():
    isim = ""
    pozisyon=""


while (True):
    nesne = tip()
    nesne.isim = input("Adınızı Giriniz: ")
    nesne.pozisyon = input("Poziyonunuzu Giriniz: ")

    print("{} personelinin pozizyonu {}'dır".format(nesne.isim,nesne.pozisyon))
    sonuc = input("Devam etmek ister misiniz? (e/h)")

    if (sonuc == "h"):
        break



def sistem_calisma():
    while True :
        
        secenek = input("Yapmak istediğiniz seçeneği seçiniz: ")
        
        if secenek == "1" :
            
            print("\nHesap Sistemine HoşgeLdiniz !!!")
            
            calisanlar = []
            
            maaslar = []
            
            for i in range(0,5,1) :

                i = input("Çalışanın numarasını giriniz: ")

                sözlük1={"1":"Hazar","2":"Emre","3":"Başar","4":"Selda","5":"Bülent"}

                calisan= sözlük1.get(i)
                
                calisanlar.append(calisan)
                
                aylık_brut_maas = 5400
                
                prim = 20
                    
                satis_miktari = input("Aylık yapıLan satış miktarını giriniz:")
               
                satis_miktari = int(satis_miktari)
                
                if satis_miktari < 15:
                        
                    maas = aylık_brut_maas
                        
                    maaslar.append(maas)
                elif satis_miktari > 15:
                        
                    carpan = satis_miktari/5
                        
                    maas = aylık_brut_maas + (prim * carpan)
                       
                    maaslar.append(maas)
                    
            
            for x in range(0,5,1):
                    
                print("Çalışan {}  maaş {}".format(calisanlar[x],maaslar[x]))
            
            break
        elif secenek == "2":
            
            print("\nİyi Günler DiLeriz")
            
            break
        else :
            print ("\nGeçerli seçenek numarası girişi yapınız")
            
            break


def sistem_giris():
    merhaba = "SİSTEME HOŞGELDİNİZ"
    try:
        merhaba = int(merhaba)
    except:
        print(merhaba)

sistem_giris()
#Kullanıcı adı: admin
#şifre: 123456
kullanıcı_adı = str(input("Kullanıcı adınızı giriniz: "))
try:
    if kullanıcı_adı == "admin":
        print("Geçerli kullanıcı adı")
    else:
        print("Geçersiz kullanıcı adı")
except:
    print("Geçersiz kullanıcı adı")
        
       

sifre = input("Şifreyi giriniz: ")
try:
    if sifre == "123456":
        print("Geçerli şifre")
    else:
        print("Geçersiz şifre")
except:
    print("Geçersiz şifre")

while True:    
    if kullanıcı_adı == "admin" and sifre == "123456":
        print("\nGiriş Başarılı")
        sistem_calisma()
        break
    else:
        print("Tekrar Deneyiniz")
        break