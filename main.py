



def pero(x):
    while x > 0:
        yield x
        x -=1


a = pero(3)

print(a)