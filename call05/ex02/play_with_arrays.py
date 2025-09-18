import ast
args = ast.literal_eval(input("Enter a list of numbers: "))
numbers = [int(x) for x in args]
result = [x + 2 for x in numbers if x > 5]
print(result)