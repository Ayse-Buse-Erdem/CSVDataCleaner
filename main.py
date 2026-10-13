from data_cleaner import main as run_data_cleaner
from data_analysis import main as run_data_analysis


def main():
    print("=" * 45)
    print("CSV VERİ TEMİZLEME VE ANALİZ ARACI")
    print("=" * 45)

    print("\n1. Veri temizleme işlemi başlatılıyor...")
    run_data_cleaner()

    print("\n2. Veri analizi işlemi başlatılıyor...")
    run_data_analysis()

    print("\n" + "=" * 45)
    print("Bütün işlemler başarıyla tamamlandı.")
    print("=" * 45)


if __name__ == "__main__":
    main()