list = [1, 3, 5, 7, 9, 11, 15]
list_of_prime = []
def filter_prime(argu1):
    for i in range(2, len(argu1)):
        if argu1[i] % i == 0:
            continue
        else:
            list_of_prime.append(argu1[i])
filter_prime(list)
print(list_of_prime)