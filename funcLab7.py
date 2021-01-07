import random
def differtwovalue(x,y):
    if x>=y:
        return x-y
    else:
        return y-x
for z in range(5):
    a = random.randint(1, 30)
    b = random.randint(1, 30)
    print(a,'와',b,'의','차는',differtwovalue(a, b),'입니다.')