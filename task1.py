import os

def parse_file_path(file_path: str) -> tuple:
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return path, name, extension

file_path = 'c:/Users/Vladislav/Desktop/deep_to_python/test.txt'
result = parse_file_path(file_path)
print(result)
