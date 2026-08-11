# # listV = [1, 2, 3]
# # print(listV)

# # listContrustor = list((1, 2, 3, 'apple', 4.5))
# # print(listContrustor)

# # listRepeatedElement = [2] * 5
# # print(listRepeatedElement)

# # representingList = [1, 2, 2, "Python"]
# # print(representingList[-1])   # index-based
# # print(representingList)

# ListAppend = [1, 2]
# # # ListAppend.append(14)
# # # print(ListAppend)

# # # listInsert = [3, 5]
# # # listInsert.insert(1, 4)
# # print(listInsert)

# ListAppend.extend([3, 4, 5])
# # print(ListAppend)

# # ListAppend.remove(2)

# # try:
# #     ListAppend.remove(2)
# # except:
# #     print("there is no 2")

# # del ListAppend[0]

# # ListAppend.cleaaar()

# for lis in ListAppend:
#     print(f"index ke {lis} adalah {ListAppend[lis-1]}")

# # print(ListAppend)a

# nested_list = [[1, 2, 5], [3, 4, 6]]
# print(nested_list[0][2])

# def addToList(a):
#     a += [10]

# contoh_list.append(10)

# print(contoh_list)
# https://wiki.python.org/moin/TimeComplexityaa

import bisect

li = [1, 3, 5, 7, 9, 12, 12]

bisect.insort(li, 2, 0, 2)

print(li)
