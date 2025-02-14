import math

# Input the set elments
def data_input():
    while True:
        print('Input the set elments (1, 2, 3, ...):')
        input1 = input()
        try:
            set1 = set(input1.split(", "))
            for x in set1:
                if not x.isdigit():
                    raise ValueError
            return set1
        except ValueError:
            print("Error! Please enter a valid set of numbers")

# Binary operations proccessing
def binary_operations(set1, set2):
    set1, set2 = list(set1), list(set2)
    set1.reverse(), set2.reverse()
    check = 0
    print("\nRead the instructions in README.md")
    user_condition = input("Input a condition using 'a' and 'b': ")
    result = []
    print("Result - ")
    for a in set1:
        a = int(a)
        matrix = []
        for b in set2:
            b = int(b)
            try:
                matrix.append(1 if eval(user_condition) else 0)
            except Exception as e:
                print(f"Error in condition:{e}")
                check = 1
                break
        if check == 1: break
        result.append(matrix)
    return result

# The main part of program
def main():
    set1 = data_input()
    set2 = data_input()
    while True:
        print('\nPick the set operation you need:\n1 - Intersection\n2 - Union\n3 - Symmetric Difference\n4 - Difference\n5 - Binary Relations')
        choice = int(input("Input operation number - "))

        if choice == 1:
            print(f'Result of sets intersection - {sorted(set1 & set2)}')
            print(f'Cardinality of intersection - {len(set1 & set2)}')
        elif choice == 2:
            print(f'Result of sets union - {sorted(set1 | set2)}')
            print(f'Cardinality of union - {len(set1 | set2)}')
        elif choice == 3:
            print(f'Result of symmetric difference ({set1} ^ {set2}) - {sorted(set1 ^ set2)}')
            print(f'Cardinality of symmetric difference - {len(set1 ^ set2)}')
        elif choice == 4:
            print(f'Result of difference ({set1} - {set2}) - {sorted(set1 - set2)}')
            print(f'Cardinality of difference - {len(set1 - set2)}')
        elif choice == 5:
            for row in binary_operations(set1, set2):
                print(row)
                
        if input("Do you want to continue? (Y/N): ") == "N":
            break

# Program start
if __name__ == "__main__":
    main()