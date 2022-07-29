def arithmetic_arranger(lista,true=False):
    
    #1 Situations that will return an error
    if len(lista)>5:
        return "Error: Too many problems."

    str_lista=" ".join(lista)
    new_lista=str_lista.split()

    operators=[]
    strs=[]
    counter=0
    up_numbers=[]
    down_numbers=[]
    lines=[]
    total_operation=[]

    for operator in new_lista:
        if operator=="+" or operator=="-":
            operators.append(operator)
            continue
        if operator.isdigit()==True:
            counter+=1
            if len(operator)>4:
                #4 Situations that will return an error
                return "Error: Numbers cannot be more than four digits."

            if counter%2!=0:
                up_numbers.append(operator)
            else:
                down_numbers.append(operator)
            continue
        else:
            strs.append(operator)

    #2 Situations that will return an error
    if len(operators)<len(lista):
        return "Error: Operator must be '+' or '-'."

    #3 Situations that will return an error
    if len(strs)>=1:
        return "Error: Numbers must only contain digits."

    #calculating the lines width and the total of the math operations.
    results=0
    width_line=0
    counter_lines=0
    spaces=4
    for up_number,down_number,operation in zip(up_numbers,down_numbers,operators):
        counter_lines+=1
        if len(up_number)>=len(down_number):
            width_line=(len(up_number)+2)*"-"
        if len(down_number)>=len(up_number):
            width_line=(len(down_number)+2)*"-"

        if counter_lines<5:
            #4 spaces for each line.
            width_line=width_line+(spaces*" ")
        lines.append(width_line)

        if operation=="+":
            results=int(up_number)+int(down_number)
        if operation=="-":
            results=int(up_number)-int(down_number)
        total_operation.append(results)

    #finding the right space
    counter=0
    up_numbers_space,up_numbers_sp=0,[]
    down_numbers_space,down_numbers_sp=0,[]
    total_operation_space,total_operation_sp=0,[]
    for upspace,downspace,operatorspace,linespace,totalspace in zip(up_numbers,down_numbers,operators,lines,total_operation):
        counter+=1
        totalspace=str(totalspace)

        #for up_numbers
        if (len(linespace)>len(upspace)):
            up_numbers_space=((len(linespace)-spaces)-len(upspace))*" "
            up_numbers_sp.append(up_numbers_space)
            up_numbers_sp.append(upspace)

        if (len(linespace)>len(upspace)) and counter<5:
            up_numbers_sp.append(spaces*" ")

        if (len(linespace)>len(upspace)) and counter==4:
            up_numbers_sp.append(up_numbers_space)

        #for down_numbers
        if (len(linespace)>len(downspace)):
            down_numbers_space=((((len(linespace)-spaces)-len(downspace))-1)*" ")
            if (len(linespace)>len(downspace)) and counter<5:
                down_numbers_sp.append(operatorspace)

            down_numbers_sp.append(down_numbers_space)
            down_numbers_sp.append(downspace)

        if (len(linespace)>len(downspace)) and counter<5:
            down_numbers_sp.append(spaces*" ")

        if (len(linespace)>len(downspace)) and counter==4:
            down_numbers_sp.append(operatorspace)
            down_numbers_sp.append(down_numbers_space)

        #for total_operation
        if (len(linespace)>len(totalspace)):
            total_operation_space=((len(linespace)-spaces)-len(totalspace))*" "
            total_operation_sp.append(total_operation_space)
            total_operation_sp.append(totalspace)

        if (len(linespace)>len(totalspace)) and counter<5:
            total_operation_sp.append(spaces*" ")

        if (len(linespace)>len(totalspace)) and counter==4:
            total_operation_sp.append(up_numbers_space)

    up_numbers_str="".join(map(str,up_numbers_sp))
    down_numbers_str="".join(map(str,down_numbers_sp))
    lines_str="".join(lines)
    total_operation_str="".join(map(str,total_operation_sp))

    output=(f'{up_numbers_str.rjust(len(lines_str))}\n{down_numbers_str.rjust(len(lines_str))}\n\
{lines_str}\n{total_operation_str.rjust(len(lines_str)) if true==True else ""}')

    return output

print(arithmetic_arranger(["3 + 8","38 - 2","45 + 43","123 + 49","43 + 2"]))