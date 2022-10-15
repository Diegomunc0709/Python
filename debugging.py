def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]

    return divisors


def run():
    try:
        num = int(input("Ingresa un número: "))
        print(divisors(num))
        print("Terminó el programa.")
    except ValueError:
        print("Debes ingresar un número")

if __name__ == '__main__':
    run()