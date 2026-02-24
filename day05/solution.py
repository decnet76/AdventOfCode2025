import time
import sys
import os
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
    ingredients = data.splitlines()
    #print("Ingredients:", ingredients)
    ranges = ingredients[0:ingredients.index('')]
    available = ingredients[ingredients.index('')+1:]

    #print("Ranges:", ranges)
    #print("Available:", available     )
    fresh = []
    #fresh_ranges = []
    for i in range(len(ranges)):
        from_, to = map(int, ranges[i].split('-'))
        fresh.append( (from_, to) )
        
    #     for j in range(from_, to+1):
    #          fresh_ranges.append(j)
    # fresh_ranges = set(fresh_ranges) # remove duplicates for part 2
    # print("Part 2 = ", len(fresh_ranges))

    #print("Fresh:", fresh)
    #time.sleep(3)

    cnt_fresh = 0
    for item in available:
        item_int = int(item)
        for from_, to in fresh:
            if from_ <= item_int <= to:
                cnt_fresh += 1
                break
    return cnt_fresh


# This one does not work, too slow with the input, it won't terminate in reasonable time, it needs to be more clever
@timer
def part2(data: str) -> int:
    ingredients = data.splitlines()
    ranges = ingredients[0:ingredients.index('')]

    fresh_dict = {}
    for i in range(len(ranges)):
        from_, to = map(int, ranges[i].split('-'))
        for j in range(from_, to+1):
            fresh_dict[j] = True
    return len(fresh_dict)


if __name__ == "__main__":
    data = read_input(5)
    #data = read_test_input(5)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data)) 