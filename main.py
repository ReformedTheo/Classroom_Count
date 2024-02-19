import random

def print_room(tables):
    print("is here!")
    for row in tables:
        print(row)

def count_students(tables):
    print(tables)
    count = 0
    for row in tables:
        for student in row:
            if student == 1:
                count = count + 1
    print(f"there are {count} students in class")

def main():
    room_size = round(int(input("Enter room size: "))/3)
    tables = [[random.randint(0, 1) for _ in range(room_size)] for _ in range(room_size)]
    print("************\n")
    print("****MENU****\n")
    print("************\n")
    print("\n\n\n")
    while True:  
        print("\n\n\n0 - Quit\n")
        print("1 - Print randomized room \n")
        print("2 - Count students \n\n")
        option = int(input("Choose your option: "))
        if option == 0:
            break
        elif option == 1:
            print_room(tables)
        elif option == 2:
            count_students(tables)
        else:
            print("Invalid Option")
            continue

if __name__ == "__main__":
    main()