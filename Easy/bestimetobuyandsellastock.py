# 121. Best time to buy and sell stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        lowestprice = prices[0]
        for price in prices:
            if lowestprice>price:
                lowestprice = price
            elif price-lowestprice>mp:
                    mp = price-lowestprice
        return mp