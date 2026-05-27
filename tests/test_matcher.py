from pathlib import Path
import unittest

from excel_image_matcher_cli.matcher import match_images


class ImageMatcherTest(unittest.TestCase):
    def test_match_images_reports_missing_row(self) -> None:
        root = Path(__file__).resolve().parents[1]
        output_dir = root / "outputs" / "test-run"
        result = match_images(
            input_csv=root / "examples" / "input" / "products.csv",
            image_dir=root / "examples" / "images",
            key_column="image_key",
            output_dir=output_dir,
        )
        self.assertEqual(result.rows_processed, 4)
        self.assertEqual(result.rows_matched, 3)
        self.assertEqual(result.missing_images, 1)
        self.assertTrue((output_dir / "matched_rows.csv").exists())


if __name__ == "__main__":
    unittest.main()
