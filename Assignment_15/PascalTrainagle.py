from math import factorial

def binomial(x, y):
    try:
        return factorial(x) / (factorial(y) * factorial(x - y))
    except ValueError:
        return 0

def pascals_triangle(number_of_rows):
    triangle = []
    
    if number_of_rows <= 0:
        return None
    else:
        for row in range(number_of_rows+1):
            triangle.append([binomial(row, column) for column in range(row+1)])
    return triangle

x = int(input("Enter number of rows : "))
result = pascals_triangle(x)
for i in range(0, len(result)):
  print(*result[i])