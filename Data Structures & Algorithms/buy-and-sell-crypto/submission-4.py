class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        l = 0 
        buy = prices[l]
        r = l + 1
        while r < len(prices):
            print(f'buy:{prices[l]}, sell:{prices[r]}, max:{max_profit}, current:{(prices[r] - prices[l])}')
            max_profit = max(max_profit, (prices[r] - prices[l]))
            if prices[r] < prices[l]:
                l = r
        
            r+=1

        return max_profit 

        # prices=[2,1,2,1,0,1,2]
        # buy: 2 sell: 1 max:0 curr:-1
        # buy: 1 sell: 2 max:0 curr: 1
        # buy: 1 sell: 1 max: 1 curr:0
        # buy: 1 sell: 0 max: 1 curr: 1
        # buy 
