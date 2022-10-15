def run():
    # mi_dict = {}
    # for i in range(1,101):
    #    if i % 3 != 0:
    #        mi_dict[i] = i**3

    mi_dict = {i: i**3 for i in range(1,101) if i % 3 != 0}

    print(mi_dict)


if __name__ == '__main__':
    run()