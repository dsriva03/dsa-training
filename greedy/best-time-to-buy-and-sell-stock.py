# 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def best_time_to_buy_and_sell_stock(prices):
    maxProfit = 0
    minPrice = float('inf')

    for price in prices:
        minPrice = min(minPrice, price)
        profit = price - minPrice
        maxProfit = max(maxProfit, profit)

    return maxProfit


# Input: 
# Output: 5
prices = [7,1,5,3,6,4]
print(best_time_to_buy_and_sell_stock(prices))
