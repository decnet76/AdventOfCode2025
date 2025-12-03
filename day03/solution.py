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
    # This looks easy: find the max in the row, then the second max after that (cannot rearrange digits)
    # if secondmax < max, need to swap them
    sum_joltage = 0
    banks = data.splitlines()
    for bank in banks:
        digits = [int(d) for d in bank]
        max_digit = max(digits)      
        max_pos = digits.index(max_digit)

        if max_pos == 0:
            second_max = max(digits[1:])
            second_max_pos = digits.index(second_max)
        elif max_pos == len(digits)-1:
            second_max = max(digits[:-1])
            second_max_pos = digits.index(second_max)
        else:            
            second_max = max(digits[max_pos+1:])
            second_max_pos = max_pos + 1 + digits[max_pos+1:].index(second_max)
        
        joltage = 10*second_max + max_digit
        if max_pos < second_max_pos:
            sum_joltage += 10*max_digit + second_max
            joltage = 10*max_digit + second_max
        else:
            sum_joltage += 10*second_max + max_digit

        print(bank, digits, max_digit, second_max, max_pos, second_max_pos, joltage)

        #time.sleep(3)

    return sum_joltage


def max_digits_in_order(digits, k):
    n = len(digits)
    start = 0
    result = []

    for remaining in range(k, 0, -1):
        # We must leave (remaining-1) digits after the chosen one.
        end = n - remaining + 1          
        window = digits[start:end]       

        best = max(window)               
        idx_in_window = window.index(best)
        result.append(best)

        # Move start so next choice comes after this digit
        start += idx_in_window + 1

    return result


def digits_to_int(digs):
    val = 0
    for d in digs:
        val = val * 10 + d
    return val


@timer
def part2(data: str) -> int:
    sum_joltage = 0
    banks = data.splitlines()
    for bank in banks:
        digits = [int(d) for d in bank]

        max_twelve = max_digits_in_order(digits, 12)    

        joltage = digits_to_int(max_twelve)
        #print(bank, digits, max_twelve, joltage)
        #time.sleep(5)

        sum_joltage += joltage

    return sum_joltage



if __name__ == "__main__":
    data = read_input(3)
    #data = read_test_input(3)
    #print("Part 1:", part1(data))
    print("Part 2:", part2(data)) 