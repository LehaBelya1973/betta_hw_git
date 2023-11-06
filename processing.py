def state_into(list_data: list[dict], state: str = "EXECUTED"):
    """Функция принимает на вход список словарей
    и значение для ключа state
    (опциональный параметр со значением по умолчанию
    EXECUTED)
    и возвращает новый список, содержащий только те словари, у которых ключ
    state содержит переданное в функцию значение"""
    result_list = []
    for operation in list_data:
        if operation.get("state") == state:
            result_list.append(operation)
    return result_list


def sort_date(list_data: list[dict], keys: bool = False):
    """Функция принимает на вход список словарей
    и возвращает новый список,
    в котором исходные словари отсортированы по убыванию даты (ключ
    date)."""
    list_data.sort(key=lambda operation: operation["date"], reverse=keys)
    return list_data
