# Sets calculator

This program allows users to perform various set operations and binary relations using two sets of integers. The program supports the following operations:

- **Intersection**: Finds the common elements between two sets.
- **Union**: Finds all the unique elements from both sets.
- **Symmetric Difference**: Finds elements that are in either set, but not in both.
- **Difference**: Finds elements in the first set that are not in the second set.
- **Binary Relations**: Allows users to define and evaluate binary relations between the two sets based on a condition.

## Features

- Input validation for sets (only accepts integers).
- Performs standard set operations: intersection, union, symmetric difference, and difference.
- Allows the user to define custom binary relations between the two sets.
- Displays both the result of the operation and the cardinality of the result (number of elements).

## Requirements

- Python 3.x

## Usage

1. **Input Sets**: You will be prompted to input two sets of numbers (separated by commas).
2. **Choose Operation**: After entering the sets, you can choose from the following operations:
   - **1** - Intersection: Finds the common elements between two sets.
   - **2** - Union: Finds all unique elements from both sets.
   - **3** - Symmetric Difference: Finds elements in either set, but not in both.
   - **4** - Difference: Finds elements in the first set that are not in the second set.
   - **5** - Binary Relations: Prompts you to input a condition involving the elements of the sets. For example, `a > b` or `a == b`.

3. **Input Binary Condition**: When selecting the Binary Relations operation, you will need to provide a condition using the variables `a` (from the first set) and `b` (from the second set).
   If you want to use functions like `sin`, `cos`, `sqrt`, etc., use the `math` module. For example: `math.sin(a) > math.sqrt(b)`.

5. **Repeat or Exit**: After performing an operation, you can choose to continue with another operation or exit the program.

## Contributing

Feel free to fork this repository and submit pull requests. Contributions are welcome!
