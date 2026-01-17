def primes(limit):

    LIST = []

    for j in range(2,limit+1):
        count = 0
        for i in range(2,j):
            if j % i == 0:
                count +=1


        if count == 0:
            LIST.append(j)

    return LIST