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
    
@timer
def part1(data: str) -> int:
    # Implement Part 1 logic here
    pos = 50
    cnt = 0
    print(data)
    lines = data.splitlines()
    for line in lines:
        shift = int(line[1:])        
        if line[0] == "L":
            pos = (pos - shift)%100
        else:
            pos = (pos + shift)%100
        print(line[0], shift, pos)
        if pos == 0:
            cnt += 1
    return cnt

@timer
def part2(data: str) -> int:
    # Implement Part 2 logic here
    pos = 50
    cnt = 0    
    #print(data)
    print(round(abs((50 - 1000)//100)))

    lines = data.splitlines()
    for line in lines:
        shift = int(line[1:])    
        cur_cnt = cnt    
        cur_pos = pos
        cnt += shift //100
        offset = shift % 100
        if offset != 0:
            if line[0] == "L":
                offset = -offset
            pos = cur_pos + offset
            if cur_pos != 0 and (pos <= 0 or pos >= 100):
                cnt += 1
            pos = pos % 100

        if cnt != cur_cnt:# and shift > 99 and line[0] == "L":
            print(cur_pos, line[0], shift, pos, cur_cnt, cnt)
            #time.sleep(5)
    return cnt



if __name__ == "__main__":
    data = read_input(1)
    #data = read_test_input(1)
    #print("Part 1:", part1(data))
    print("Part 2:", part2(data)) # 2797 too low
