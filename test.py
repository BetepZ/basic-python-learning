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

def calculate(li, ls, i, u):

    while ls[i] == li[i]:
        i += 1
        if i == n:
            return -1

    while ls[u] == li[u]:
        u += 1
        if u == n:
            return 1


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = len(li)
i = 0
u = 0

aim = calculate(ls, li, i, u)

print(aim)
