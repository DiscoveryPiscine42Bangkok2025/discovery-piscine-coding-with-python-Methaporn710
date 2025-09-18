import ast
args = ast.literal_eval(input("Enter a list of numbers: "))
numbers = [int(x) for x in args]
unique_only = [x for x in numbers if numbers.count(x) == 1]
new_u = [x + 2 for x in unique_only]
print(list(numbers))
print(list(new_u))