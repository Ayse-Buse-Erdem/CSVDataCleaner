from pathlib import Path

import pandas as pd


def load_cleaned_data(file_path):
    """Temizlenmiş CSV dosyasını okur."""
    path = Path(file_path)

    if not path.exists():
        print("Hata: Önce data_cleaner.py dosyasını çalıştırmalısınız.")
        return None

    try:
        return pd.read_csv(path)
    except Exception as error:
        print(f"Dosya okunurken hata oluştu: {error}")
        return None


def calculate_statistics(data):
    """Ürün verileri için genel istatistikleri hesaplar."""
    statistics = {
        "Toplam ürün sayısı": len(data),
        "Ortalama fiyat": data["Price"].mean(),
        "En düşük fiyat": data["Price"].min(),
        "En yüksek fiyat": data["Price"].max(),
        "Toplam stok": data["Stock"].sum(),
        "Ortalama stok": data["Stock"].mean(),
    }

    return statistics


def create_category_summary(data):
    """Ürünleri kategorilerine göre özetler."""
    summary = data.groupby("Category").agg(
        ProductCount=("ProductID", "count"),
        AveragePrice=("Price", "mean"),
        TotalStock=("Stock", "sum"),
    )

    return summary.round(2)


def save_report(statistics, category_summary, output_path):
    """Analiz sonuçlarını metin raporuna kaydeder."""
    with open(output_path, "w", encoding="utf-8") as report:
        report.write("CSV VERİ ANALİZ RAPORU\n")
        report.write("=" * 35 + "\n\n")

        report.write("GENEL İSTATİSTİKLER\n")
        report.write("-" * 25 + "\n")

        for title, value in statistics.items():
            if isinstance(value, float):
                report.write(f"{title}: {value:.2f}\n")
            else:
                report.write(f"{title}: {value}\n")

        report.write("\nKATEGORİ BAZLI ÖZET\n")
        report.write("-" * 25 + "\n")
        report.write(category_summary.to_string())

    print(f"Analiz raporu '{output_path}' dosyasına kaydedildi.")


def main():
    input_file = "cleaned_data.csv"
    report_file = "analysis_report.txt"
    summary_file = "category_summary.csv"

    data = load_cleaned_data(input_file)

    if data is None:
        return

    statistics = calculate_statistics(data)
    category_summary = create_category_summary(data)

    print("\n--- GENEL İSTATİSTİKLER ---")
    for title, value in statistics.items():
        if isinstance(value, float):
            print(f"{title}: {value:.2f}")
        else:
            print(f"{title}: {value}")

    print("\n--- KATEGORİ BAZLI ÖZET ---")
    print(category_summary)

    category_summary.to_csv(summary_file)
    save_report(statistics, category_summary, report_file)

    print(f"Kategori özeti '{summary_file}' dosyasına kaydedildi.")


if __name__ == "__main__":
    main()