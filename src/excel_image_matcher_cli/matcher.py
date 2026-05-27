from __future__ import annotations

import csv
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}


@dataclass(frozen=True)
class MatchResult:
    rows_processed: int
    rows_matched: int
    missing_images: int
    duplicate_image_keys: int
    output_dir: Path


def match_images(
    input_csv: Path,
    image_dir: Path,
    key_column: str,
    output_dir: Path,
    dry_run: bool = False,
) -> MatchResult:
    output_dir.mkdir(parents=True, exist_ok=True)
    image_index, duplicates = build_image_index(image_dir)

    with input_csv.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames:
            raise ValueError("Input CSV has no header row")
        if key_column not in reader.fieldnames:
            raise ValueError(f"Missing key column: {key_column}")
        rows = [dict(row) for row in reader]

    matched_rows: list[dict[str, str]] = []
    missing_rows: list[dict[str, str]] = []

    for row in rows:
        key = normalize_key(row.get(key_column, ""))
        image_path = image_index.get(key)
        output_row = dict(row)
        output_row["matched_image_path"] = str(image_path) if image_path else ""
        output_row["match_status"] = "matched" if image_path else "missing"
        matched_rows.append(output_row)
        if not image_path:
            missing_rows.append(output_row)

    write_csv(output_dir / "matched_rows.csv", matched_rows, extra_fields=["matched_image_path", "match_status"])
    write_csv(output_dir / "missing_images.csv", missing_rows, extra_fields=["matched_image_path", "match_status"])
    write_duplicate_report(output_dir / "duplicate_images.csv", duplicates)
    write_summary(output_dir / "run_summary.md", rows, matched_rows, missing_rows, duplicates, dry_run)

    return MatchResult(
        rows_processed=len(rows),
        rows_matched=len(rows) - len(missing_rows),
        missing_images=len(missing_rows),
        duplicate_image_keys=len(duplicates),
        output_dir=output_dir,
    )


def build_image_index(image_dir: Path) -> tuple[dict[str, Path], dict[str, list[Path]]]:
    grouped: dict[str, list[Path]] = defaultdict(list)
    for path in image_dir.rglob("*"):
        if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES:
            grouped[normalize_key(path.stem)].append(path)

    index: dict[str, Path] = {}
    duplicates: dict[str, list[Path]] = {}
    for key, paths in grouped.items():
        sorted_paths = sorted(paths)
        index[key] = sorted_paths[0]
        if len(sorted_paths) > 1:
            duplicates[key] = sorted_paths
    return index, duplicates


def normalize_key(value: str) -> str:
    return value.strip().lower()


def write_csv(path: Path, rows: list[dict[str, str]], extra_fields: list[str]) -> None:
    if rows:
        fields = list(rows[0].keys())
    else:
        fields = extra_fields
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_duplicate_report(path: Path, duplicates: dict[str, list[Path]]) -> None:
    rows = [
        {"image_key": key, "paths": ";".join(str(path) for path in paths)}
        for key, paths in sorted(duplicates.items())
    ]
    write_csv(path, rows, extra_fields=["image_key", "paths"])


def write_summary(
    path: Path,
    input_rows: list[dict[str, str]],
    matched_rows: list[dict[str, str]],
    missing_rows: list[dict[str, str]],
    duplicates: dict[str, list[Path]],
    dry_run: bool,
) -> None:
    lines = [
        "# Image Matching Summary",
        "",
        f"Dry run: `{dry_run}`",
        f"Rows processed: {len(input_rows)}",
        f"Rows matched: {len(matched_rows) - len(missing_rows)}",
        f"Missing images: {len(missing_rows)}",
        f"Duplicate image keys: {len(duplicates)}",
        "",
        "No real customer, product, order, or private business data is included in this demo.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
