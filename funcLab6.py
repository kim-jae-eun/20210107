def print_gugudan(n):
    if type(n)!=int:
        return
    elif n<1 or n>9:
        return
    else:
        for x in range(1,10):
            print(n,'×',x,'=',n*x)
    print()

print_gugudan(4)
print_gugudan(9)
print_gugudan(13)
print_gugudan('안녕')