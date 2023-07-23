import os
import json, csv, pickle

def get_directory_size(directory):
    total_size = 0
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def traverse_and_save(directory):
    results = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        item_type = "file" if os.path.isfile(item_path) else "directory"

        if item_type == "file":
            item_size = os.path.getsize(item_path)
        else:
            item_size = get_directory_size(item_path)

        item_info = {
            "name": item,
            "type": item_type,
            "size": item_size,
            "parent_directory": directory
        }
        results.append(item_info)

        if item_type == "directory":
            results.extend(traverse_and_save(item_path))

    return results

def save_to_json(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

def save_to_csv(data, file_path):
    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def save_to_pickle(data, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(data, file)

# Пример использования
directory_to_traverse = "E:\Study\CoDeSys SP RTE"
result_data = traverse_and_save(directory_to_traverse)

# Сохранение результатов в файлы
save_to_json(result_data, "result.json")
save_to_csv(result_data, "result.csv")
save_to_pickle(result_data, "result.pkl")
