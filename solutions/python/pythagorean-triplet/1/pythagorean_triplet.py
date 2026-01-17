def triplets_with_sum(number):

    outer_list = []
    
    for a in range(1,number//3+1):
        for b in range(a+1,(number-a)//2+1):
                c = number - a - b
                if a**2 + b**2 == c**2:
                    outer_list.append([a, b, c])
            
    return outer_list

