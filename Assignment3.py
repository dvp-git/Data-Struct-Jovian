""" Verson 1 """
#def multiply_basic(poly1, poly2):
#     result = [0] * (len(poly1) + len(poly2) - 1)
#     for i in range(len(poly1)):
#         for j in range(len(poly2)):
#             result[i+j] += poly1[i] * poly2[j]
#     return result

# def multiply_basic(poly1, poly2):
#     result = [0] * (len(poly1) + len(poly2)-1)
#     # print(len(result))
#     for k in range(len(result)//2 + 1):
#         # if k <= len(result)//2:
#         for i in range((k%len(poly1))+1):
#             result[k] += poly1[i%len(poly1)] * poly2[(k-i)%len(poly2)]
#             continue
#     for k in range(len(result)// 2 + 1,len(result)):
#         for i in range(k,len(result)):
#             result[k] += poly1[(i+1)%len(poly1)]*poly2[(k-i-1)%len(poly2)]
#             # result[4] += poly1[1]*poly2[3] + poly1[2]*poly2[2] + poly1[3]*poly2[1]
#             # result[5] += poly1[2]*poly2[3] + poly1[3]*poly2[2]
#             # result[6] += poly1[3]*poly2[3]
#     return result

""" Verson 2 ( working on tests, need to remove 0's) """
def multiply_basic(poly1, poly2):
    if len(poly1) < len(poly2):
        poly1 = resolve_len(poly1, poly2)
    if len(poly1) > len(poly2):
        poly2 = resolve_len(poly2, poly1)
    result = [0] * (len(poly1) + len(poly2)-1)
    # print(len(result))
    # For i = 0, k = 0 to len(result)// 2
    # result[0] = a[0] * b[0]
    # result[1] = a[0] * b[1] + a[1] * b[0]
    # result[2] = a[0] * b[2] + a[1] * b[1] + a[2] * b[0]
    # result[3] = a[0] * b[3] + a[1] * b[2] + a[2] * b[1] + a[3] * b[0]
    # In general result[k] += a[i] * b[k-i] until k reaches len(result)//2
    for k in range(len(result)//2 + 1):
        # if k <= len(result)//2:
        for i in range((k%len(poly1))+1):
            result[k] += poly1[i%len(poly1)] * poly2[(k-i)%len(poly2)]
            continue
    # Once highest number of expression terms are evaludated, happens are result[len(result//2)].
    for k in range(len(result)// 2 + 1,len(result)):
        for i in range(k,len(result)):
            result[k] += poly1[(i+1)%len(poly1)]*poly2[(k-i-1)%len(poly2)]

    #Remove trailing zeros'
    for k in range(len(result)-1,0,-1):
        if result[k] == 0:
            del result[k]
        else:
            break
    return result

# Match the length
def resolve_len(poly1, poly2):
    if len(poly1) == len(poly2):
        return poly1
    if len(poly1) < len(poly2):
        poly1.append(0)
        poly1 = resolve_len(poly1, poly2)
    return poly1


test0 = {     # fail
    'input': {
        'poly1': [2, 0, 5, 7],
        'poly2': [3, 4, 2]
    },
    'output': [6, 8, 19, 41, 38, 14]
}
test1 = {
    'input': {
        'poly1': [7],
        'poly2': [2]
    },
    'output': [14]
}
test2 = {
    'input': {
        'poly1': [1, 3, 5, 7],
        'poly2': [1, 3, 5, 7]
    },
    'output': [1, 6, 19, 44, 67, 70, 49]
}
test3 = {     # fail
    'input': {
        'poly1': [2, 4, 6, 10],
        'poly2': [3]
    },
    'output': [6, 12, 18, 30]
}
test4 = {
    'input': {
        'poly1': [0, 1, 19, 2],
        'poly2': [2, 2, 2, 2]
    },
    'output': [0, 2, 40, 44, 44, 42, 4]
}
test5 = {     # fail
    'input': {
        'poly1': [1, 2, 3, 4],
        'poly2': [0, 0, 0, 0]
    },
    'output': [0]
}


print(f"==========Start test===========")  ## Failing
print(multiply_basic(test0['input']['poly1'],test0['input']['poly2']) == test0['output'])
print(f"Actual : {multiply_basic(test0['input']['poly1'],test0['input']['poly2'])}")
print(f"Expected: {test0['output']}")
print(f"==========End test===========")

print(f"==========Start test===========")
print(multiply_basic(test1['input']['poly1'],test1['input']['poly2']) == test1['output'])
print(f"Actual : {multiply_basic(test1['input']['poly1'],test1['input']['poly2'])}")
print(f"Expected: {test1['output']}")
print(f"==========End test===========")

print(f"==========Start test===========")
print(multiply_basic(test2['input']['poly1'],test2['input']['poly2']) == test2['output'])
print(f"Actual : {multiply_basic(test2['input']['poly1'],test2['input']['poly2'])}")
print(f"Expected: {test2['output']}")
print(f"==========End test===========")

print(f"==========Start test===========")   ## Failing
print(multiply_basic(test3['input']['poly1'],test3['input']['poly2']) == test3['output'])
print(f"Actual : {multiply_basic(test3['input']['poly1'],test3['input']['poly2'])}")
print(f"Expected: {test3['output']}")
print(f"==========End test===========")


print(f"==========Start test===========")
print(multiply_basic(test4['input']['poly1'],test4['input']['poly2']) == test4['output'])
print(f"Actual : {multiply_basic(test4['input']['poly1'],test4['input']['poly2'])}")
print(f"Expected: {test4['output']}")
print(f"==========End test===========")


print(f"==========Start test===========")   ## Failing
print(multiply_basic(test5['input']['poly1'],test5['input']['poly2']) == test5['output'])
print(f"Actual : {multiply_basic(test5['input']['poly1'],test5['input']['poly2'])}")
print(f"Expected: {test5['output']}")
print(f"==========End test===========")


#
