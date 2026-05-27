from __future__ import annotations

import argparse
from pathlib import Path

from excel_image_matcher_cli.matcher import match_images


def main() -> int:
    parser = argparse.ArgumentParser(description="Match spreadsheet rows to image files.")
    parser.add_argument("--input", required=True, help="Input CSV file")
    parser.add_argument("--images", required=True, help="Directory containing image files")
    parser.add_argument("--key-column", default="image_key", help="CSV column used to match image names")
    parser.add_argument("--output-dir", default="outputs", help="Output directory")
    parser.add_argument("--dry-run", action="store_true", help="Analyze only; still writes validation logs")
    args = parser.parse_args()

    result = match_images(
        input_csv=Path(args.input),
        image_dir=Path(args.images),
        key_column=args.key_column,
        output_dir=Path(args.output_dir),
        dry_run=args.dry_run,
    )
    print(f"Rows processed: {result.rows_processed}")
    print(f"Rows matched: {result.rows_matched}")
    print(f"Missing images: {result.missing_images}")
    print(f"Duplicate image keys: {result.duplicate_image_keys}")
    print(f"Outputs written to: {result.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
