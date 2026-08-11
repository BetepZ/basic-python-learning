import bisect

li = [20, 30, 45, 60, 70, 80, 110]
low = 0
high = len(li) - 1

while True:

    print("bisect binary Searching")

    search_number = int(input("Masukkan angka yang ingin dicari : "))

    try:
        result = bisect.bisect_left(li, search_number)

    except ValueError:
        print("masukkin yang bener jir")
        continue

    try:
        if li[int(result)] != search_number:
            print("Angka nya tidak ada di index")
            continue

        elif li[int(result)] == search_number:
            print(f"Angka yang anda cari ada di index {result}")

        else:
            print("Angka nya tidak ada di index")

    except IndexError:
        print(f"Angka terlalu besar maksimal ada di {li[-1]}")
