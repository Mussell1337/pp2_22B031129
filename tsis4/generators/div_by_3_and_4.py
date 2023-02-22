def fun(num):
    i = 0
    while i <= num:
        if i % 3 == 0 and i % 4 == 0:
            yield i
        i += 1

for i in fun(13):
    print(i)
