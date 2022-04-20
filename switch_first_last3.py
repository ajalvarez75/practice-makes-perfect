a_list = ["a", "b", "c"]

index1 = a_list.index("a")
index2 = a_list.index("c")
a_list[index1], a_list[index2] = a_list[index2], a_list[index1]

print(a_list)