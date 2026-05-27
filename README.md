# Excel Image Matcher CLI

A public-safe Python CLI that matches spreadsheet rows to image files, writes clean output CSV files, and produces validation logs.

This project is designed as a small freelance-ready automation demo. It uses synthetic sample rows and placeholder SVG images only.

## What It Shows

- Spreadsheet-style CSV processing
- Image matching by configurable key
- Missing image report
- Duplicate image report
- Dry-run mode
- Repeatable command-line workflow

## Quick Start

```bash
PYTHONPATH=src python3 -m excel_image_matcher_cli.cli \
  --input examples/input/products.csv \
  --images examples/images \
  --key-column image_key \
  --output-dir outputs
```

Generated files:

- `outputs/matched_rows.csv`
- `outputs/missing_images.csv`
- `outputs/duplicate_images.csv`
- `outputs/run_summary.md`

## Demo Data

All sample rows and images are synthetic. No customer, product, price, order, or private company data is included.

## Portfolio Summary

I built a Python automation tool that matches image files to spreadsheet rows, validates missing/duplicate files, and generates clean output logs for repeatable Excel/image workflows.

## Resume Bullet

- Built a public-safe Python CLI for spreadsheet image matching with configurable keys, validation logs, dry-run mode, and synthetic demo data for product/report automation workflows.
