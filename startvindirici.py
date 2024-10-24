import os
import requests
from bs4 import BeautifulSoup
import json
import subprocess

# Kullanıcıdan bilgileri al
web_page_url = input("Star TV Dizi linkini girin (örneğin: https://www.startv.com.tr/dizi/genis-aile): ")
start_bölüm = int(input("Başlangıç bölümünü girin: "))
end_bölüm = int(input("Bitiş bölümünü girin: "))

# Dizi adını URL'den alma
dizi_adi = web_page_url.rstrip('/').split('/')[-1]  # URL sonundaki kısımdan dizi adını al

# Dizi adı ile klasör oluştur
dizi_klasörü = dizi_adi.replace(" ", "_")  # Klasör adı için boşlukları alt çizgi ile değiştir
if not os.path.exists(dizi_klasörü):
    os.makedirs(dizi_klasörü)  # Dizi klasörünü oluştur

# Bölüm aralığında döngü başlat
for bölüm_numarası in range(start_bölüm, end_bölüm + 1):
    print(f"{bölüm_numarası}. bölüm için işleme alınıyor...")

    # Bölüm sayfası URL'sini oluştur
    bölüm_url = f"{web_page_url}/bolumler/{bölüm_numarası}-bolum"

    # Web sayfasından meta verilerini bulmak
    page_response = requests.get(bölüm_url)
    soup = BeautifulSoup(page_response.content, "html.parser")

    # Meta etiketini bul
    meta_tag = soup.select_one("meta[property='dyg:tags']")
    bölüm_adi = None
    bölüm_kodu = None

    if meta_tag and 'content' in meta_tag.attrs:
        content = meta_tag['content']
        
        # İçerikten bölüm adı ve bölüm kodunu ayıklamak
        parts = content.split(',')
        if len(parts) >= 3:
            bölüm_adi = parts[1].replace("-", ".")  # 59-Bolum -> 59.Bölüm
            bölüm_kodu = parts[2]  # 30406

            # API çağrısı yap ve JSON verisini al
            api_url = f"https://dygvideo.dygdigital.com/api/video_info?akamai=true&PublisherId=1&ReferenceId=StarTv_{bölüm_kodu}&SecretKey=NtvApiSecret2014*"
            api_response = requests.get(api_url)

            if api_response.status_code == 200:
                json_data = api_response.json()
                # JSON verisinden gerekli indirme linkini al
                download_link = json_data['data']['flavors']['hls']  # HLS linkini alıyoruz
                
                # Dosya adını ayarlama
                file_name = f"{bölüm_adi}.mp4"  # Dosya adını oluştur ve mp4 uzantısını kullan
                file_path = os.path.join(dizi_klasörü, file_name)  # Klasör ile dosya yolunu birleştir
                print(f"İndirilen dosya adı: {file_path}")

                # ffmpeg ile dosyayı mp4 formatında indirme
                ffmpeg_command = [
                    'ffmpeg',
                    '-i', download_link,
                    '-c', 'copy',
                    file_path  # MP4 dosyasını kaydet
                ]
                
                # Komutu çalıştır
                subprocess.run(ffmpeg_command)
                print(f"{file_path} başarıyla indirildi.")
            else:
                print("API isteği başarısız oldu:", api_response.status_code)
        else:
            print("Bölüm adı ve kodu bulunamadı. Lütfen kontrol edin:", content)
    else:
        print("Meta etiketi bulunamadı veya içerik yok.")
