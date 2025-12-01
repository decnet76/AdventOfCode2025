
import time
from pathlib import Path

def read_input(day: int) -> str:
    """Read input file for a given day."""
    file_path = Path(__file__).parent.parent / f"day{day:02d}" / "input.txt"
    with open(file_path) as f:
        return f.read().strip()

def timer(func):
    """Decorator to measure execution time."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} executed in {time.time() - start:.4f}s")
        return result
    return wrapper
