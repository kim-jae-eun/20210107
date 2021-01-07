def expr(x,y,z):
    if z=='+':
        return x+y
    elif z=='-':
        return x-y
    elif z=='*':
        return x*y
    elif z=='/':
        return x/y
    else:
        return None
a=expr(6,8,'*')
if a is None:
    print('수행 불가')
else:
    print('연산결과 :',a)