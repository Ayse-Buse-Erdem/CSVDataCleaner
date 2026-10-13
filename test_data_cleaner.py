import unittest

import pandas as pd

from data_analysis import calculate_statistics, create_category_summary
from data_cleaner import clean_data


class TestCSVDataCleaner(unittest.TestCase):

    def setUp(self):
        self.sample_data = pd.DataFrame(
            {
                "ProductID": [1, 2, 2, 3],
                "ProductName": ["Laptop", "Mouse", "Mouse", None],
                "Category": [
                    "Electronics",
                    "Electronics",
                    "Electronics",
                    "Furniture",
                ],
                "Price": [30000, 500, 500, None],
                "Stock": [10, 20, 20, None],
            }
        )

    def test_duplicate_records_are_removed(self):
        cleaned_data = clean_data(self.sample_data)

        self.assertEqual(len(cleaned_data), 3)

    def test_missing_values_are_filled(self):
        cleaned_data = clean_data(self.sample_data)

        self.assertEqual(cleaned_data.isnull().sum().sum(), 0)
        self.assertEqual(
            cleaned_data.loc[3, "ProductName"],
            "Unknown",
        )

    def test_statistics_are_calculated(self):
        cleaned_data = clean_data(self.sample_data)
        statistics = calculate_statistics(cleaned_data)

        self.assertEqual(statistics["Toplam ürün sayısı"], 3)
        self.assertGreater(statistics["Ortalama fiyat"], 0)
        self.assertGreater(statistics["Toplam stok"], 0)

    def test_category_summary_is_created(self):
        cleaned_data = clean_data(self.sample_data)
        summary = create_category_summary(cleaned_data)

        self.assertIn("Electronics", summary.index)
        self.assertIn("Furniture", summary.index)


if __name__ == "__main__":
    unittest.main()