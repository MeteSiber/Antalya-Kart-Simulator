import random
from time import sleep
Program = input("Programı Kullanabilmek icin Lütfen Parolayı Giriniz» ")
if Program == "metesber2023" or Program == "Metesber2023" or Program == "MeteSber2023":
    while True:
        bakiye = int(random.randint(1000,5000))
        print("""
        --------------------------------------------------------------
       | Otobüs Simulatörüne Hoşgeldiniz Yapmak istediğiniz işlem Nedir |
       |                                                                |
       | 1. Kart Alma                                                   |
       |                                                                |
       | 2. Bakiyeniz                                                   |
       |                                                                |
       | 3. Kart a Para Yatırma                                         |
       |                                                                |            
       | 4. Kart Bakiye Kontrolü (Kart Varsa!!!)                        |
       |                                                                |            
       | 5. Kartı iptal Ettirme (Kart Varsa!!!)                         |    
       |                                                                |    
       | Programdan Çıkmak İstiyorsan 'Çıkış' Komudu'nu Kullanın        |
        ----------------------------------------------------------------|
        """)
        while True:
            islem = input("Lütfen Yapmak İstediğiniz İşlemi Giriniz» ")
            if islem == "Çıkış":
                exit("Oynadığınız için Teşekkürler Developer: Mete Tunç")
            elif islem != "1":
                print("Yanlış İşlem Yaptınız İşlem Yapmak İçin Kart Almalısınız!!!")
            else:
                print("Başarılı Bir Şekilde Kart Aldınız Son İşlemler Kaldı")
                Ad = input("Kart da Gözükmesini İstediğiniz Adınızı Giriniz(Minimum 7) » ")
                Tarih = input("Kart da Gözükmecek Doğum Tarihinizi Giriniz» ")
                print("""
                --------------------------------------------------------------------------------
               | Antalya                                                        Antalya |
               | BüyükŞehir                                                      Ulaşım |
               | Belediyesi                                                             |
               |                                                                        |
               | Kart Adınız » {}                                                  |  
               |                                                                        |  
               | Doğum Tarihiniz » {}                                           |
               |                                                                        |
                ------------------------------------------------------------------------
                """.format(Ad,Tarih))
                while True:
                    islem = input("Lütfen Yapmak İstediğiniz İşlemi Giriniz» ")   
                    if (islem == "Çıkış"):
                        exit("Başarılı Bir Şekilde Çıkış Yaptınız")
                    elif (islem == "2"):           
                        print("Bakiyeniz Şuanda",bakiye,"TL Dir")
                    elif (islem == "3"):
                        bakiye2 = int(input("Kartınıza Para Yatırmak istediğiniz Değeri Giriniz» "))
                        bakiye -= bakiye2
                        if (bakiye - bakiye2 <= 0):
                            print("Olmayan Parayı Yatıramazsınız") 
                    elif (islem == "4"):
                        kontrol = print("Bakiyeniz Şuanda {} TL Dir".format(bakiye2))
                    elif (islem == "5"):
                        onay = input("Kartı iptal Ettirmek istediğinize Eminmisiniz» ")
                        if onay == "evet" or onay == "Evet":
                            onay2 = input("Tekrar Oynamak istermisiniz» ")
                            if onay2 == "evet" or onay2 == "Evet":
                                break
                            else:
                                exit("Oynadığın İçin Teşekkürler Developer: Mete Tunç")
                        else:
                            break