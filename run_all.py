import subprocess
import sys
from pathlib import Path


TASK_FILES = (
    "task01_max_consecutive_ones.py",
    "task02_even_digits.py",
    "task03_sorted_squares.py",
    "task04_duplicate_zeros.py",
    "task05_merge_sorted_array.py",
    "task06_remove_duplicates.py",
    "task07_check_if_n_and_double_exist.py",
    "task08_valid_mountain_array.py",
    "task09_replace_with_greatest_right.py",
    "task10_sort_array_by_parity.py",
)


# Запускає кожну задачу окремо й повертає код помилки, якщо є збій.
def main():
    project_dir = Path(__file__).resolve().parent
    failed = False
    for filename in TASK_FILES:
        result = subprocess.run(
            [sys.executable, "-E", "-B", str(project_dir / filename)],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0 and result.stdout.strip() == "OK":
            print(f"{filename}: OK")
        else:
            print(f"{filename}: FAIL")
            for output in (result.stdout, result.stderr):
                if output:
                    print(output.rstrip())
            failed = True
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
