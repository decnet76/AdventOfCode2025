from utils.helpers import read_input, timer

@timer
def part1(data: str) -> int:
    # Implement Part 1 logic here
    return sum(map(int, data.split()))

@timer
def part2(data: str) -> int:
    # Implement Part 2 logic here
    return sum(map(int, data.split())) * 2

if __name__ == "__main__":
    data = read_input(1)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
