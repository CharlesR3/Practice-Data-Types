import random

# Task 1: Integers and Floats

length_int = 5

width_float = 3.7

area_float = length_int * width_float

print(f'Area of the rectangle: {area_float:.2f} square units')

# Task 2: Strings

user_input_str = input("Enter a string: ")

reversed_str = user_input_str[::-1]

print(f'Reversed string: {reversed_str}')

# Task 3: Lists

random_int_list = [random.randint(1, 100)]

random_int_list.append(random.randint(1, 100))

print(f'Updated list: {random_int_list}')

# Task 4: Tuples

mixed_data_tuple = (42, 3.14, "Python", True)

print(mixed_data_tuple)

# Task 5: Dictionaries

book_info_dict = {"title": "Python Programming", "author": "Jane Doe", "publication_year": 2021, "rating": 4.5}

print(f'Book Information: {book_info_dict}')

# Task 6: Boolean Values 

bool_var_a = True

bool_var_b = False

print(f'Logical AND: {bool_var_a and bool_var_b}')
print(f'Logical OR: {bool_var_a or bool_var_b}')
print(f'Logical NOT on A: {not bool_var_a}')

# Task 7: Sets

number_list = [int(random.randint(1, 10)), int(random.randint(1, 10)), int(random.randint(1, 10)), int(random.randint(1, 10)), int(random.randint(1, 10))]

unique_numbers_set = set(number_list)

print(f'Original list: {number_list}')

print(f"Unique numbers set: {unique_numbers_set}")

# Task 8: Data Type Conversion

number_string = "123456"

number_list = [int(number_string[0]), int(number_string[1]), int(number_string[2]), int(number_string[3]), int(number_string[4]), int(number_string[5])]

print(f'String of numbers: {number_string}')

print(f'Converted to list of integers: {number_list}')

# Task 9: Formatting Task

large_float = 123456.789

print(f'Formatted as currency: ${large_float:,.2f}')