def arithmetic_arranger(lista,true=False):

    #1 situation that will return an error:
    if len(lista)>5:
        return "Error: Too many problems."

    problem_1,problem_2,problem_3,problem_4,problem_5=lista[0],lista[1],lista[2],lista[3],lista[4]
    problem_1=problem_1.split(" ")
    problem_2=problem_2.split(" ")
    problem_3=problem_3.split(" ")
    problem_4=problem_4.split(" ")
    problem_5=problem_5.split(" ")

    #2 situation that will return an error:
    if (problem_1[1]=="+" or problem_1[1]=="-") and (problem_2[1]=="+" or problem_2[1]=="-") and \
    (problem_3[1]=="+" or problem_3[1]=="-") and (problem_4[1]=="+" or problem_4[1]=="-") and \
    (problem_5[1]=="+" or problem_5[1]=="-"):
        pass
    else:
        return "Error: Operator must be '+' or '-'."

    #3 situation that will return an error:
    from_lista_to_str=" ".join(lista)
    for digits in from_lista_to_str:
        if digits=="+" or digits=="-" or digits==" ":
            continue
        elif digits.isdigit()==False:
            return "Error: Numbers must only contain digits."

    #4 situation that will return an error:
    from_lista_str_to_list=from_lista_to_str.split()
    for width_of_digits in from_lista_str_to_list:

        if width_of_digits=="+" or width_of_digits=="-":
            continue
        elif len(width_of_digits)>4:
            return "Error: Numbers cannot be more than four digits."

    #5 math_operations:
    #up= upper number, do= down number, op= operator simbol, l= line.
    up1,do1,op1=from_lista_str_to_list[0],from_lista_str_to_list[2],from_lista_str_to_list[1]
    up2,do2,op2=from_lista_str_to_list[3],from_lista_str_to_list[5],from_lista_str_to_list[4]
    up3,do3,op3=from_lista_str_to_list[6],from_lista_str_to_list[8],from_lista_str_to_list[7]
    up4,do4,op4=from_lista_str_to_list[9],from_lista_str_to_list[11],from_lista_str_to_list[10]
    up5,do5,op5=from_lista_str_to_list[12],from_lista_str_to_list[14],from_lista_str_to_list[13]

    l1=("-"*(len(up1)+2) if int(up1)>int(do1) else "-"*(len(do1)+2))
    l2=("-"*(len(up2)+2) if int(up2)>int(do2) else "-"*(len(do2)+2))
    l3=("-"*(len(up3)+2) if int(up3)>int(do3) else "-"*(len(do3)+2))
    l4=("-"*(len(up4)+2) if int(up4)>int(do4) else "-"*(len(do4)+2))
    l5=("-"*(len(up5)+2) if int(up5)>int(do5) else "-"*(len(do5)+2))

    s1=(int(up1)+int(do1) if op1=="+" else int(up1)-int(do1))
    su1=(str(s1) if true==True else "")
    s2=(int(up2)+int(do2) if op2=="+" else int(up2)-int(do2))
    su2=(str(s2) if true==True else "")
    s3=(int(up3)+int(do3) if op3=="+" else int(up3)-int(do3))
    su3=(str(s3) if true==True else "")
    s4=(int(up4)+int(do4) if op4=="+" else int(up4)-int(do4))
    su4=(str(s4) if true==True else "")
    s5=(int(up5)+int(do5) if op5=="+" else int(up5)-int(do5))
    su5=(str(s5) if true==True else "")

    #op_pos=operant position, to ten=the difference to reach the 10 position
    spaces=4
    po_ini1=len(l1)
    op_pos1=(po_ini1+1)-len(l1)
    to_ten1=po_ini1-op_pos1

    po_ini2=len(l2)+spaces
    op_pos2=(po_ini2+1)-len(l2)
    to_ten2=po_ini2-op_pos2

    po_ini3=len(l3)+spaces
    op_pos3=(po_ini3+1)-len(l3)
    to_ten3=po_ini3-op_pos3

    po_ini4=len(l4)+spaces
    op_pos4=(po_ini4+1)-len(l4)
    to_ten4=po_ini4-op_pos4

    po_ini5=len(l5)+spaces
    op_pos5=(po_ini5+1)-len(l5)
    to_ten5=po_ini5-op_pos5

    struture1="{}{}{}{}{}   \n{}{}{}{}{}{}{}{}{}{}  \n{}{}{}{}{}   \n{}{}{}{}{}".format(
        up1.rjust(po_ini1),up2.rjust(po_ini2),up3.rjust(po_ini3),up4.rjust(po_ini4),up5.rjust(po_ini5),

        op1.rjust(op_pos1),do1.rjust(to_ten1),op2.rjust(op_pos2),do2.rjust(to_ten2),op3.rjust(op_pos3),
        do3.rjust(to_ten3),op4.rjust(op_pos4),do4.rjust(to_ten4),op5.rjust(op_pos5),do5.rjust(to_ten5),

        l1.rjust(po_ini1),l2.rjust(po_ini2),l3.rjust(po_ini3),l4.rjust(po_ini4),l5.rjust(po_ini5),

        su1.rjust(po_ini1),su2.rjust(po_ini2),su3.rjust(po_ini3),su4.rjust(po_ini4),su5.rjust(po_ini5))

    return struture1
print(arithmetic_arranger(["10 + 1000","40 - 2000","4 + 43","1 + 49","1 + 1"]))