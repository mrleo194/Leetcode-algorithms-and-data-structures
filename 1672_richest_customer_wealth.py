def maximumWealth(accounts):
    """
    A customer's wealth is the amount of money 
    they have in all their bank accounts. 
    The richest customer is the customer 
    that has the maximum wealth.
    Example: 
        Input: accounts = [[1,2,3],[3,2,1]]
        Output: 6
    """
    wealth = []
    for customers in accounts:
        total = 0
        for money in customers:
            total += money
        wealth.append(total) 
    return max(wealth)

if __name__ == "__main__":
    accounts = [[1,5],[7,3],[3,5]]
    ans = maximumWealth(accounts)
    print(ans)
