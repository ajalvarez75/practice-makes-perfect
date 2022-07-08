def combination(num1, num2):
    for i in range(num1):
        for j in range(num2):
            if i<j:
                print(f'{i:02}{j:02}')

combination(100,100)
