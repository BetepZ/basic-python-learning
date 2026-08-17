turn = 0


def linear_searching(target: int, list_name: list[int]) -> int:
    lenght = len(list_name)

    global turn

    for index in range(lenght):
        if list_name[index] == target:
            turn = turn + 1
            return index

    return -1


li = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

while True:

    print("Linear Searching")

    search_number = input("Masukkan angka yang ingin dicari : ")

    try:
        result = linear_searching(int(search_number), li)

    except ValueError:
        print("masukkin yang bener jir")
        continue

    if result == -1:
        print("angka anda tidak ketemu")
        turn = 0

    else:
        print(f"angka anda ketemu di index ke {result}")
        turn = 0
