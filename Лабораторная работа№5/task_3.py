import random


def get_unique_list_numbers() -> list[int]:
    result = []
    while len(result) != 15:
        number = random.randint(-10, 10)
        if number not in result:
            result.append(number)
    return result


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
