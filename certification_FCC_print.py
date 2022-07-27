def arithmetic_arranger(lista,*args):
    args=list(args)
    true="".join(map(str, args))

    lista_in_string=" ".join(lista)
    the_list=lista_in_string.split()

    new_list=[]
    first_number=[]
    second_number=[]
    list_operations=[]
    results=[]

    for i in the_list: 
        if i=="+" or i=="-":
            list_operations.append(i)
            continue
        new_list.append(i)

    if len(new_list)>10:
        print("Error: Too many problems.")

    else:
        counter=0
        for numbers in new_list:
            numbers=int(numbers)
            counter+=1
            if counter%2!=0:
                first_number.append(numbers)
            else:
                second_number.append(numbers)
            
        for firstnumbers in first_number:
            print(f'{" "}{firstnumbers:4}', end="\t")
        print("")

        for secondnumbers,operations in zip(second_number,list_operations):
            print(f'{operations}{secondnumbers:4}', end="\t")
        print("")

        resultado=0
        for number_up,operations,number_down in zip(first_number,list_operations,second_number):

            if operations=="+":
                resultado=number_up+number_down
                results.append(resultado)

            elif operations=="-":
                resultado=number_up-number_down
                results.append(resultado)

        for total_operation in results:
            if true == "True":
                print(f'{" "}{total_operation:4}',end="\t")
        print("")

        print("\n","\n","\n")
arithmetic_arranger(["32 + 698","3801 - 2","45 + 43","123 + 49","1 + 2"],True)