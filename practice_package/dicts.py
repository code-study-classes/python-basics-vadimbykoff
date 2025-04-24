from typing import Callable, Dict


def count_char_occurrences(text: str) -> Dict[str, int]:
    result = {}
    for char in text.lower():
        if char.isalpha():  # учитываем только буквы
            result[char] = result.get(char, 0) + 1
    return result


def merge_dicts(dict1: Dict, dict2: Dict, conflict_resolver: Callable[[str, any, any], any]) -> Dict:
    merged_dict = dict1.copy()  # копируем первый словарь
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] = conflict_resolver(key, merged_dict[key], value)
        else:
            merged_dict[key] = value
    return merged_dict


def invert_dictionary(original_dict: Dict) -> Dict:
    inverted_dict = {}
    for key, value in original_dict.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]
    return inverted_dict


def dict_to_table(data_dict: Dict, columns: list) -> str:
    headers = [col.upper() for col in columns]
    
    table_rows = []
    for row_id, row_data in data_dict.items():
        row = []
        for column in columns:
            row.append(str(row_data.get(column, 'N/A')))
        table_rows.append(row)

    column_widths = [
        max(len(str(item)) for item in col) for col in zip(*table_rows, headers)
    ]
    
    formatted_table = []
    formatted_table.append(
        '| ' + ' | '.join([headers[i].ljust(column_widths[i]) for i in range(len(headers))]) + ' |'
    )
    formatted_table.append(
        '|' + '|'.join(['-' * column_widths[i] for i in range(len(headers))]) + '|'
    )
    
    for row in table_rows:
        formatted_table.append(
            '| ' + ' | '.join([row[i].ljust(column_widths[i]) for i in range(len(row))]) + ' |'
        )

    return '\n'.join(formatted_table)


def deep_update(base_dict: Dict, update_dict: Dict) -> Dict:
    result = base_dict.copy()  # копируем исходный словарь
    for key, value in update_dict.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = deep_update(result[key], value)  # рекурсивно обновляем
        else:
            result[key] = value
    return result