# Дан словарь с разной степенью вложенности. На нижнем уровне обязательно находится число.
# Нужно написать функцию, которая будет генерировать пары (ключи, соединенные через точку; значение).
#
# Например, из словаря:
# a = {
#     'b' : 4,
#     'c' : {
#         'd': 3,
#         'e': 5,
#     }
# }
#
# Должно получиться:
# [
#     ('b', 4),
#     ('c.d', 3),
#     ('c.e', 5),
# ]

def create_keys(some_dict: dict):

    if len(some_dict) == 0:
        return 'Nothing to iterate'

    stack = [(k, v) for k, v in some_dict.items()]
    pairs = []

    while stack:
        k, v = stack.pop()

        while isinstance(v, dict):
            for sub_k, sub_v in v.items():
                stack.append((f"{k}.{sub_k}", sub_v))
            k, v = stack.pop()

        pairs.append((k, v))

    return pairs[::-1]