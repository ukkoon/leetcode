from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        return self.localMaxProfit(prices=prices,idx=0)
    
    def localMaxProfit(self, prices: List[int], idx) ->int:
        if idx+1==len(prices):
            return 0
            
        elif prices[idx+1] > prices[idx]:
            return prices[idx+1] - prices[idx]+self.localMaxProfit(prices=prices,idx=idx+1)
        
        else:
            return self.localMaxProfit(prices=prices,idx=idx+1)