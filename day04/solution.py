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
    
def check_accessible(grid):
    H= len(grid)
    W= len(grid[0])
    accessible_list = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            rolls = 0
            if grid[row][col] != '@':
                continue
            for dr, dc in [(-1,-1), (-1,0), (-1,1),
                    (0,-1),         (0,1),
                    (1,-1),  (1,0), (1,1)]:
                nr, nc = row + dr, col + dc # neighbour row/col
                if 0 <= nr < H and 0 <= nc < W:
                    ch = grid[nr][nc]
                    if ch == '@':
                        rolls += 1
            if rolls < 4:
                accessible_list.append( (row, col) )
                #accessible += 1   

    return accessible_list


@timer
def part1(data: str) -> int:
    accessible = 0
    grid = data.splitlines()
    accessible_list = check_accessible(grid)   
    #print("Accessible positions:", accessible_list)

    #time.sleep(3)
    return len(accessible_list)


def remove_from_grid(grid, positions):
    grid_copy = grid.copy()
    for row, col in positions:
        line = list(grid_copy[row])
        line[col] = '.'
        grid_copy[row] = ''.join(line)
    return grid_copy

def show(grid):
    os.system("cls" if os.name == "nt" else "clear")
    for row in grid:
        print("".join(row))

@timer
def part2(data: str) -> int:
    accessible = 0
    grid = data.splitlines()
    #show(grid)
    #time.sleep(1)

    while True:  
        accessible_list = check_accessible(grid)   
        grid = remove_from_grid(grid, accessible_list)

        #show(grid)
        #time.sleep(1)

        if len(accessible_list) == 0:
            break
        else:
            accessible += len(accessible_list)

    #time.sleep(3)
    return accessible



if __name__ == "__main__":
    data = read_input(4)
    #data = read_test_input(4)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data)) 