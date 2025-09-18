import ast
args = ast.literal_eval(input("Enter a list of numbers: "))
print([x + 2 for x in args])