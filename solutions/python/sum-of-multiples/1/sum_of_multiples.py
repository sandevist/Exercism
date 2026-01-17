def sum_of_multiples(limit, multiples):

    ALL = set()
    for i in multiples:
        if i == 0:
            continue     
        ALL |= set(range(i,limit,i))


    SUM = sum(ALL)

    return SUM


        
