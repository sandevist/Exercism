def can_chain(dominoes):
    if not dominoes:
        return [] # return empty if chain is empty
    if len(dominoes) == 1: 
        return dominoes if dominoes[0][0] == dominoes[0][1] else None # if 1 domino check domino can be used to make a closed loop 

    stack = []  # stores tuples: (current_chain, remaining_dominoes)
    for i in range(len(dominoes)): #when iterating dominoes
        start = dominoes[i] # domino being iterated
        remain = dominoes[:i] + dominoes[i+1:] #dominoes not being iterated
        for order in [start, (start[1], start[0])]: # check the domino is both its normal position and flipped --> so loop runs twice for each iterated domino 
            stack.append(([order], remain)) # make a stack with the normal iteration and the flipped version, have a list of the non-iterated (remaining) attached 

    while stack:
        chain, remain = stack.pop() # keep removing whatever the last domino is from the remaining stack and adding to chain once match found [code loop below]
        if not remain: #if theres none left check the chain is complete
            if chain[0][0] == chain[-1][1]:
                return chain
            continue

        last_L, last_R = chain[-1] 
        for j, (L, R) in enumerate(remain): # for dominos in remaining list
            next_remain = remain[:j] + remain[j+1:] # remaining from remaining list
            if last_R == L: #check if iterated domino in remaining matches the end (last domino) in the popped/iterated chain
                stack.append((chain + [(L,R)], next_remain)) # if it odes then add it to the chain
            # try adding flipped
            if last_R == R: # smae process if it matches the flipped way
                stack.append((chain + [(R,L)], next_remain))

    return None
