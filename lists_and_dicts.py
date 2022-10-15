from contextlib import suppress


def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {"firstname": "Diego", "lastname": "Muñoz"}

    super_list = [
        {"firstname": "Diego", "lastname": "Muñoz"},
        {"firstname": "Alberto", "lastname": "García"},
        {"firstname": "Rubén", "lastname": "Jesús"},
        {"firstname": "Ana", "lastname": "Mercado"},
        {"firstname": "Yadira", "lastname": "Hernández"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums" : [-1, -2, 0 ,1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for value in super_list:
        print(value)

if __name__ == '__main__':
    run()