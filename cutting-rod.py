def cutRod(prices, n):
    max_value = 0
    if n <= 0:
        return 0
    elif len(prices) == 1:
        return prices[0]
    else:
        for i in range(0, n):
            # Recursively cutRod(n-i)
            individual_price = prices[i]
            max_value = max(max_value, individual_price + cutRod(prices, n-i-1))
            print(individual_price + cutRod(prices, n-i-1))
        print("Length of piece",i+1)
        print("Max_Value :",max_value)
        print("---------------")
    return max_value





prices = [1, 7, 6, 12, 10, 17, 17, 17, 17]

prices2 = [3 , 5  ,8 ,9 ,10 , 17, 17 ,20]

prices3 = [5, 2, 3, 8]
table = [0 for _ in range(4)]
print(cutRod(prices2,3))



# print(cutRod(prince2, 8))
