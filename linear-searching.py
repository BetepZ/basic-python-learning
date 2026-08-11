
li = [20, 30, 45, 60, 40, 50, 70]


def linear_searching(target: int, list_name: list[int]) -> int:
    lenght = len(list_name)

    for i in range(lenght):
        if list_name[i] == target:
            return int(i)

    return -1


while True:
    search_number = input("Masukkan angka yang ingin dicari : ")

    try:
        result = linear_searching(int(search_number), li)

    except ValueError:
        print("masukkin yang bener jir")
        continue

    if int(result) != -1:

        print(f"Angka yang anda cari ada di index {result}")

    else:
        print("Angka nya tidak ada di index")
