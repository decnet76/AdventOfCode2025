import time
import sys
from pathlib import Path

#from utils.helpers import read_input, timer, read_test_input
def read_input(day: int) -> str:
    """Read input file for a given day."""
    file_path = Path(__file__).parent.parent / f"day{day:02d}" / "input.txt"
    with open(file_path) as f:
        return f.read().strip()
    
def read_test_input(day: int) -> str:
    """Read input file for a given day."""
    file_path = Path(__file__).parent.parent / f"day{day:02d}" / "test.txt"
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

######################################################
    
@timer
def part1(data: str) -> int:
    # Start trying with Brute Force
    sum_invalid_ids = 0
    #print(data)
    lines = data.split(",")
    for line in lines:
        #print(line)
        start, end = line.split("-")
        #print(start, end)
        for i in range(int(start), int(end)+1):
            id = str(i)
            #print(id, len(id)/2)
            if id[0:int(len(id)/2)] == id[int(len(id)/2):]:
                #print(id)
                sum_invalid_ids += i
    return sum_invalid_ids

@timer
def part2(data: str) -> int:
    # Start trying with Brute Force
    sum_invalid_ids = 0
    #print(data)
    lines = data.split(",")
    for line in lines:
        #print(line)
        start, end = line.split("-")
        #print(start, end)
        for i in range(int(start), int(end)+1):
            id = str(i)
            l = len(id)
            # strings with odd length can still have a pattern i.e. 123123123 length 9, divisors 1, 3, check for triplets
            # Find divisors of l (excluding l)
            divisors = [d for d in range(1, l) if l % d == 0]
            
            # Check for repeated pattern
            if any(id == id[:d] * (l // d) for d in divisors):
                sum_invalid_ids += i

    return sum_invalid_ids



if __name__ == "__main__":
    data = read_input(2)
    #data = read_test_input(2)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data)) 