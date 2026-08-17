turn = 0


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
low = 0
high = len(li) - 1


while True:

    print("Binary Searching")

    search_number = input("Masukkan angka yang ingin dicari : ")

    try:
        result = binary_searching(int(search_number), li, low, high)

    except ValueError:
        print("masukkin yang bener jir")
        continue

    if int(result) != -1:
        print(f"Angka yang anda cari ada di index {result}")
        print(f"Dijalankan selama {turn} kali")

    else:
        print("Angka nya tidak ada di index")
