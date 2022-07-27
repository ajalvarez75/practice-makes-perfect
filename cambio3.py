def cambio(money):

    coins1=[25,10,5,1]
    resultado=0

    for i in coins1:
        M_coins=money//i
        money=money-(i*M_coins)
        resultado+=M_coins
        #print(M_coins if M_coins>=1 else "")
    print(resultado)

cambio(90)
print()

#devolver el minimo cantidad de monedas si 

coins2=[25,10,1]
# bajo el metodo anterior para un cambio de 31 la respuesta seria
# 7 monedas, 1 moneda de 25 y 6 monedas de 1
# lo anterior no seria verdad ya que la cantidad minima seria 3 monedas de 10 y 1 moneda 1

def change(i):
    amount_25=i%25

    if (((amount_25>4 and amount_25<10) or(amount_25>14 and amount_25<20)) and i>29):
        amount_25+=25
        amount_10_count=amount_25//10
        amount_25_count=(i-(amount_10_count*10))//25
        amount_1_count=i-((amount_25_count*25)+(amount_10_count*10))

    else:
        amount_25=i%25
        amount_25_count=i//25
        amount_10=amount_25%10
        amount_10_count=amount_25//10
        amount_1=amount_10%1
        amount_1_count=amount_10//1

    total_coins=amount_25_count+amount_10_count+amount_1_count
    print("Amount to change:",i)
    print("Total coins:",total_coins)
    print("details:", amount_25_count,"of 25",amount_10_count,"of 10,",amount_1_count,"of 1.")

change(50)

