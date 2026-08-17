turn = 0


def interpolation_searching(target: int, list_name: list[int]) -> int:

    global turn

    low = 0

    high = len(list_name) - 1

    while low <= high and target >= list_name[low] and target <= list_name[high]:

        pos = low + \
            ((target - list_name[low]) * (high - low) //
             (list_name[high] - list_name[low]))

        if target == list_name[pos]:
            turn += 1
            return pos

        elif target > list_name[pos]:
            turn += 1
            low = pos + 1

        elif target < list_name[pos]:
            turn += 1
            high = pos - 1

    return -1


li = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

while True:

    print("Interpolation Searching")

    search_number = input("Masukkan angka yang ingin dicari : ")

    try:
        result = interpolation_searching(int(search_number), li)

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
