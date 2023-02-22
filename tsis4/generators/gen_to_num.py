def fun(num):
    i =1
    while i <= num:
        yield i**2
        i +=1


for i in fun(10):
    print(i)