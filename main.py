import os
import sys
from pathlib import Path
from collections import defaultdict

FILE_GROUPS = {
    "Videos":      [".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv", ".webm", ".m4v"],
    "Images":      [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".heic", ".svg"],
    "ZIP Files":   [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
    "Documents":   [".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".txt", ".csv"],
    "Audio":       [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "Code":        [".py", ".js", ".ts", ".html", ".css", ".java", ".cpp", ".c", ".go", ".rs"],
    "Executables": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".sh", ".bat"],
}

def get_group(ext: str) -> str:
    ext = ext.lower()
    for group, exts in FILE_GROUPS.items():
        if ext in exts:
            return group
    return "Other"

def format_size(size_bytes: int) -> str:
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} PB"

def scan_folder(root: Path) -> dict:
    sizes = defaultdict(int)
    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            fpath = Path(dirpath) / fname
            try:
                size = fpath.stat().st_size
                group = get_group(fpath.suffix)
                sizes[group] += size
            except (PermissionError, FileNotFoundError):
                pass
    return sizes

def draw_bar(value: int, max_value: int, width: int = 32) -> str:
    if max_value == 0:
        return ""
    filled = int((value / max_value) * width)
    return "#" * filled + "-" * (width - filled)

def main():
    if len(sys.argv) < 2:
        target = Path(".")
    else:
        target = Path(sys.argv[1]).expanduser()

    if not target.exists():
        print(f"Error: Path '{target}' does not exist.")
        sys.exit(1)
    if not target.is_dir():
        print(f"Error: '{target}' is not a directory.")
        sys.exit(1)

    print(f"\nfolderheat  {target.resolve()}\n")
    print("Scanning...", end="", flush=True)
    sizes = scan_folder(target)
    print(" done.\n")

    if not sizes:
        print("No files found.")
        return

    sorted_items = sorted(sizes.items(), key=lambda x: x[1], reverse=True)
    sorted_items = [(k, v) for k, v in sorted_items if v > 0]

    max_size = sorted_items[0][1] if sorted_items else 1
    max_label = max(len(k) for k, _ in sorted_items)

    print(f"  {'Category':<{max_label}}   {'Size':>10}   Distribution")
    print(f"  {'-' * max_label}   {'-' * 10}   {'-' * 32}")

    for group, size in sorted_items:
        bar = draw_bar(size, max_size)
        print(f"  {group:<{max_label}}   {format_size(size):>10}   {bar}")

    total = sum(v for _, v in sorted_items)
    print(f"\n  {'-' * (max_label + 48)}")
    print(f"  {'TOTAL':<{max_label}}   {format_size(total):>10}\n")

if __name__ == "__main__":
    main()
