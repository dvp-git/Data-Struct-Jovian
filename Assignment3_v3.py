# Match the length
def add(poly1, poly2):
    """Add two polynomials"""
    result = [0] * max(len(poly1), len(poly2))
    for i in range(len(result)):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] += poly2[i]
    return result

def resolve_len(poly1, poly2):
    if len(poly1) < len(poly2):
        poly1.append(0)
        resolve_len(poly1, poly2)
    elif len(poly2) < len(poly1):
        poly2.append(0)
        resolve_len(poly1, poly2)
    return poly1,poly2

def sub(poly1, poly2):
    """Subtract two polynomials"""
    poly1, poly2 = resolve_len(poly1, poly2)
    result = [0] * max((len(poly1), len(poly2)))
    for i in range(len(result)):
        result[i] = poly1[i] - poly2[i]
    return result

def split(poly1, poly2):
    """Split each polynomial into two smaller polynomials"""
    mid = max(len(poly1), len(poly2)) // 2
    return  (poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:])

def increase_exponent(poly, n):
    """Multiply poly1 by x^n"""
    return [0] * n + poly

def multiply_basic(poly1, poly2):
    # if len(poly1) < len(poly2):
    #     poly1 = resolve_len(poly1, poly2)
    # if len(poly1) > len(poly2):
    #     poly2 = resolve_len(poly2, poly1)
    poly1 , poly2 = resolve_len(poly1, poly2)
    print("Inside BASIC: ",poly1, poly2)
    result = [0] * (len(poly1) + len(poly2)-1)
    print(len(result))
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
            print(result)
            continue
    # Once highest number of expression terms are evaludated, happens are result[len(result//2)].
    for k in range(len(result)// 2 + 1,len(result)):
        for i in range(k,len(result)):
            print(result)
            result[k] += poly1[(i+1)%len(poly1)] * poly2[(k-i-1)%len(poly2)]

    #Remove trailing zeros'
    for k in range(len(result)-1,0,-1):
        if result[k] == 0:
            del result[k]
        else:
            break
    return result

# def multiply_dnc_optimized(poly1, poly2):
#     if len(poly1) == 1:
#         temp = [poly1[0] * poly2[i] for i in range(len(poly2))]
#         return temp
#     elif len(poly2) == 1:
#         temp = [poly2[0] * poly1[i] for i in range(len(poly1))]
#         return temp
#     (poly1_0, poly1_1),(poly2_0, poly2_1) = split(poly1, poly2)
#     print((poly1_0, poly1_1),(poly2_0, poly2_1))
#
#     U = multiply_dnc_optimized(poly1_0, poly2_0)
#
#     print((poly1_0, poly1_1),(poly2_0, poly2_1))
#     Z = multiply_dnc_optimized(poly1_1, poly2_1)
#
#     print((poly1_0, poly1_1),(poly2_0, poly2_1))
#     Y = multiply_dnc_optimized(add(poly1_0, poly1_1),add(poly2_0,poly2_1))
#
#     result = add(U , add(increase_exponent(sub(sub(Y,Z),U),len(poly1)//2),increase_exponent(Z,len(poly1))))
#     for k in range(len(result)-1,0,-1):
#         if result[k] == 0:
#             del result[k]
#         else:
#             break
#     return result
#
def multiply_dnc_optimized(poly1, poly2, threshold=4):
    print("Inside DNC:" ,poly1, poly2)
    if len(poly1) == 0:
        return 0
    elif len(poly2) == 0:
        return 0
    elif len(poly1) <= threshold  or len(poly2)  <= threshold:
        return multiply_basic(poly1, poly2)
    # elif len(poly1) == 1:
    #     return [poly1[0] * poly2[i] for i in range(len(poly2))]
    # elif len(poly2) == 1:
    #     return [poly2[0] * poly1[i] for i in range(len(poly1))]
    else:
        n = max(len(poly1) , len(poly2))
        (poly1_0, poly1_1),(poly2_0, poly2_1) = split(poly1, poly2)
#         print((poly1_0, poly1_1),(poly2_0, poly2_1))

        U = multiply_dnc_optimized(poly1_0, poly2_0)

#         print((poly1_0, poly1_1),(poly2_0, poly2_1))
        Z = multiply_dnc_optimized(poly1_1, poly2_1)

#         print((poly1_0, poly1_1),(poly2_0, poly2_1))
        Y = multiply_dnc_optimized(add(poly1_0, poly1_1),add(poly2_0,poly2_1))
        Y_Z_U = increase_exponent(sub(sub(Y,Z),U),n//2)

        result = add(add(U ,Y_Z_U),increase_exponent(Z,2*(n//2)))
        for k in range(len(result)-1,0,-1):
            if result[k] == 0:
                del result[k]
            else:
                break
        print(f"THRESHOLD : {threshold}")
        return result


""" From JOVIAN
def multiply_dnc_optimized(poly1, poly2, i=0, threshold=None):
    # print("=================ith iteration:==================================", i)
    i+=1
    if len(poly1) == 0:
        return 0
    elif len(poly2) == 0:
        return 0
    if len(poly1) == 1:
        return [poly1[0] * i for i in poly2]
    elif len(poly2) == 1:
        return [poly2[0] * i for i in poly1]
    else:
        n = max(len(poly1) , len(poly2))
        (poly1_0, poly1_1),(poly2_0, poly2_1) = split(poly1, poly2)
        # print((poly1_0, poly1_1),(poly2_0, poly2_1))

        U = multiply_dnc_optimized(poly1_0, poly2_0,i)
        #print(f"U:{U}")

        # print((poly1_0, poly1_1),(poly2_0, poly2_1))
        Z = multiply_dnc_optimized(poly1_1, poly2_1,i)
        #print(f"Z:--->{Z}")

        # print((poly1_0, poly1_1),(poly2_0, poly2_1))
        Y = multiply_dnc_optimized(add(poly1_0, poly1_1),add(poly2_0,poly2_1),i)
        #print(f"Y:--->{Y}")

        Y_Z_U = increase_exponent(sub(sub(Y,Z),U),n//2)
        #print(f"Y_Z_U:--->{Y_Z_U}")


        # Corrected the issue : Increase exponent was wrong. First calculate floor division by 2 and then raise to the multiply by 2.
        result = add(add(U ,Y_Z_U),increase_exponent(Z,2*(n//2)))
        for k in range(len(result)-1,0,-1):
            if result[k] == 0:
                del result[k]
            else:
                break
        # print(f"Result:{result}")
        # print(f"THRESHOLD : {threshold}")
        return result
"""


test0 = {     # fail
    'input': {
        'poly1': [2, 0, 5, 7, 4, 0, 0, 5],
        'poly2': [3, 4, 2, 4, 5, 0 ,3]
    },
    'output': [6, 8, 19, 49, 60, 50, 67, 66, 55, 31, 32, 25, 0, 15]
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

# print(f"==========Start test===========")
# print(f"Actual : {multiply_basic(test0['input']['poly1'],test0['input']['poly2'])}")
# print(f"Expected: {test0['output']}")
# print(f"==========End test===========")
# # Process returned 0 (0x0)        execution time : 0.303 s

#
# print(f"==========Start test===========")
# print(f"Actual : {multiply_basic(test2['input']['poly1'],test2['input']['poly2'])}")
# print(f"Expected: {test2['output']}")
# print(f"==========End test===========")
# Process returned 0 (0x0)        execution time : 0.205 s

# print(f"==========Start test===========")
# print(f"Actual : {multiply_dnc_optimized(test0['input']['poly1'],test0['input']['poly2'])}")
# print(f"Expected: {test0['output']}")
# print(f"==========End test===========")
# # # Process returned 0 (0x0)        execution time : 0.219 s


# print(f"==========Start test===========")
# # print(multiply_dnc(test1['input']['poly1'],test1['input']['poly2']) == test1['output'])
# print(f"Actual : {multiply_dnc_optimized(test1['input']['poly1'],test1['input']['poly2'])}")
# print(f"Expected: {test1['output']}")
# print(f"==========End test===========")
#
print(f"==========Start test===========")
# print(multiply_dnc(test2['input']['poly1'],test2['input']['poly2']) == test2['output'])
print(f"Actual : {multiply_dnc_optimized(test2['input']['poly1'],test2['input']['poly2'])}")
print(f"Expected: {test2['output']}")
print(f"==========End test===========")
# # Process returned 0 (0x0)        execution time : 0.304 s



# print(f"==========Start test===========")   ## Failing
# # print(multiply_dnc(test3['input']['poly1'],test3['input']['poly2']) == test3['output'])
# print(f"Actual : {multiply_dnc_optimized(test3['input']['poly1'],test3['input']['poly2'])}")
# print(f"Expected: {test3['output']}")
# print(f"==========End test===========")
#
#
# print(f"==========Start test===========")
# # print(multiply_dnc(test4['input']['poly1'],test4['input']['poly2']) == test4['output'])
# print(f"Actual : {multiply_dnc_optimized(test4['input']['poly1'],test4['input']['poly2'])}")
# print(f"Expected: {test4['output']}")
# print(f"==========End test===========")
#
#
# print(f"==========Start test===========")   ## Failing
# # print(multiply_dnc(test5['input']['poly1'],test5['input']['poly2']) == test5['output'])
# print(f"Actual : {multiply_dnc_optimized(test5['input']['poly1'],test5['input']['poly2'])}")
# print(f"Expected: {test5['output']}")
# print(f"==========End test===========")
