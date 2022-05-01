from typing import List

# 테스트케이스 수작업으로 테스트해보고
# 쉽게 풀리는 문제인지 잘 가늠해보기 

# O(n)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         benefit = 0
#         min_price = float('inf')

#         for cur_price in prices:
#             min_price = min (min_price,cur_price)
#             benefit = max(benefit, cur_price-min_price)

#         return benefit

