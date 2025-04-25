import random

def create_ran_list(n):
    random_list = []
    for _ in range(n):
        random_list.append(random.randint(1, 100))
    return random_list

def print_list(lst):
    print("Danh sách:", lst)

def print_reverse(lst):
    reversed = lst[::-1]
    print("Danh sách đảo ngược: ", reversed)

def sorted_and_print(lst):
    sorted_list = sorted(lst)
    print(sorted_list)
    
def find_max_and_last_position(lst):
    max_val = lst[0]
    last_pos = 0

    for i in range(len(lst)):
        if lst[i] >= max_val:
            max_val = lst[i]
            last_pos = i
    
    print(f"Phần tử lớn nhất: {max_val}, Vị trí lớn nhất cuối cùng: {last_pos}")

def count_x_and_positions(lst, x):
    count = 0
    pos = []

    for i in range(len(lst)):
        if lst[i] == x:
            count += 1
            pos.append(i)
    
    print(f"Số lượng phần tử bằng {x} là: {count}")
    print("Vị trí xuất hiện:", pos)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_positions(lst):
    positions = []
    for i in range(len(lst)):
        if is_prime(lst[i]):
            positions.append(i)
    print("Vị trí các phần tử là số nguyên tố:", positions)

def unique_numbers(lst):
    uniques = []

    for val in lst:
        if lst.count(val) == 1:
            uniques.append(val)

    print("Các số duy nhất (không trùng lặp):", uniques)

def frequency_count(lst):
    freq = {}

    for val in lst:
        if val in freq:
            freq[val] += 1
        else:
            freq[val] = 1

    print("Giá trị và số lần xuất hiện:")
    for k in freq:
        print(k, "xuất hiện", freq[k], "lần")

def decreasing_subarrays(lst):
    result = []
    i = 0

    while i < len(lst) - 1:
        sub = [lst[i]]
        while i < len(lst) - 1 and lst[i] > lst[i + 1]:
            sub.append(lst[i + 1])
            i += 1
        if len(sub) > 1:
            result.append(sub)
        i += 1

    print("Các đoạn con giảm liên tiếp:")
    for sub in result:
        print(sub)

def display_menu():
    """Hiển thị menu lựa chọn"""
    print("\n===== MENU =====")
    print("1. In ra danh sách vừa tạo")
    print("2. In đảo ngược danh sách")
    print("3. Sắp xếp danh sách và in ra")
    print("4. Tìm phần tử lớn nhất và vị trí cuối cùng")
    print("5. Đếm số lượng phần tử bằng X và in vị trí")
    print("6. In ra vị trí các phần tử là số nguyên tố")
    print("7. Tìm các số duy nhất (không trùng lặp)")
    print("8. Liệt kê các giá trị kèm số lần xuất hiện")
    print("9. In ra các đoạn con giảm liên tiếp")
    print("0. Thoát chương trình")
    print("================")

def main():
    while True:
        try:
            n = int(input("Nhập số phần tử N (1-100): "))
            if 1 <= n <= 100:
                break
            else:
                print("Vui lòng nhập số trong khoảng từ 1 đến 100.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

    my_list = create_ran_list(n)

    while True:
        choice = input("Nhập lựa chọn của bạn: ")
        
        if choice == '1':
            print_list(my_list)
        elif choice == '2':
            print_reverse(my_list)
        elif choice == '3':
            sorted_and_print(my_list)
        elif choice == '4':
            find_max_and_last_position(my_list)
        elif choice == '5':
            try:
                x = int(input("Nhập giá trị X: "))
                count_x_and_positions(my_list, x)
            except ValueError:
                print("Giá trị X không hợp lệ.")
        elif choice == '6':
            prime_positions(my_list)
        elif choice == '7':
            unique_numbers(my_list)
        elif choice == '8':
            frequency_count(my_list)
        elif choice == '9':
            decreasing_subarrays(my_list)
        elif choice == '0':
            print("Kết thúc chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()