import math

turn = 0


def jump_searching(target: int, list_name: list[int]) -> int:

    global turn

    n = len(list_name)
    jump = int(math.sqrt(n))
    step = jump
    previous = 0

    while list_name[min(step, n) - 1] < target:
        turn += 1
        previous = step
        step += jump
        if (previous >= n):
            return -1

    while list_name[previous] < target:
        turn += 1
        previous += 1
        if previous == min(step, n):
            return -1

    if list_name[previous] == target:
        turn += 1
        return previous
    return -1


li = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

while True:

    print("Jump Searching")

    search_number = input("Masukkan angka yang ingin dicari : ")

    try:
        result = jump_searching(int(search_number), li)

    except ValueError:
        print("masukkin yang bener jir")
        continue

    if int(result) != -1:
        print(f"Angka yang anda cari ada di index {result}")
        print(f"Dijalankan selama {turn} kali")

    else:
        print(f"Dijalankan selama {turn} kali")
        print("Angka nya tidak ada di index")
