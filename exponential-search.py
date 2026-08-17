turn = 0


def exponential_searching(target: int, list_name: list[int], n):

    global turn

    if target < list_name[0] or target > list_name[n - 1]:
        return -1

    if target == list_name[0]:

        return 0

    i = 1
    while (i < n and list_name[i] <= target):
        turn += 1
        i *= 2

    low = i // 2
    high = min(i, n - 2)
    return binary_searching(target, list_name, low, high)


def binary_searching(target: int, list_name: list[int], low: int = 0, high: int = 0) -> int:

    global turn
    middle = (low + high) / 2

    if low > high:
        return -1

    if target == list_name[int(middle)]:
        turn += 1
        return int(middle)
    # target ada di kanan, potong bagian bawah
    elif target > list_name[int(middle)]:
        low = int(middle) + 1
        turn += 1
        return binary_searching(target, list_name, low, high)
    # target ada di kiri, potong bagian atas
    elif target < list_name[int(middle)]:
        high = int(middle) - 1
        turn += 1
        return binary_searching(target, list_name, low, high)

    return -1


li = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n = len(li)

while True:

    print("Exponential Search")

    search_number = input("Masukkan angka yang ingin dicari : ")

    try:
        result = exponential_searching(int(search_number), list_name=li, n=n)

    except ValueError:
        print("masukkin yang bener jir")
        continue

    if int(result) != -1:
        print(f"Angka yang anda cari ada di index {result}")
        print(f"Dijalankan selama {turn} kali")
        turn = 0

    else:
        turn = 0
        print("Angka nya tidak ada di index")
