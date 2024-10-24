# Star TV İndirici

Bu Python scripti, Star TV dizilerini indirmek için kullanılır. Kullanıcıdan dizi linki, başlangıç bölümü ve bitiş bölümünü alarak belirtilen bölümleri mp4 formatında indirir.

## Özellikler
- Kullanıcıdan dizi linkini alır.
- Belirtilen bölüm aralığındaki dizileri indirir.
- İndirilen dosyaları dizi adıyla oluşturulan bir klasöre kaydeder.

## Gereksinimler

Bu scripti çalıştırmak için aşağıdaki Python modüllerine ihtiyacınız var:

- `requests`: HTTP istekleri yapmak için.
- `beautifulsoup4`: HTML ve XML dosyalarını ayrıştırmak için.
- `subprocess`: Sistem komutlarını çalıştırmak için.

## Kurulum

1. **Gerekli Python modüllerini yükleyin:**

   Terminal veya komut istemcisini açın ve aşağıdaki komutları girin:

   ```bash
   pip install requests beautifulsoup4
   ```

2. **Scripti indirin:**

   GitHub deposundan script dosyasını indirin veya kopyalayın.

3. **Scripti çalıştırın:**

   Scripti çalıştırmak için terminal veya komut istemcisinde şu komutu kullanın:

   ```bash
   python startv_indirici.py
   ```

4. **Gerekli bilgileri girin:**

   Script çalıştırıldığında sizden aşağıdaki bilgileri isteyecektir:
   - Star TV Dizi linki (örneğin: `https://www.startv.com.tr/dizi/genis-aile`)
   - Başlangıç bölümü (örneğin: `59`)
   - Bitiş bölümü (örneğin: `108`)

## Kullanım

Script çalışmaya başladığında, belirtilen bölüm aralığındaki dizileri indirir ve dizi adıyla oluşturulan klasöre kaydeder.

## Lisans

Bu proje MIT lisansı ile lisanslanmıştır.
