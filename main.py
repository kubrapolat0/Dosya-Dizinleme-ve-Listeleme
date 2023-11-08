import fitz
import os

def menu():
    print("HOŞGELDİNİZ!")
    print("MENÜ")
    print("1. PDF isimlerini göster")
    print("2. PDF dosyalarının başlıklarını yaz")
    print("3. Çıkış")

    seçim = input("Yapmak istediğiniz işlem nedir? ")

    return seçim

def pdf_listele():
    klasör_adi = "makale"
    dosyalar = os.listdir(klasör_adi)

    print("PDF dosyaları:")
    for dosya in dosyalar:
        if dosya.endswith(".pdf"):
            print(dosya)

def pdf_ilk_sayfa_basligi_al():
    klasör_adi = "makale"
    dosyalar = os.listdir(klasör_adi)

    for dosya in dosyalar:
        if dosya.endswith(".pdf"):
            pdf_dosya = fitz.open(os.path.join(klasör_adi, dosya))
            sayfa = pdf_dosya.load_page(0)  # İlk sayfayı yükle

            metin = sayfa.get_text()
            basliklar = [satir.strip() for satir in metin.split('\n') if satir.strip()]

            if basliklar:
                ilk_baslik = basliklar[0]
                print(f"{dosya} ilk sayfadaki başlık: {ilk_baslik}")
            else:
                print(f"{dosya} ilk sayfada başlık bulunamadı.")

if __name__ == "__main__":
    seçim = menu()

    while seçim != "3":
        if seçim == "1":
            pdf_listele()
        elif seçim == "2":
            pdf_ilk_sayfa_basligi_al()
        else:
            print("Geçersiz seçim.")

        seçim = menu()




