def divisors(num):
    try:
        if num <= 0:
            raise ValueError('Debes ingresar un nÃºmero positivo')

        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)

        return divisors
    except ValueError as ve:
        print('Error:', ve)


def run():
    try: 
        num = int(input('Ingresa un nÃºmero: '))
        print(divisors(num))
        print("TerminÃ³ mi programa")
    except ValueError: 
        print("Debes ingresar un nÃºmero")


if __name__ == '__main__':
    run()