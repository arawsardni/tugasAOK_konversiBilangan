#Gaung Taqwa Indraswara (235150207111043)
def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def decimal_to_hexadecimal(n):
    return hex(n).replace("0x", "")

def binary_to_decimal(binary):
    return int(binary, 2)

def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    return decimal_to_hexadecimal(decimal)

def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

def hexadecimal_to_binary(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    return decimal_to_binary(decimal)

while True:
    try:
        print("Pilih menu konversi:")
        print("1. Bilangan Desimal ke Bilangan Hexadesimal")
        print("2. Bilangan Desimal ke Bilangan Biner")
        print("3. Bilangan Hexadesimal ke Bilangan Desimal")
        print("4. Bilangan Hexadesimal ke Bilangan Biner")
        print("5. Bilangan Biner ke Bilangan Desimal")
        print("6. Bilangan Biner ke Bilangan Hexadesimal")
        print("7. Keluar")

        choice = int(input("Masukkan pilihan: "))

        if choice == 1:
            num = int(input("Masukkan bilangan desimal yang ingin dikonversi: "))
            print(f"{num} dalam bentuk Bilangan Desimal = {hex(num).replace('0x', '')} dalam bentuk Bilangan Hexadesimal")
        elif choice == 2:
            num = int(input("Masukkan bilangan desimal yang ingin dikonversi: "))
            print(f"{num} dalam bentuk Bilangan Desimal = {bin(num).replace('0b', '')} dalam bentuk Bilangan Biner")
        elif choice == 3:
            hex_num = input("Masukkan bilangan hexadesimal yang ingin dikonversi: ")
            print(f"{hex_num} dalam bentuk Bilangan Hexadesimal = {hexadecimal_to_decimal(hex_num)} dalam bentuk Bilangan Desimal")
        elif choice == 4:
            hex_num = input("Masukkan bilangan hexadesimal yang ingin dikonversi: ")
            print(f"{hex_num} dalam bentuk Bilangan Hexadesimal = {hexadecimal_to_binary(hex_num)} dalam bentuk Bilangan Biner")
        elif choice == 5:
            bin_num = input("Masukkan bilangan biner yang ingin dikonversi: ")
            print(f"{bin_num} dalam bentuk Bilangan Biner = {binary_to_decimal(bin_num)} dalam bentuk Bilangan Desimal")
        elif choice == 6:
            bin_num = input("Masukkan bilangan biner yang ingin dikonversi: ")
            print(f"{bin_num} dalam bentuk Bilangan Biner = {binary_to_hexadecimal(bin_num)} dalam bentuk Bilangan Hexadesimal")
        elif choice == 7:
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
    except ValueError:
        print("Masukkan tidak valid. Silakan coba lagi.")