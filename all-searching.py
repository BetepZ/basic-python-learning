
def linear_searching(target: int, lis: list, n: int):

    for i in range(n):
        if lis[i] == target:
            return i

    return -1


def binary_searching(target: int, lis: list, low: int = 0, high: int = 0, n: int = 0):

    middle = (low + high) // 2

    if lis[middle] == target:
        return middle

    elif lis[middle] < target:
        low = middle + 1
        return binary_searching(target, lis, low, high, n)

    elif target < lis[middle]:
        high = middle - 1
        return binary_searching(target, lis, low, high, n)

    else:
        return

    return -1


def jump_searching():
    pass


def exponential_searching():
    pass


def interpolation_searching():
    pass


while True:

    searching = 0

    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
          12, 13, 14, 15, 16, 17, 18, 19, 20]

    print("All Searching Logika")

    search_number = int(input("Masukkan angka yang ingin dicari : "))

    print("1. Linear Searching \n 2.Binary Searching \n 3. Jump Searching 4. Eksponential Searching \n 5. Interpolation Search. ")

    try:
        pass

    except ValueError:
        print("Masukkin yang bener dong nilai nya:")

    print("")
