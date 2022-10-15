#Crear lista de los primeros 100 números al cuadrado y que no sean divisibles entre 3

def run():
    # mi_lista = []
    # for i in range(0, 101):
    #    if i % 3 != 0:
    #        mi_lista.append(i ** 2)

    squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    print(squares)

# list comprehensions de numeros que son divisibles por 4, 6 y 9 hasta 5 dígitos
    squares2 = [i for i in range(1,100001) if i % 36 == 0]

    print(squares2)


if __name__ == '__main__':
    run()