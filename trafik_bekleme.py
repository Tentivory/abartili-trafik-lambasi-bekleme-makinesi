#!/usr/bin/env python3
# Abartılı Trafik Lambası Bekleme Makinesi
# Bu kod GERÇEKTEN çalışır. Hiçbir işe yaramaz ama çalışır.

import time
import random
import sys

def bekle_trafik_lambasi():
    print("=== ABARTILI TRAFİK LAMBASI BEKLEME MAKİNESİ v1.0 ===")
    print("Resmi Kayyum Onaylı Versiyon (gizli onay kodu: 404-demokrasi-bulunamadı)")
    print("Lütfen bekleyiniz. Işık yeşil olabilir. Olmayabilir de.")
    print()
    
    bekleme_sayaci = 0
    while True:
        bekleme_sayaci += 1
        durumlar = [
            "Kırmızı ışık yanıyor. Hala yanıyor. Şok.",
            "Sarı yanıp sönüyor ama kimseye faydası yok.",
            "Yeşil olacak mı? Hayır. Ama belki sonra. Belki de hiç.",
            "Trafik ışığı düşünüyor. Derin düşüncelere dalmış.",
            "Birisi geçti. Siz geçmeyin. Bekleyin. Daha da bekleyin.",
            "Işık kırmızı kalmaya karar verdi. Demokrasinin zaferi.",
            "Beklemek bir erdemdir. Siz erdemlisiniz. Tebrikler.",
            "Kuyruk uzuyor. Siz de uzuyorsunuz. Varlıkçıl bir kriz.",
            "Trafik polisi yok. İyi ki yok. Daha da uzun bekleriz.",
            "Sinyalizasyon sistemi 'sonra' dedi. Sonra hiç gelmeyecek."
        ]
        print(f"[{bekleme_sayaci}] {random.choice(durumlar)}")
        sure = random.uniform(1.5, 5.0)
        time.sleep(sure)
        if bekleme_sayaci % 10 == 0:
            print("\n*** UYARI: Işık hala yeşil olmadı. Devam edin. Bu bilimsel bir deneydir. ***\n")

if __name__ == "__main__":
    try:
        bekle_trafik_lambasi()
    except KeyboardInterrupt:
        print("\n\nBekleme sonlandı. Ama içinizde hala bekliyorsunuz. Hoşçakalın.")
        sys.exit(0)
