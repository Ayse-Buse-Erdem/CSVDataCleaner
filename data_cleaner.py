from pathlib import Path

import pandas as pd


def load_csv(file_path):
    """CSV dosyasını okur ve veri tablosunu döndürür."""
    path = Path(file_path)

    if not path.exists():
        print(f"Hata: '{file_path}' dosyası bulunamadı.")
        return None

    try:
        data = pd.read_csv(path)
        print("CSV dosyası başarıyla okundu.")
        return data
    except pd.errors.EmptyDataError:
        print("Hata: CSV dosyası boş.")
    except pd.errors.ParserError:
        print("Hata: CSV dosyasının biçimi geçersiz.")
    except Exception as error:
        print(f"Beklenmeyen hata: {error}")

    return None


def inspect_data(data):
    """Eksik ve tekrarlanan kayıtları inceler."""
    print("\n--- VERİ İNCELEME SONUÇLARI ---")
    print(f"Toplam satır sayısı: {len(data)}")
    print(f"Toplam sütun sayısı: {len(data.columns)}")
    print(f"Tekrarlanan satır sayısı: {data.duplicated().sum()}")

    print("\nSütunlara göre eksik değerler:")
    print(data.isnull().sum())


def clean_data(data):
    """Eksik ve tekrarlanan kayıtları temizler."""
    cleaned_data = data.copy()

    # Tekrarlanan satırları kaldır
    cleaned_data = cleaned_data.drop_duplicates()

    # Sayısal sütunlardaki eksik değerleri sütun ortalamasıyla doldur
    numeric_columns = cleaned_data.select_dtypes(include="number").columns

    for column in numeric_columns:
        mean_value = cleaned_data[column].mean()
        cleaned_data[column] = cleaned_data[column].fillna(mean_value)

    # Metin sütunlarındaki eksik değerleri Unknown ile doldur
    text_columns = cleaned_data.select_dtypes(include="object").columns

    for column in text_columns:
        cleaned_data[column] = cleaned_data[column].fillna("Unknown")

    return cleaned_data


def save_cleaned_data(data, output_path):
    """Temizlenen verileri yeni bir CSV dosyasına kaydeder."""
    data.to_csv(output_path, index=False)
    print(f"\nTemizlenen veriler '{output_path}' dosyasına kaydedildi.")


def main():
    input_file = "sample_data.csv"
    output_file = "cleaned_data.csv"

    data = load_csv(input_file)

    if data is None:
        return

    inspect_data(data)
    cleaned_data = clean_data(data)
    save_cleaned_data(cleaned_data, output_file)

    print("\n--- TEMİZLEME SONRASI ---")
    print(f"Kalan satır sayısı: {len(cleaned_data)}")
    print(f"Eksik değer sayısı: {cleaned_data.isnull().sum().sum()}")


if __name__ == "__main__":
    main()