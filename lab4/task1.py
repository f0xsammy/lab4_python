import json

def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)
    total_sum = sum(entry["score"] * entry["weight"] for entry in data)
    return round(total_sum, 3)


print(task())