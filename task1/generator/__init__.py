__all__ = (
    'join',
)

def join(strings_file, numbers_file):
    strings_lines = strings_file.readlines()
    numbers_lines = numbers_file.readlines()
    numbers_lines_count = len(numbers_lines)

    for i, line in enumerate(strings_lines):
        line = line.strip()
        number = int(numbers_lines[i].strip()) if i < numbers_lines_count else None
        yield (line, number)
