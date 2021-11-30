
# Using the memoised solution to the DP problem

def mincostTickets_memoized(days, costs):
    last_travel_day = days[-1]
    total_stay = [x for x in range(1,last_travel_day + 1)]
    memoized_cache = [0 for _ in range(0,len(total_stay))]
    return min_spend_memoized(days, costs, total_stay, memoized_cache, idx=days[-1])

# Recursive dynamic program function for calculating minimum cost
def min_spend_memoized(days, costs ,total_stay, memoized_cache, idx=0):
    if idx <= 0:
        return 0
    if memoized_cache[idx-1]!= 0:
        return memoized_cache[idx-1]
    if len(costs) == 1 :
        return costs[0] * len(days)
    elif total_stay[idx-1] in days:
        cost_1 = costs[0] + min_spend_memoized(days, costs, total_stay, memoized_cache, idx-1)
        print(f"Cost_1 : {cost_1}")

        cost_7 = costs[1] + min_spend_memoized(days, costs, total_stay, memoized_cache, idx-7)
        print(f"Cost_7 : {cost_7}")

        cost_30 = costs[2] + min_spend_memoized(days, costs, total_stay, memoized_cache, idx-30)
        print(f"Cost_30 : {cost_30}")

        min_spent = min(cost_1, min(cost_7, cost_30))
        print(f"Min Spend idx in ticket_day_pass:{min_spent}")
    else:
        min_spent = min_spend_memoized(days, costs, total_stay, memoized_cache, idx-1)
        print(f"Min Spend idx not in ticket_day_pass:{min_spent}")
    memoized_cache[idx-1] =  min_spent
    return memoized_cache[idx-1]



days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
print(mincostTickets_memoized(days, costs))

# 
# days = [1, 7, 9, 21, 25]
# costs = [5]
# print(mincostTickets_memoized(days, costs))
#
#
# #
# days2 = [x for x in range(1, 10)]
# costs2 = [2,7,15]
# print(mincostTickets_memoized(days2, costs2))
# # #
# days3 = [33 ,34, 35, 36, 37, 40 ,42]
# costs3 = [3 ,9 ,50]
# print(mincostTickets_memoized(days3, costs3))
# #
# #
# #
# # #
# days4 = [1, 7, 30]
# costs4 =  [3, 8, 24]
# print(mincostTickets_memoized(days4, costs4))
#
#
# days5 = [1, 7, 8, 9, 10, 11, 12, 13, 14, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
# costs5 = [3 ,8 ,24]
# print(mincostTickets_memoized(days5, costs5))
