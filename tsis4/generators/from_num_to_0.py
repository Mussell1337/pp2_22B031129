def fun(num):
    i = num
    while i >= 0:
        yield i
        i -= 1

for i in fun(10):
    print(i)