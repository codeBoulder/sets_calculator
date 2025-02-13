import math

# Input the set elments
def data_input():
    while True:
        print('Введіть елементи множини у вигляді (1, 2, 3, ...):')
        input1 = input()
        try:
            set1 = set(input1.split(", "))
            for x in set1:
                if not x.isdigit():
                    raise ValueError
            return set1
        except ValueError:
            print("Помилка! Введіть коректну множину чисел.")

# Binary operations proccessing
def binary_operations(set1, set2):
    set1, set2 = list(set1), list(set2)
    set1.reverse()
    set2.reverse()
    print("Оберіть потрібне бінарне відношення:\n1 -- a > b\n2 -- sin(a) > sin(b)\n3 -- a ** 2 = b\n4 -- a + 1 < b")
    choice_bin = int(input())
    result = []
    for a in set1:
        a = int(a)
        matrix = []
        for b in set2:
            b = int(b)
            if choice_bin == 1:
                matrix.append(1 if a > b else 0)
            elif choice_bin == 2:
                matrix.append(1 if math.sin(a) > math.sin(b) else 0)
            elif choice_bin == 3:
                matrix.append(1 if a ** 2 == b else 0)
            elif choice_bin == 4:
                matrix.append(1 if a + 1 < b else 0)
        result.append(matrix)
    return result

# The main part of program
def main():
    set1 = data_input()
    set2 = data_input()
    while True:
        print('Оберіть потрібну дію із множинами:\n1 - Перетин\n2 - Об\'єднання\n3 - Симетрична різниця\n4 - Різниця\n5 - Бінарні відношення')
        choice = int(input("Введіть номер дії - "))

        if choice == 1:
            print(f'Результат перетину множин - {sorted(set1 & set2)}')
            print(f'Потужність - {len(set1 & set2)}')
        elif choice == 2:
            print(f'Результат об\'єднання множин - {sorted(set1 | set2)}')
            print(f'Потужність - {len(set1 | set2)}')
        elif choice == 3:
            print(f'Результат симетричної різниці ({set1} ^ {set2}) - {set1 ^ set2}')
            print(f'Потужність - {len(set1 ^ set2)}')
        elif choice == 4:
            print(f'Результат різниці ({set1} - {set2}) - {sorted(set1 - set2)}')
            print(f'Потужність - {len(set1 - set2)}')
        elif choice == 5:
            print(f"Результат -")
            for row in binary_operations(set1, set2):
                print(row)
                
        if input("Бажаєте продовжити? (Y/N): ") == "N":
            break

# Program start
if __name__ == "__main__":
    main()