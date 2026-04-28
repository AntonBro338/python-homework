import time
import bisect

def read_file (filename: str) -> dict[str, bool]:
    """Читает слова из файла и сохраняет их в словаре как ключи."""
    word = {}
    with open("путь к файлу") as file:
        for line in file:
            line = line.strip()
            word[line] = 1
    return word

start = time.time()
result = read_file
end = time.time()

cpu_time = end - start


print(f"Время: {cpu_time:.6f} секунд")

def binary_search(sorted_list: list[str], target: str):
    """
    >>> binary_search(['1', '2', '3'], '2')
    True
    """
    index = bisect.bisect_left(sorted_list, target)
    return index < len(sorted_list) and sorted_list[index] == target

start = time.time()
result2 = binary_search
end = time.time()

cpu_time2 = end - start

print(f"Время: {cpu_time2:.6f} секунд")
