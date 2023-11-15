list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [1, 2, 3]
list_3 = [1, 2, 3, 4, 5]
list_4 = [1]
list_5 = []
midl = len(list_1) // 2
part_1 = list_1[:midl]
part_2 = list_1[midl:]
print(part_1, part_2)
midl_1 = len(list_2) // 2
part_3 = list_2[:midl_1 + 1]
part_4 = list_2[midl_1 + 1:]
print(part_3, part_4)
midl_2 = len(list_3) // 2
part_5 = list_3[:midl_2 + 1]
part_6 = list_3[midl_2 + 1:]
print(part_5, part_6)
midl_3 = len(list_4) // 2
part_7 = list_4[:midl_3 + 1]
part_8 = list_4[midl_3 + 1:]
print(part_7, part_8)
midl_4 = len(list_5) // 2
part_9 = list_5[:midl_4 + 1]
part_10 = list_5[midl_4 + 1:]
print(part_9, part_10)
