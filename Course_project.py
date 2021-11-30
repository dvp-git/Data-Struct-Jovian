"""
Finding the minimum cost

In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.\
"""



# def minimum_cost(days, costs, ticket_day_pass, idx=0):
#     if idx <= 0:
#         return 0
#     if len(costs) ==1 :
#             return costs[0] + minimum_cost(days, costs, ticket_day_pass, idx-1)
#     elif ticket_day_pass[(idx)-1] in days:
#         cost_1 = costs[0] + minimum_cost(days, costs, ticket_day_pass, idx-1)
#         print(f"Cost_1 : {cost_1}")
#         cost_7 = costs[1] + minimum_cost(days, costs, ticket_day_pass, idx-7)
#         print(f"Cost_7 : {cost_7}")
#         cost_30 = costs[2] + minimum_cost(days, costs, ticket_day_pass, idx-30)
#         print(f"Cost_30 : {cost_30}")
#         print(f"Comparing {cost_1}, {cost_7}, {cost_30}")
#         min_spent = min(cost_1, min(cost_7, cost_30))
#         print(f"Min Spend idx in ticket_day_pass:{min_spent}")
#     else:
#         min_spent = minimum_cost(days, costs, ticket_day_pass, idx-1)
#         print(f"Min Spend idx not in ticket_day_pass:{min_spent}")
#     return min_spent




def mincostTickets(days, costs):
    last_travel_day = days[-1]
    total_stay = [x for x in range(1,last_travel_day + 1)]
    return min_spend(days, costs, total_stay, idx=days[-1])

# Recursive dynamic program function for calculating minimum cost
def min_spend(days, costs ,total_stay, idx=0):
    if idx <= 0:
        return 0
    if len(costs) ==1 :
        #return costs[0] + min_spend(days, costs, total_stay, idx-1)
        return costs[0] * len(days)
    elif total_stay[idx-1] in days:
        cost_1 = costs[0] + min_spend(days, costs, total_stay, idx-1)
        print(f"Cost_1 : {cost_1}")

        cost_7 = costs[1] + min_spend(days, costs, total_stay, idx-7)
        print(f"Cost_7 : {cost_7}")

        cost_30 = costs[2] + min_spend(days, costs, total_stay, idx-30)
        print(f"Cost_30 : {cost_30}")

        min_spent = min(cost_1, min(cost_7, cost_30))
        print(f"Min Spend idx in ticket_day_pass:{min_spent}")
    else:
        min_spent = min_spend(days, costs, total_stay, idx-1)
        print(f"Min Spend idx not in ticket_day_pass:{min_spent}")
    return min_spent



days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
print(mincostTickets(days, costs))


# days = [1, 7, 9, 21, 25]
# costs = [5]
# print(mincostTickets(days, costs))
#
#
# #
# days2 = [x for x in range(1, 10)]
# costs2 = [2,7,15]
# print(mincostTickets(days2, costs2))
# # #
# days3 = [33 ,34, 35, 36, 37, 40 ,42]
# costs3 = [3 ,9 ,50]
# print(mincostTickets(days3, costs3))
# #
# #
# #
# # #
# days4 = [1, 7, 30]
# costs4 =  [3, 8, 24]
# print(mincostTickets(days4, costs4))
#
#
# days5 = [1, 7, 8, 9, 10, 11, 12, 13, 14, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
# costs5 = [3 ,8 ,24]
# print(mincostTickets(days5, costs5))

# Process returned 0 (0x0)        execution time : 0.168 s
