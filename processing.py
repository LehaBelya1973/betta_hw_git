# # вход функции
a = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def state_into(list_data: list[dict], state: str='EXECUTED'):
    result_list = []
    for operation in list_data:
        if operation.get('state') == state:
            result_list.append(operation)
    return result_list


def sort_date(list_data: list[dict], key: str=''):
    sort_list = []
