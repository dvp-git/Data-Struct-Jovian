class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_travel_day = days[-1]
        total_stay = [x for x in range(1,last_travel_day + 1)]
        return self.min_spend(days, costs, total_stay,idx=days[-1])

# Recursive dynamic program function for calculating minimum cost
    def min_spend(self,days,costs , total_stay ,idx=0):
        if idx <= 0:
            return 0
        elif total_stay[idx-1] in days:
            cost_1 = costs[0] + self.min_spend(days,costs, total_stay, idx-1)
            # print(f"Cost_1 : {cost_1}")
            cost_7 = costs[1] + self.min_spend(days,costs, total_stay, idx-7)
            # print(f"Cost_7 : {cost_7}")
            cost_30 = costs[2] + self.min_spend(days,costs, total_stay, idx-30)
            # print(f"Cost_30 : {cost_30}")
            min_spent = min(cost_1, min(cost_7, cost_30))
            # print(f"Min Spend idx in ticket_day_pass:{min_spent}")
        else:
            min_spent = self.min_spend(days, costs, total_stay,idx-1)
            # print(f"Min Spend idx not in ticket_day_pass:{min_spent}")
        return min_spent



""" Memoized solution"""
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_travel_day = days[-1]
        total_stay = [x for x in range(1,last_travel_day + 1)]
        memoized_cache = [0 for _ in range(0,len(total_stay))]
        return self.min_spend(days, costs, total_stay, memoized_cache, idx=days[-1])

# Recursive dynamic program function for calculating minimum cost
    def min_spend(self, days, costs, total_stay, memoized_cache, idx=0):
        if idx <= 0:
            return 0
        if memoized_cache[idx-1] != 0:
            return memoized_cache[idx-1]
        if len(costs) == 1:
            return costs[0] * days
        elif total_stay[idx-1] in days:
            cost_1 = costs[0] + self.min_spend(days, costs, total_stay, memoized_cache, idx-1)
            # print(f"Cost_1 : {cost_1}")
            cost_7 = costs[1] + self.min_spend(days, costs, total_stay, memoized_cache, idx-7)
            # print(f"Cost_7 : {cost_7}")
            cost_30 = costs[2] + self.min_spend(days, costs, total_stay, memoized_cache, idx-30)
            # print(f"Cost_30 : {cost_30}")
            min_spent = min(cost_1, min(cost_7, cost_30))
            # print(f"Min Spend idx in ticket_day_pass:{min_spent}")
        else:
            min_spent = self.min_spend(days, costs, total_stay, memoized_cache, idx-1)
            # print(f"Min Spend idx not in ticket_day_pass:{min_spent}")
        memoized_cache[idx-1] =  min_spent
        return memoized_cache[idx-1]
