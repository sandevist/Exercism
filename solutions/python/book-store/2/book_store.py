def total(basket):
    # --- Step 1: sort the basket ---
    # sort by decreasing count, then by book number
    def sort_key(book):
        return (-basket.count(book), book)
    
    basket = sorted(basket, key=sort_key)

    # --- Step 2: build marginal cost dictionary dynamically ---
    def build_marginals():
        # discount rules: group_size -> multiplier
        discounts = {1: 1.00, 2: 0.95, 3: 0.90, 4: 0.80, 5: 0.75}
        base_price = 800  # 8 dollars in cents

        # compute total price for each group size
        totals = [0]  # cost for 0 books
        for k in range(1, 6):
            totals.append(int(base_price * k * discounts[k]))

        # compute marginal cost of adding each book
        marginals = [totals[i] - totals[i - 1] for i in range(1, len(totals))]
        return marginals  # [800, 720, 640, 400, 440]

    marginals = build_marginals()

    # helper to get marginal cost for a group
    def add_price(group):
        # marginal cost of adding next book based on group size
        return marginals[len(group)]

    # --- Step 3: create empty groups ---
    if not basket:
        groups = []
    else:
        max_count = basket.count(basket[0])
        groups = [[] for _ in range(max_count)]

    # --- Step 4: distribute books into groups ---
    for book in basket:
        # find groups that don't yet have this book
        possible_groups = []
        for group in groups:
            if book not in group:
                possible_groups.append(group)

        # pick the group with the smallest marginal cost
        best_group = possible_groups[0]
        best_price = add_price(best_group)
        for group in possible_groups[1:]:
            price = add_price(group)
            if price < best_price:
                best_group = group
                best_price = price

        # add book to the chosen group
        best_group.append(book)

    # --- Step 5: calculate total cost ---
    total_cost = 0
    for group in groups:
        for i in range(len(group)):
            # sum marginal cost for each book in the group
            total_cost += add_price(group[:i])

    return total_cost
