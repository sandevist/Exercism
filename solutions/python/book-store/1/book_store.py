def total(basket):
    # Count how many copies of each book type (1-5) we have
    book_counts = [0] * 5
    for book in basket:
        if 1 <= book <= 5:
            book_counts[book - 1] += 1

    # Discount multipliers for different group sizes
    discount_rates = {
        1: 1.00,  # 0% discount
        2: 0.95,  # 5% discount
        3: 0.90,  # 10% discount
        4: 0.80,  # 20% discount
        5: 0.75   # 25% discount
    }

    # Store previously calculated results to avoid redundant calculations
    calculated_results = {}

    def calculate_min_cost(remaining_books):
        """
        Calculate the minimum cost for the remaining books
        remaining_books: list of remaining copies of each book type
        """
        # Convert to tuple for use as dictionary key
        current_state = tuple(remaining_books)
        
        # Return previously calculated result if available
        if current_state in calculated_results:
            return calculated_results[current_state]

        # Base case: no books left to process
        if all(count == 0 for count in remaining_books):
            return 0

        best_total_cost = float('inf')

        # Try all possible group sizes from largest to smallest
        for group_size in range(5, 0, -1):
            # Get all available books (indices where count > 0)
            available_books = [index for index, count in enumerate(remaining_books) if count > 0]
            
            # Need at least group_size distinct books available
            if len(available_books) >= group_size:
                # Generate all possible combinations of group_size distinct books
                from itertools import combinations
                for book_selection in combinations(available_books, group_size):
                    # Create a copy of remaining books
                    new_remaining = list(remaining_books)
                    
                    # Remove one copy of each selected book
                    for book_index in book_selection:
                        new_remaining[book_index] -= 1
                    
                    # Calculate cost for this group
                    group_cost = group_size * 800 * discount_rates[group_size]
                    
                    # Recursively calculate cost for remaining books
                    remaining_cost = calculate_min_cost(new_remaining)
                    
                    # Total cost for this grouping option
                    total_cost = group_cost + remaining_cost
                    
                    # Keep the best (lowest) total cost
                    best_total_cost = min(best_total_cost, total_cost)

        # Store the result for this state
        calculated_results[current_state] = best_total_cost
        return best_total_cost

    # Start the calculation with all books
    final_cost = calculate_min_cost(book_counts)
    
    # Round to 2 decimal places for currency format
    return round(final_cost, 2)

# -------------------------------------------------------------------
# UNRAVELLED RECURSION STORY (using your variable names)
#
# Example: basket = [1,2]
#
# 1. basket = [1,2] → counts = [1,1,0,0,0]
#
# 2. First call: calculate_cost([1,1,0,0,0])
#    state = (1,1,0,0,0)
#    Not in results → compute
#
# 3. Try group_size = 5,4,3 → not enough books → skip
#
# 4. group_size = 2:
#       available = [0,1] (both books available)
#       new_count = [0,0,0,0,0]
#       GROUP_COST = 2*8*0.95 = 15.2
#       TOTAL = 15.2 + calculate_cost([0,0,0,0,0])
#
#       Recurse: calculate_cost([0,0,0,0,0])
#           Base case → return 0
#       TOTAL = 15.2 + 0 = 15.2
#       BEST = 15.2
#
# 5. group_size = 1:
#       available = [0,1]
#       Take first book → new_count = [0,1,0,0,0]
#       GROUP_COST = 1*8*1.0 = 8
#       TOTAL = 8 + calculate_cost([0,1,0,0,0])
#
#       Recurse: calculate_cost([0,1,0,0,0])
#           group_size = 1 only
#           new_count = [0,0,0,0,0]
#           GROUP_COST = 8
#           TOTAL = 8 + 0 = 8
#           BEST = 8
#           results[(0,1,0,0,0)] = 8
#
#       Back to first call:
#       TOTAL = 8 + 8 = 16
#       Compare with previous BEST = 15.2 → BEST remains 15.2
#
# 6. Memoize first call:
#       results[(1,1,0,0,0)] = 15.2
#
# 7. Return final_cost = 15.2
#
# KEY IDEA:
# - Each RECURSED_COUNT is a snapshot of remaining books
# - state = tuple(RECURSED_COUNT) allows us to memoize results
# - The recursion explores all grouping possibilities
# - Base case stops recursion when no books are left
# - BEST keeps track of minimum total cost across all options
# - results dictionary prevents recalculating the same state
# - final_cost is the cheapest price for the whole basket
# -------------------------------------------------------------------
