def print_triangle(n):
    if 1<=n<=10:
        for x in range(n,0,-1):
            print('@'*x)
    else:
        return
    print()
print_triangle(2)
print_triangle(5)
print_triangle(14)