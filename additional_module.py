from pathlib import Path


def count_error_lines(log_path: str) -> int:
    path = Path(log_path)
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    count = 0
    for line in lines:
        if "ERROR" in line:
            count += 1
    return count
