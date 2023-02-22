def fun(num):
    i = 0
    while i <= num:
        if i % 2==0:
           yield i
        i +=1
        
for i in fun(10):
    print(i)