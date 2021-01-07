def print_triangle(n):
    if n<1 or n>10:
        return
    for x in range(n+1):
        print('*'*x)
print_triangle(2)
print_triangle(5)
print_triangle(11)